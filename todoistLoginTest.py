import pytest
from pageobject.LoginForm import LoginForm
from pageobject.TodoistApp import TodoistApp

from playwright.sync_api import Page, expect, Playwright

def test_userCanLogIn(page: Page):
  todoist = TodoistApp(page)
  login = LoginForm(page)
  todoist.navigateToLoginPage()

  login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  login.enterPassword('ti4FCvBL39i7mMq')
  login.submitForm()

  cookies = todoist.getAllCookies()
  assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"Expected cookie todoistd dosn't exists in: {cookies}"


