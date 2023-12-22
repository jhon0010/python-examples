from playwright.async_api import Page
import pytest


@pytest.mark.skip_browser("chromium")
def test_title_is_google(page: Page):
    page.goto("https://google.com")
    assert page.title() == "Google"

@pytest.mark.only_browser("chromium")    
def test_sauce_demo_inventory_site(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    #page.fill("#user-name", "standard_user")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."