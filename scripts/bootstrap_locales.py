#!/usr/bin/env python3
"""Create or refresh locale directories under HelpDocs/content.

Usage (from repo root):
  python3 HelpDocs/content/scripts/bootstrap_locales.py
  python3 HelpDocs/content/scripts/bootstrap_locales.py --locale de --locale ja
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

CONTENT = Path(__file__).resolve().parents[1]
TEMPLATES = CONTENT / "_templates"

LOCALES: list[tuple[str, str]] = [
    ("de", "German"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("nl", "Dutch"),
    ("pt-BR", "Brazilian Portuguese"),
    ("zh-Hans", "Simplified Chinese"),
    ("zh-Hant", "Traditional Chinese"),
    ("hu", "Hungarian"),
]


def fill(template: str, code: str, name: str) -> str:
    return template.replace("{{LOCALE_CODE}}", code).replace("{{LOCALE_NAME}}", name)


def bootstrap_locale(code: str, name: str, force_config: bool) -> None:
    loc_dir = CONTENT / code
    loc_dir.mkdir(exist_ok=True)

    config_en = CONTENT / "config.yaml"
    if not config_en.exists():
        raise SystemExit(f"Missing English master: {config_en}")

    header_path = TEMPLATES / "config.locale.header.yaml"
    header = header_path.read_text(encoding="utf-8") if header_path.exists() else ""
    config_dst = loc_dir / "config.yaml"
    if force_config or not config_dst.exists():
        body = config_en.read_text(encoding="utf-8")
        config_dst.write_text(fill(header, code, name) + body, encoding="utf-8")
        print(f"  wrote {config_dst.relative_to(CONTENT)}")

    for filename in ("SYNTAX.md", "GLOSSARY.md"):
        tpl_path = TEMPLATES / filename
        dst = loc_dir / filename
        if tpl_path.exists() and (force_config or not dst.exists()):
            dst.write_text(
                fill(tpl_path.read_text(encoding="utf-8"), code, name),
                encoding="utf-8",
            )
            print(f"  wrote {dst.relative_to(CONTENT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--locale",
        action="append",
        metavar="CODE",
        help="Locale code (repeatable). Default: all locales.",
    )
    parser.add_argument(
        "--force-config",
        action="store_true",
        help="Overwrite existing config.yaml in locale dirs",
    )
    args = parser.parse_args()

    wanted = {code: name for code, name in LOCALES}
    if args.locale:
        missing = [c for c in args.locale if c not in wanted]
        if missing:
            raise SystemExit(f"Unknown locale(s): {', '.join(missing)}")
        pairs = [(c, wanted[c]) for c in args.locale]
    else:
        pairs = LOCALES

    for code, name in pairs:
        print(code)
        bootstrap_locale(code, name, args.force_config)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
