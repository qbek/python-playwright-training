from playwright.sync_api import Page

_LOGIN_PAGE_URL = 'https://app.todoist.com/auth/login'
_MAIN_APP_URL = 'https://app.todoist.com/app/'


class TodoistApp:

  def __init__(self, page: Page):
    self._page = page

  def navigateToLoginPage(self):
    self._page.goto(_LOGIN_PAGE_URL)

  def getAllCookies(self):
    self._page.wait_for_url(_MAIN_APP_URL)
    return self._page.context.cookies()

  def navigateTo(self, url):
    self._page.goto(url)

  def saveSession(self):
    self._page.context.storage_state(path='session.json')