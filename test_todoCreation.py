import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMvc import TodoMvc
from pageobjects.TodosList import TodosList


def test_userCanCreateATodo(page: Page):
    app = TodoMvc(page)
    newTodoInput = NewTodoInput(page)
    todosList = TodosList(page)

    app.openApp()
    todoName = 'Moje todo zmienie tylko raz'
    
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.check_todo_displayed(todoName)