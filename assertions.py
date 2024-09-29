from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Verify element visibility, text content, and attributes
    page.goto("https://example.com")
    assert page.is_visible("selector-for-element")
    assert page.text_content("selector-for-element") == "Expected text"
    assert page.get_attribute("selector-for-element", "attribute-name") == "expected-value"

    # Check for element states
    page.goto("https://example.com/form")
    assert page.is_enabled("selector-for-element")
    assert page.is_checked("selector-for-checkbox")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)