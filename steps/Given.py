from playwright.sync_api import APIRequestContext
from pageobject.TodoistApp import TodoistApp
from steps.When import When
from steps.Then import Then


class Given:
  def __init__(self, page, request_context: APIRequestContext):
    self._todoist = TodoistApp(page)
    self._actions = When(page)
    self._checks = Then(page)
    self._request_context = request_context


  def userOpensLoginPage(self):
    self._todoist.navigateToLoginPage()

  def userIsLoggedIn(self):
    # self.userOpensLoginPage()
    # self._actions.userEntersCorrectCredentials()
    # self._checks.userChecksIfIsLoggedIn()
    self._todoist.navigateToMainPage()

  def userHasProjectCreated(self, projectName):
    self.userIsLoggedIn()
    # self._actions.userCreatesNewProject(projectName)
    response = self._request_context.post(url='/rest/v2/projects', data={"name": projectName})
    body = response.json()
    self._todoist.navigateTo(body["url"])
    


