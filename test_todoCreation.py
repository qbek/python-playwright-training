import pytest
from playwright.sync_api import Page, expect
from pageobjects.Filters import Filters
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


def test_userCanCompleteATodo(page: Page):
    app = TodoMvc(page)
    newTodoInput = NewTodoInput(page)
    todosList = TodosList(page)
    filters = Filters(page)
    
    app.openApp()

    todoName = 'Wykonane zadanie'
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()

    todosList.check_complete_toggle()
    todosList.check_todo_marked_as_completed()

    filters.goto_active()
    todosList.check_list_empty()    

    filters.goto_completed()
    todosList.check_todo_displayed(todoName)