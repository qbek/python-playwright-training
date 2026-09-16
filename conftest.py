import pytest
from playwright.sync_api import Page

from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMVCApp import TodoMVCApp
from pageobjects.TodosList import TodosList


@pytest.fixture
def newTodoInput(page: Page):
    return NewTodoInput(page)

@pytest.fixture
def todoMvc(page: Page):
    return TodoMVCApp(page)

@pytest.fixture
def todosList(page: Page):
    return TodosList(page)