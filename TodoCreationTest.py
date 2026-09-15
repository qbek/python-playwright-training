import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect

def test_userCanCreateATodo(page: Page):
    page.goto('https://todomvc.com/examples/jquery/dist/#/all')

    page.locator('#new-todo').fill('To jest moje zadanie')
    page.keyboard.press('Enter')

    expect(page.locator('#todo-list label')).to_have_text('To jest moje zadanie')