import pytest
from playwright.sync_api import Page
from time import sleep

def test_helloWorld(page: Page):
    page.goto('https://google.com')
    sleep(5)

