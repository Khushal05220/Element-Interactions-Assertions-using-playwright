from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    
    # Capture screenshots
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="screenshot.png")
    page.locator("selector-for-element").screenshot(path="element_screenshot.png")

    # Record videos
    context = browser.new_context(record_video_dir="videos/", record_video_size={"width": 1280, "height": 720})
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True)
    page.goto("https://example.com")
    page.click("selector-for-button")
    context.tracing.stop(path="trace.zip")
    
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)