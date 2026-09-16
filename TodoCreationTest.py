import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodosList import TodosList
from pageobjects.TodoMVCApp import TodoMVCApp


def test_userCanCreateATodo(newTodoInput, todosList, todoMvc, todoName):
    todoMvc.open_main_view()
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.check_todo_displayed(todoName)
    