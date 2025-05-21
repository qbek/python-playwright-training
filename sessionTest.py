import time
from playwright.sync_api import Playwright, Page


def test_loadSessionOption1(playwright: Playwright):
  chrome = playwright.firefox
  browser = chrome.launch(headless=False)
  context = browser.new_context(storage_state='session.json')
  page = context.new_page()
  page.goto('https://app.todoist.com/app')
  time.sleep(5)
  page.close()

def test_loadSessionWithPage(page: Page):
  new_context = page.context.browser.new_context(storage_state='session.json')
  page.close()
  page_with_session = new_context.new_page()
  page_with_session.goto('https://app.todoist.com/app')
  time.sleep(10)