from pageobject.TodoistApp import TodoistApp
from steps.When import When
from steps.Then import Then


class Given:
  def __init__(self, page):
    self._todoist = TodoistApp(page)
    self._actions = When(page)
    self._checks = Then(page)


  def userOpensLoginPage(self):
    self._todoist.navigateToLoginPage()

  def userIsLoggedIn(self):
    self.userOpensLoginPage()
    self._actions.userEntersCorrectCredentials()
    self._checks.userChecksIfIsLoggedIn()

  def userHasProjectCreated(self, projectName):
    self.userIsLoggedIn()
    self._actions.userCreatesNewProject(projectName)



