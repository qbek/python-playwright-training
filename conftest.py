import pytest
from playwright.sync_api import Page

from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoFilters import TodoFilters
from pageobjects.TodoMVCApp import TodoMVCApp
from pageobjects.TodosList import TodosList
from faker import Faker


@pytest.fixture
def newTodoInput(page: Page):
    return NewTodoInput(page)

@pytest.fixture
def todoMvc(page: Page):
    return TodoMVCApp(page)

@pytest.fixture
def todosList(page: Page):
    return TodosList(page)

@pytest.fixture
def todoFilters(page: Page):
    return TodoFilters(page)


@pytest.fixture
def todoName():
    faker = Faker()
    return faker.name()