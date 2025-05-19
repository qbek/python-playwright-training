import pytest
from playwright.sync_api import Page

def helloWorld(page: Page):
     page.goto('https://google.com')

