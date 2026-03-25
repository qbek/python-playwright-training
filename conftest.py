import pytest
from playwright.sync_api import Page

from steps.Given import Given
from steps.Then import Then
from steps.When import When


@pytest.fixture
def sessionPage(page: Page):
  # sessionPage = page.context.browser.new_context(storage_state='session.json').new_page()
  # page.close()
  return page


@pytest.fixture
def given(sessionPage):
  return Given(sessionPage)

@pytest.fixture
def when(sessionPage):
  return When(sessionPage)

@pytest.fixture
def then(sessionPage):
  return Then(sessionPage)
