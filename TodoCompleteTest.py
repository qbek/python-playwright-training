import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect

TODOMVC_URL = 'https://todomvc.com/examples/jquery/dist/#/all'

NEW_TODO_INPUT = '#new-todo'
TODO_LABEL = '#todo-list label'
TODO_ITEM = '#todo-list li'

TODO_COMPLETE_TOGGLE = '.toggle'

ACTIVE_TAB = '#filters [href="#/active"]'
COMPLETED_TAB = '#filters [href="#/completed"]'

TODO_COMPLETED_MARK = ' completed'

def test_userCanCompleteTheTodo(page: Page):
    todoName = 'Zadanie do zakończenia'
    page.goto(TODOMVC_URL)

    page.locator(NEW_TODO_INPUT).fill(todoName)
    page.keyboard.press('Enter')

    page.locator(TODO_COMPLETE_TOGGLE).check()
    expect(page.locator(TODO_ITEM)).to_have_attribute('class', TODO_COMPLETED_MARK)