_LOGIN_PAGE_URL = 'https://app.todoist.com/auth/login'
_MAIN_APP_URL = 'https://app.todoist.com/app/'


class TodoistApp:

  def __init__(self, page):
    self._page = page

  def navigateToLoginPage(self):
    self._page.goto(_LOGIN_PAGE_URL)

  def getAllCookies(self):
    self._page.wait_for_url(_MAIN_APP_URL)
    return self._page.context.cookies()