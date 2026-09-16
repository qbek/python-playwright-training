import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodosList import TodosList
from pageobjects.TodoMVCApp import TodoMVCApp


def test_userCanCreateATodo(given, when, then, todoName):
    given.todoMvc_app_is_opened()
    when.create_todo(todoName)
    then.check_todo_created(todoName)
