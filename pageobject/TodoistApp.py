class TodoistApp:

  def __init__(self, page):
    self._page = page

  def navigateToLoginPage(self):
    self._page.goto('https://app.todoist.com/auth/login')
  
  def getAllCookies(self):
    self._page.wait_for_url('https://app.todoist.com/app/')
    return self._page.context.cookies()