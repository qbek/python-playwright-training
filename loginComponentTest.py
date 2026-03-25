import pytest
import time
from playwright.sync_api import Page, Route
from pageobjects.LoginForm import LoginForm
from pageobjects.TodoistApp import TodoistApp


def test_loginNegativeCase(page: Page):
  app = TodoistApp(page)
  login = LoginForm(page)

  page.route('**/api/v1/user/login', failedReponse)

  app.gotoLoginPage()
  login.enterLogin('gbinxeqerpnywwysux@awdrt.org')
  login.enterPass('ti4FCvBL39i7mMq')
  login.submitForm()

  time.sleep(10)

def test_loginNegativeCase2(page: Page):
  app = TodoistApp(page)
  login = LoginForm(page)

  page.route('**/api/v1/user/login', failedReponse2)

  app.gotoLoginPage()
  login.enterLogin('gbinxeqerpnywwysux@awdrt.org')
  login.enterPass('ti4FCvBL39i7mMq')
  login.submitForm()

  time.sleep(10)


def failedReponse(route: Route):
  data = {
    "error": "Wrong email or password",
    "error_code": 9,
    "error_extra": {
        "event_id": "8da8e224d6e44c6d9125091647742ada",
        "retry_after": 3
    },
    "error_tag": "AUTHENTICATION_ERROR",
    "http_code": 401
  }
  route.fulfill(status=401, json=data)


def failedReponse2(route: Route):
  data = {
    "error_desc": "Dzikie węże",
   
    
    "error_tag": "ERROR",
    "http_code": 414
  }
  route.fulfill(status=503, json=data)