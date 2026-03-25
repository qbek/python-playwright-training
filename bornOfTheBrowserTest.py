import pytest
import time
from playwright.sync_api import Page, Playwright


def test_vanilaBrowser(playwright: Playwright):
  browser = playwright.chromium
  browserRuntime = browser.launch(headless=False)
  
  # context = browserRuntime.new_context()
  # page = context.new_page()
  # page2 = context.new_page()
  # page.goto('https://www.google.com')
  # page2.goto('https://www.gazeta.pl')

  context = browserRuntime.new_context(storage_state='session.json')
  page = context.new_page()

  page.goto('https://app.todoist.com/app/')
  
  time.sleep(15)

def test_pageBrowser(page: Page):

  # page2 = page.context.new_page()

  # page.goto('https://www.google.com')
  # page2.goto('https://www.gazeta.pl')
  # page.locator()
  # page2.locator()

  sessionPage = page.context.browser.new_context(storage_state='session.json').new_page()
  page.close()
  sessionPage.goto('https://app.todoist.com/app/')


  time.sleep(15)