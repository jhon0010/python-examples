import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

def sync () :
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://whatsmyuseragent.org/")
        page.screenshot(path="example.png")
        browser.close()
    
    
"""_summary_
Using async_playwright to launch a browser and take a screenshot of a webpage.
asyncio library to run the main function.
"""
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://whatsmyuseragent.org/")
        await page.screenshot(path="example.png")
        await browser.close()
        
asyncio.run(main())