import pytest
from playwright.sync_api import Page, expect, Playwright



def test_userCanLogIn(page: Page):
  page.goto('https://app.todoist.com/auth/login')
  page.locator('#element-0').fill('gbinxeqerpnywwysux@awdrt.org')
  page.locator('#element-2').fill('ti4FCvBL39i7mMq')
  page.locator('[type="submit"]').click()
  page.wait_for_url('https://app.todoist.com/app/')
  cookies = page.context.cookies()
  assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"Expected cookie todoistd dosn't exists in: {cookies}"

  