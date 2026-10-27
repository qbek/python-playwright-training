import pytest
from playwright.sync_api import Page, expect

TODOMVC_URL = 'https://todomvc.com/examples/jquery/dist/#/all'

NEW_TODO_INPUT = '#new-todo'
TODO_LABEL = '#todo-list label'

TODO = '#todo-list li'
TODO_COMPLETE_TOGGLE = '.toggle'
TODOS_LIST = '#todo-list'
ACTIVE_FILTER = '[href="#/active"]'
COMPLETED_FILTER = '[href="#/completed"]'

def test_userCanCreateATodo(page: Page):
    page.goto(TODOMVC_URL)

    todoName = 'Moje todo zmienie tylko raz'
    
    page.locator(NEW_TODO_INPUT).fill(todoName)
    page.keyboard.press('Enter')
    expect(page.locator(TODO_LABEL)).to_have_text(todoName)

def test_userCanCompleteATodo(page: Page):
    page.goto(TODOMVC_URL)

    todoName = 'Wykonane zadanie'
    page.locator(NEW_TODO_INPUT).fill(todoName)
    page.keyboard.press('Enter')

    page.locator(TODO_COMPLETE_TOGGLE).check()
    expect(page.locator(TODO)).to_have_attribute('class', ' completed')

    page.locator(ACTIVE_FILTER).click()
    expect(page.locator(TODOS_LIST)).to_be_empty()

    page.locator(COMPLETED_FILTER).click()
    expect(page.locator(TODO_LABEL)).to_have_text(todoName)

