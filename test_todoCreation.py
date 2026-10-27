import pytest
from playwright.sync_api import Page, expect


def test_userCanCreateATodo(page: Page):
    page.goto('https://todomvc.com/examples/jquery/dist/#/all')

    page.locator('#new-todo').fill('Moje todo')
    page.keyboard.press('Enter')

    expect(page.locator('#todo-list label')).to_have_text('Moje todo')