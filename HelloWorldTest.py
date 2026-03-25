import pytest
from playwright.sync_api import Page

def test_helloWorld(page: Page):
     page.goto('https://google.com')


