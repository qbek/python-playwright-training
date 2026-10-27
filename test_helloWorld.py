import pytest
from playwright.sync_api import Page

def test_helloWorldFromPlaywright(page: Page):
    page.goto("https://google.com")