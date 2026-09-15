import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect

TODOMVC_URL = 'https://todomvc.com/examples/jquery/dist/#/all'

NEW_TODO_INPUT = '#new-todo'
TODO_LABEL = '#todo-list label'


def test_userCanCreateATodo(page: Page):
    todoName = 'To jest moje lepsze zadanie'

    page.goto(TODOMVC_URL)

    page.locator(NEW_TODO_INPUT).fill(todoName)
    page.keyboard.press('Enter')

    expect(page.locator(TODO_LABEL)).to_have_text(todoName)