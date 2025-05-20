from pageobject.TodoistApp import TodoistApp


class Then:
  def __init__(self, page):
    self._todoist = TodoistApp(page)

  def userChecksIfIsLoggedIn(self):
    cookies = self._todoist.getAllCookies()
    assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"Expected cookie todoistd dosn't exists in: {cookies}"