"""Optional browser regression checks for the original synthetic RTL demo."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", help="Installed browser channel, e.g. msedge or chrome")
    parser.add_argument("--output", type=Path, help="Optional JSON/screenshots directory")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    records = []
    with sync_playwright() as runtime:
        browser = runtime.chromium.launch(headless=True, **({"channel": args.channel} if args.channel else {}))
        try:
            for width in (390, 1024):
                page = browser.new_page(viewport={"width": width, "height": 844})
                page.goto((root / "examples/rtl/before.html").as_uri())
                assert page.locator("html").get_attribute("dir") is None
                assert page.locator("input").get_attribute("id") is None
                if args.output:
                    args.output.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(args.output / f"before-{width}.png"), full_page=True)
                page.goto((root / "examples/rtl/after.html").as_uri())
                assert page.locator("html").get_attribute("lang") == "fa"
                assert page.locator("html").get_attribute("dir") == "rtl"
                assert page.locator("bdi").inner_text() == "AB-123/45"
                assert page.locator("bdi").evaluate("(el) => getComputedStyle(el).direction") == "ltr"
                phone = page.get_by_label("شمارهٔ تماس", exact=True)
                assert phone.count() == 1
                page.keyboard.press("Tab")
                assert phone.evaluate("(el) => el === document.activeElement")
                page.keyboard.press("Tab")
                assert page.get_by_role("button", name="بررسی درخواست").evaluate("(el) => el === document.activeElement")
                page.locator("label").click()
                assert phone.evaluate("(el) => el === document.activeElement")
                value = "+98 912 000 0000"
                phone.fill(value)
                assert phone.input_value() == value
                phone.press("ControlOrMeta+A")
                selected = phone.evaluate("(el) => el.value.slice(el.selectionStart, el.selectionEnd)")
                assert selected == value
                phone.fill("09120000000")
                assert phone.input_value() == "09120000000"
                assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
                if args.output:
                    page.screenshot(path=str(args.output / f"after-{width}.png"), full_page=True)
                records.append({
                    "width": width, "status": "pass",
                    "checks": ["before defects present", "semantic language/direction", "identifier text and direction",
                               "accessible label lookup", "label click focuses input", "input then button tab order",
                               "phone entry and selection", "leading zero preserved", "no horizontal page overflow"],
                    "unverified": ["OS clipboard", "screen reader", "native mobile keyboard", "backend submission"]
                })
                page.close()
            report = {"browser": browser.version, "channel": args.channel or "bundled chromium",
                      "headless": True, "fixture": "synthetic RTL demo", "records": records}
            if args.output:
                (args.output / "browser-results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(report, ensure_ascii=False, indent=2))
        finally:
            browser.close()


if __name__ == "__main__":
    main()
