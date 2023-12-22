import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        
        # Create a new incognito browser context allows us to have multiple browser contexts.
        context = await browser.new_context()
        
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        page = await browser.new_page()
        await page.goto("https://demoqa.com/checkbox")        
        
        # actions 
        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path="checkboxes.png")
        
        #assertions
        await page.is_checked('label[for="tree-node-home"]') is True
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
        
        await context.tracing.stop(path="trace.zip")        
        
        # Close the browser
        await browser.close()
        
asyncio.run(main())