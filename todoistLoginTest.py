import pytest
from playwright.sync_api import Page

from steps.Given import Given
from steps.When import When
from steps.Then import Then


@pytest.fixture
def given(page: Page):
  return Given(page)

@pytest.fixture
def when(page: Page):
  return When(page)

@pytest.fixture
def then(page: Page):
  return Then(page)


def test_userCanLogIn(given: Given, when: When, then: Then):
  given.userOpensLoginPage()
  when.userEntersCorrectCredentials()
  then.userChecksIfIsLoggedIn()


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

# def test_checkProjectListExample(login: LoginForm, todoist: TodoistApp, page: Page):
  # todoist.navigateToLoginPage()
  # login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  # login.enterPassword('ti4FCvBL39i7mMq')
  # login.submitForm()
  # page.wait_for_selector('#projects_list')
  # expect().to_have_text(['1', '2', '3'])
  # items = ['1', '2', '4', '3']
  # assert set(['1', '2', '5']).issubset(items) 
