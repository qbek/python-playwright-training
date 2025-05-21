import pytest
from playwright.sync_api import Page, Playwright

from steps.Given import Given
from steps.When import When
from steps.Then import Then


@pytest.fixture
def session_page(page: Page):
  session_page = page.context.browser.new_context(storage_state='session.json').new_page()
  page.close()
  yield session_page
  session_page.close()


@pytest.fixture
def given(session_page: Page, playwright: Playwright):
  headers = {
        "Accept": "application/json",
        "Authorization": "Bearer d469ce54eca3a7ca5b6b5e7d4c8d51ced8d4c7b1",
    }
  request_context = playwright.request.new_context(
      base_url="https://api.todoist.com", extra_http_headers=headers
  )
  yield Given(session_page, request_context)
  request_context.dispose()

@pytest.fixture
def when(session_page: Page):
  return When(session_page)

@pytest.fixture
def then(session_page: Page):
  return Then(session_page)


def test_userCanCreateProject(given: Given, when: When, then: Then):
  projectName = 'Moj testowy projekt'
  given.userIsLoggedIn()
  when.userCreatesNewProject(projectName)
  then.userVerifiesCreatedProject(projectName)

def test_userCanAddTaskToTheProject(given: Given, when: When, then: Then):
  projectName = "Projekt na zadnie"
  taskName = "Moje zadanie"
  given.userHasProjectCreated(projectName)
  when.userAddTaskToTheProject(taskName)
  then.userChecksIfTaskIsCreated(taskName)