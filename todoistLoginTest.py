import time
import pytest
from playwright.sync_api import Page, Playwright, Route

from steps.Given import Given
from steps.When import When
from steps.Then import Then


@pytest.fixture
def given(page: Page, playwright: Playwright):
  headers = {
        "Accept": "application/json",
        "Authorization": "Bearer d469ce54eca3a7ca5b6b5e7d4c8d51ced8d4c7b1",
    }
  request_context = playwright.request.new_context(
      base_url="https://api.todoist.com", extra_http_headers=headers
  )
  yield Given(page, request_context)
  request_context.dispose()

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

def test_userCannotLogIn(given: Given, when: When, page: Page):
  page.route('**/api/v9.223/user/login', invalidEmailResponse)
  given.userOpensLoginPage()
  when.userEntersCorrectCredentials()
  time.sleep(5)

def invalidEmailResponse(route: Route):
  data = {
              "error": "Email is invalid",
              "error_code": 8,
              "error_extra": {
                  "argument": "email",
                  "event_id": "bb850f92a51e4750957a24fa31cd8c04",
                  "expected": "email",
                  "retry_after": 5
              },
              "error_tag": "INVALID_EMAIL",
              "http_code": 400
          }
  route.fulfill(status=500, json=data)


# def test_checkProjectListExample(login: LoginForm, todoist: TodoistApp, page: Page):
  # todoist.navigateToLoginPage()
  # login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  # login.enterPassword('ti4FCvBL39i7mMq')
  # login.submitForm()
  # page.wait_for_selector('#projects_list')
  # expect().to_have_text(['1', '2', '3'])
  # items = ['1', '2', '4', '3']
  # assert set(['1', '2', '5']).issubset(items) 


