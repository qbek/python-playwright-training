import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoFilters import TodoFilters
from pageobjects.TodosList import TodosList

TODOMVC_URL = 'https://todomvc.com/examples/jquery/dist/#/all'




def test_userCanCreateATodo(page: Page):
    todoName = 'To jest moje lepsze zadanie'
    newTodoInput = NewTodoInput(page)
    todosList = TodosList(page)

    page.goto(TODOMVC_URL)

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.check_todo_displayed(todoName)



def test_userCanFilterActiveTodos(page: Page):
    todoName = 'Zadanie do zakończenia'
    newTodoInput = NewTodoInput(page)
    todoFilters = TodoFilters(page)
    todosList = TodosList(page)

    page.goto(TODOMVC_URL)

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.complete_todo()
    todoFilters.goto_active_filter()
    todosList.check_todo_NOT_displayed()


def test_userCanFilterCompletedTodos(page: Page):
    todoName = 'Zadanie do zakończenia'
    newTodoInput = NewTodoInput(page)
    todoFilters = TodoFilters(page)
    todosList = TodosList(page)

    page.goto(TODOMVC_URL)

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.complete_todo()
    todoFilters.goto_completed_filter()
    todosList.check_todo_displayed(todoName)