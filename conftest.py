import pytest
from playwright.sync_api import Page
from pageobjects.Filters import Filters
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMvc import TodoMvc
from pageobjects.TodosList import TodosList
from steps.Given import Given
from steps.Then import Then
from steps.When import When


@pytest.fixture
def newTodoInput(page: Page):
    return NewTodoInput(page)

@pytest.fixture
def todosList(page: Page):
    return TodosList(page)

@pytest.fixture
def app(page: Page):
    return TodoMvc(page)

@pytest.fixture
def filters(page: Page):
    return Filters(page)

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
def pageObjects(newTodoInput, todosList, app, filters):
    return {
        "newTodoInput": newTodoInput,
        "todosList": todosList,
        "app": app,
        "filters": filters
    }