#!/usr/bin/env python3
"""Validate the observable delivery contract of a final architecture HTML report."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class ReportParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.local_targets: list[str] = []
        self.remote_dependencies: list[str] = []
        self.tags: Counter[str] = Counter()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags[tag] += 1
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        for key in ("src", "href"):
            value = values.get(key)
            if not value or value.startswith(("#", "data:", "mailto:", "tel:", "javascript:")):
                continue
            parsed = urlparse(value)
            if parsed.scheme in {"http", "https"}:
                if (tag == "script" and key == "src") or (tag == "link" and key == "href"):
                    self.remote_dependencies.append(value)
                continue
            if parsed.scheme == "file":
                self.local_targets.append(unquote(parsed.path))
            elif not parsed.scheme:
                self.local_targets.append(unquote(parsed.path))


REQUIRED_CONCEPTS: list[tuple[str, str]] = [
    ("执行摘要", r"执行摘要|Executive\s+Summary"),
    ("证据来源与缺口", r"证据来源|证据缺口|Evidence\s+Sources"),
    ("核心功能域", r"核心功能域|Functional\s+Domains"),
    ("端到端五流", r"端到端|five[-\s]?flow|五条流"),
    ("九层架构", r"九层|产品分层架构|Nine[-\s]?Layer"),
    ("Agent/工具/上下文", r"Agent.{0,40}工具|Agent.{0,40}context"),
    ("全局上下文", r"全局上下文|Global\s+Context"),
    ("知识与资产", r"知识.{0,20}(资产|公共)|Knowledge"),
    ("模型接入与路由", r"模型.{0,20}(接入|路由)|Model.{0,20}Routing"),
    ("底层能力/选型", r"底层.{0,20}(架构|选型|能力)|Technology"),
    ("数据实体与 ER", r"数据实体|ER\s*(图|Diagram)|erDiagram"),
    ("端到端时序", r"时序图|sequenceDiagram|Sequence\s+Diagram"),
    ("全景架构主图", r"全景.{0,15}架构|Panoramic"),
    ("As-Is", r"As[-\s]?Is"),
    ("To-Be", r"To[-\s]?Be"),
    ("关键风险", r"关键.{0,10}风险|Architecture\s+Risks"),
    ("证据追溯", r"证据追溯|Traceability"),
    ("未知与停止点", r"无法确认|尚未确认|未知|Unresolved"),
]

VISUAL_REQUIRED_CONCEPTS: list[tuple[str, str]] = [
    ("九层主图", r"九层|9\s*层|L1.{0,120}L9"),
    ("横切关注点", r"横切关注点|cross[-\s]?cutting"),
    ("端到端五流", r"五条流|五流|用户交互.{0,120}Agent.{0,120}工具.{0,120}(上下文|数据).{0,120}(资产|输出)"),
    ("证据等级", r"【已确认】.{0,200}【合理推断】.{0,200}【建议设计】.{0,200}【未知】"),
    ("证据追溯", r"证据编号|证据追溯|Traceability"),
    ("证据分布", r"证据等级(占比|分布)|Evidence\s+Distribution"),
    ("未知问题", r"无法确认|尚未确认|未知|Unresolved"),
    ("阅读说明", r"看图说明|阅读指南|使用方法|Reading\s+Guide"),
]


def resolve_target(report: Path, target: str) -> Path:
    candidate = Path(target)
    return candidate if candidate.is_absolute() else report.parent / candidate


def validate(report: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not report.is_file():
        return [f"report does not exist: {report}"], warnings
    if report.stat().st_size < 5000:
        errors.append("report is unexpectedly small (< 5 KB)")

    text = report.read_text(encoding="utf-8")
    lower = text.lower()
    if "<!doctype html" not in lower:
        errors.append("missing HTML doctype")
    if re.search(r"\b(?:TODO|TBD|lorem ipsum)\b|\{\{[^}]+\}\}", text, re.I):
        errors.append("unfinished placeholder text remains")
    if "@media" not in text:
        errors.append("missing responsive CSS media query")
    if not re.search(r"@media\s+(?:print|[^\{]*print)", text, re.I):
        errors.append("missing print CSS")
    if not re.search(r"<svg\b|sequenceDiagram|erDiagram|flowchart\s|graph\s+(?:TD|LR)", text, re.I):
        errors.append("no architecture/sequence/ER diagram or readable diagram source found")

    for label, pattern in REQUIRED_CONCEPTS:
        if not re.search(pattern, text, re.I | re.S):
            errors.append(f"missing required section/concept: {label}")

    for level in ("【已确认】", "【合理推断】", "【建议设计】", "【未知】"):
        if level not in text:
            errors.append(f"missing evidence-level label: {level}")

    evidence_ids = set(re.findall(r"E-(?:J|A|P|R|O)-\d{3}", text))
    if not evidence_ids:
        errors.append("no stage evidence IDs found (expected E-J/A/P/R/O-###)")
    elif len(evidence_ids) < 4:
        warnings.append(f"only {len(evidence_ids)} unique evidence IDs found")

    parser = ReportParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # HTMLParser is tolerant; any exception is meaningful.
        errors.append(f"HTML parser failed: {exc}")

    duplicates = sorted(value for value, count in Counter(parser.ids).items() if count > 1)
    if duplicates:
        errors.append("duplicate HTML ids: " + ", ".join(duplicates))
    if parser.tags["h1"] == 0 or parser.tags["main"] == 0:
        errors.append("missing semantic h1 or main element")
    if parser.remote_dependencies:
        errors.append("remote script/stylesheet dependencies break offline delivery: " + ", ".join(parser.remote_dependencies))

    missing_targets: list[str] = []
    for target in parser.local_targets:
        if not target or target.endswith("/"):
            continue
        resolved = resolve_target(report, target)
        if not resolved.exists():
            missing_targets.append(target)
    if missing_targets:
        errors.append("missing local linked assets: " + ", ".join(sorted(set(missing_targets))))

    if "overflow-x" not in lower:
        warnings.append("no explicit horizontal overflow handling found for wide diagrams/tables")
    if "evidence-led" not in lower and "证据" not in text[:3000]:
        warnings.append("report provenance is not clearly stated near the top")

    return errors, warnings


def validate_visual(report: Path) -> tuple[list[str], list[str]]:
    """Validate the dedicated stage-5 layered visual without requiring stage-4 sections."""
    errors: list[str] = []
    warnings: list[str] = []
    if not report.is_file():
        return [f"report does not exist: {report}"], warnings
    if report.stat().st_size < 5000:
        errors.append("visual is unexpectedly small (< 5 KB)")
    text = report.read_text(encoding="utf-8")
    lower = text.lower()
    if "<!doctype html" not in lower:
        errors.append("missing HTML doctype")
    if re.search(r"\b(?:TODO|TBD|lorem ipsum)\b|\{\{[^}]+\}\}", text, re.I):
        errors.append("unfinished placeholder text remains")
    if "@media" not in text:
        errors.append("missing responsive CSS media query")
    if not re.search(r"@media\s+(?:print|[^\{]*print)", text, re.I):
        errors.append("missing print CSS")
    if "overflow-x" not in lower:
        errors.append("missing horizontal overflow handling")
    for label, pattern in VISUAL_REQUIRED_CONCEPTS:
        if not re.search(pattern, text, re.I | re.S):
            errors.append(f"missing visual section/concept: {label}")
    for layer in range(1, 10):
        if not re.search(rf"(?:L|Layer\s*){layer}\b|第?{layer}\s*层", text, re.I):
            errors.append(f"missing architecture layer L{layer}")
    parser = ReportParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:
        errors.append(f"HTML parser failed: {exc}")
    duplicates = sorted(value for value, count in Counter(parser.ids).items() if count > 1)
    if duplicates:
        errors.append("duplicate HTML ids: " + ", ".join(duplicates))
    if parser.tags["h1"] == 0 or parser.tags["main"] == 0:
        errors.append("missing semantic h1 or main element")
    if parser.remote_dependencies:
        errors.append("remote script/stylesheet dependencies break offline delivery: " + ", ".join(parser.remote_dependencies))
    missing_targets: list[str] = []
    for target in parser.local_targets:
        if not target or target.endswith("/"):
            continue
        if not resolve_target(report, target).exists():
            missing_targets.append(target)
    if missing_targets:
        errors.append("missing local linked assets: " + ", ".join(sorted(set(missing_targets))))
    evidence_ids = set(re.findall(r"E-(?:J|A|P|R|O)-\d{3}", text))
    if len(evidence_ids) < 4:
        warnings.append(f"only {len(evidence_ids)} unique evidence IDs found")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Path to stage-4/stage-5 HTML, or a delivery directory")
    args = parser.parse_args()
    target = args.report.expanduser().resolve()
    reports: list[Path]
    if target.is_dir():
        reports = sorted(target.glob("04-*.html")) + sorted(target.glob("05-*.html"))
        if not reports:
            print(f"FAILED: no 04-/05- HTML files found in {target}")
            return 1
    else:
        reports = [target]
    total_errors = 0
    total_warnings = 0
    for report in reports:
        is_visual = report.name.startswith("05-") or "架构分层图" in report.name
        errors, warnings = validate_visual(report) if is_visual else validate(report)
        print(f"Validated: {report} ({'stage-5 visual' if is_visual else 'stage-4 architecture'})")
        for warning in warnings:
            print(f"WARNING: {warning}")
        for error in errors:
            print(f"ERROR: {error}")
        total_errors += len(errors)
        total_warnings += len(warnings)
    if total_errors:
        print(f"FAILED: {total_errors} error(s), {total_warnings} warning(s)")
        return 1
    print(f"PASSED: 0 errors, {total_warnings} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
