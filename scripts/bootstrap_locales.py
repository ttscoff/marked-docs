#!/usr/bin/env python3
"""Create or refresh HelpDocs locale scaffolding.

Usage:
  python3 HelpDocs/content/scripts/bootstrap_locales.py es
  python3 HelpDocs/content/scripts/bootstrap_locales.py es fr nl
  python3 HelpDocs/content/scripts/bootstrap_locales.py --all-known
  python3 HelpDocs/content/scripts/bootstrap_locales.py es --force
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from help_l10n_common import (  # noqa: E402
    CONTENT_ROOT,
    LOCALE_LABELS,
    REPO_ROOT,
    locale_dir,
)

TEMPLATES = CONTENT_ROOT / "_templates"
CONFIG_HEADER = """# {locale_label} ({locale}) — localized help index
# Copied from English master on {today}.
# Translate: Title, MetaDescriptions, section title/folder, page title/sidebar_title,
# description, keywords, and wiki_keywords.
# Do NOT change page file: keys (English basenames) or build settings below.
#
"""


def render_template(path: Path, locale: str, locale_label: str) -> str:
    text = path.read_text(encoding="utf-8")
    return (
        text.replace("{LOCALE}", locale)
        .replace("{LOCALE_LABEL}", locale_label)
    )


def template_path(locale: str, name: str) -> Path:
    localized = TEMPLATES / "locales" / locale / name
    if localized.is_file():
        return localized
    return TEMPLATES / name


def write_if_missing(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def bootstrap_locale(locale: str, force: bool = False) -> list[str]:
    if locale not in LOCALE_LABELS:
        raise SystemExit(f"Unknown locale {locale!r}. Known: {', '.join(sorted(LOCALE_LABELS))}")

    locale_label = LOCALE_LABELS[locale]
    target = locale_dir(locale)
    created: list[str] = []

    target.mkdir(parents=True, exist_ok=True)

    for name in ("SYNTAX.md", "GLOSSARY.md", "APPMENU.md"):
        src = template_path(locale, name)
        if not src.is_file():
            continue
        dest = target / name
        content = render_template(src, locale, locale_label) if "{LOCALE" in src.read_text(encoding="utf-8") else src.read_text(encoding="utf-8")
        if write_if_missing(dest, content, force):
            created.append(str(dest.relative_to(CONTENT_ROOT)))

    config_dest = target / "config.yaml"
    if force or not config_dest.exists():
        header = CONFIG_HEADER.format(
            locale=locale,
            locale_label=locale_label,
            today=date.today().isoformat(),
        )
        english_config = (CONTENT_ROOT / "config.yaml").read_text(encoding="utf-8")
        config_dest.write_text(header + english_config, encoding="utf-8")
        created.append(str(config_dest.relative_to(CONTENT_ROOT)))

    ui_strings_dir = CONTENT_ROOT / "ui-strings"
    ui_strings_dir.mkdir(parents=True, exist_ok=True)
    ui_dest = ui_strings_dir / f"{locale}-ui-review.marked-l10n"
    if force or not ui_dest.exists():
        handoff_script = REPO_ROOT / "scripts" / "generate_locale_review_handoff.py"
        if handoff_script.is_file():
            subprocess.run(
                [
                    sys.executable,
                    str(handoff_script),
                    locale,
                    "--output",
                    str(ui_dest),
                ],
                check=True,
                cwd=str(REPO_ROOT),
            )
            created.append(str(ui_dest.relative_to(CONTENT_ROOT)))

    help_handoff_script = SCRIPT_DIR / "generate_help_review_handoff.py"
    help_dest = target / "REVIEW_HANDOFF.md"
    if help_handoff_script.is_file() and (force or not help_dest.exists()):
        subprocess.run(
            [sys.executable, str(help_handoff_script), locale],
            check=True,
            cwd=str(REPO_ROOT),
        )
        created.append(str(help_dest.relative_to(CONTENT_ROOT)))

    images_dir = target / "images"
    if not images_dir.exists():
        images_dir.mkdir(parents=True, exist_ok=True)
        gitkeep = images_dir / ".gitkeep"
        gitkeep.write_text("", encoding="utf-8")
        created.append(str(gitkeep.relative_to(CONTENT_ROOT)))

    return created


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Bootstrap HelpDocs locale scaffolding.")
    parser.add_argument("locales", nargs="*", help="Locale codes (e.g. es de fr)")
    parser.add_argument(
        "--all-known",
        action="store_true",
        help="Bootstrap every locale in LOCALE_LABELS",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    locales = list(LOCALE_LABELS) if args.all_known else args.locales
    if not locales:
        print("Provide locale code(s) or --all-known", file=sys.stderr)
        return 1

    for locale in locales:
        created = bootstrap_locale(locale, force=args.force)
        print(f"{locale}: {len(created)} file(s) written")
        for path in created:
            print(f"  + {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
