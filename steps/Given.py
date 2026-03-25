from pageobjects.TodoistApp import TodoistApp
from steps.When import When


class Given:
  def __init__(self, page):
    self._todoistApp = TodoistApp(page)
    self._when = When(page)

  def todoistLogginIsOpened(self):
    self._todoistApp.gotoLoginPage()

  def userIsLoggedIn(self):
    self._todoistApp.gotoToMainView()
    self._todoistApp.waitForMainView()
     

