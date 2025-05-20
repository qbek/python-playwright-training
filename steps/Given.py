from pageobject.TodoistApp import TodoistApp


class Given:
  def __init__(self, page):
    self._todoist = TodoistApp(page)

  def userOpensLoginPage(self):
    #User opens login page
    self._todoist.navigateToLoginPage()
