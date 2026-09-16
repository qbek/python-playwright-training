import pytest
from playwright.sync_api import Page

from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoFilters import TodoFilters
from pageobjects.TodoMVCApp import TodoMVCApp
from pageobjects.TodosList import TodosList
from faker import Faker

from steps.Given import Given
from steps.Then import Then
from steps.When import When


@pytest.fixture
def newTodoInput(page: Page):
    return NewTodoInput(page)

@pytest.fixture
def todoMvc(page: Page):
    return TodoMVCApp(page)

@pytest.fixture
def given(page: Page):
    return Given(page)

@pytest.fixture
def when(page: Page):
    return When(page)

@pytest.fixture
def then(page: Page):
    return Then(page)

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