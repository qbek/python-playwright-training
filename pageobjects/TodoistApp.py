from playwright.sync_api import Page


class TodoistApp:
  def __init__(self, page: Page):
    self._page = page

  def gotoLoginPage(self):
    self._page.goto('https://app.todoist.com/auth/login')

  def waitForMainView(self):
    self._page.wait_for_url('https://app.todoist.com/app/today')
    

  def getCookies(self):
    return self._page.context.cookies()