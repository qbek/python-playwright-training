import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMVCApp import TodoMVCApp
from pageobjects.TodosList import TodosList


def test_userCanCompleteTheTodo(page: Page):
    todoName = 'Zadanie do zakończenia'
    todoMvc = TodoMVCApp(page)
    newTodoInput = NewTodoInput(page)
    todosList = TodosList(page)

    todoMvc.open_main_view()
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()

    todosList.complete_todo()
    todosList.check_todo_marked_completed()