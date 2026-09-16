import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoFilters import TodoFilters
from pageobjects.TodosList import TodosList
from pageobjects.TodoMVCApp import TodoMVCApp



def test_userCanFilterActiveTodos(page: Page):
    todoName = 'Zadanie do zakończenia'
    todoMvc = TodoMVCApp(page)
    newTodoInput = NewTodoInput(page)
    todoFilters = TodoFilters(page)
    todosList = TodosList(page)

    todoMvc.open_main_view()

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.complete_todo()
    todoFilters.goto_active_filter()
    todosList.check_todo_NOT_displayed()


def test_userCanFilterCompletedTodos(page: Page):
    todoName = 'Zadanie do zakończenia'
    todoMvc = TodoMVCApp(page)
    newTodoInput = NewTodoInput(page)
    todoFilters = TodoFilters(page)
    todosList = TodosList(page)

    todoMvc.open_main_view()

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.complete_todo()
    todoFilters.goto_completed_filter()
    todosList.check_todo_displayed(todoName)