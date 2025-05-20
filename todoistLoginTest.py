import pytest
from pageobject.LoginForm import LoginForm
from pageobject.TodoistApp import TodoistApp

from playwright.sync_api import Page, expect, Playwright

@pytest.fixture
def login(page: Page):
  return LoginForm(page)

@pytest.fixture
def todoist(page: Page):
  return TodoistApp(page)


def test_userCanLogIn(login, todoist):
  #Given
  todoist.navigateToLoginPage()

  #When
  login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  login.enterPassword('ti4FCvBL39i7mMq')
  login.submitForm()

  #Then
  cookies = todoist.getAllCookies()
  assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"Expected cookie todoistd dosn't exists in: {cookies}"


