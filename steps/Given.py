from playwright.sync_api import APIRequestContext
from data.TestData import TestData
from pageobject.TodoistApp import TodoistApp
from steps.When import When
from steps.Then import Then


class Given:
  def __init__(self, page, request_context: APIRequestContext, test_data: TestData):
    self._todoist = TodoistApp(page)
    self._actions = When(page, test_data)
    self._checks = Then(page, test_data)
    self._request_context = request_context
    self._test_data = test_data


  def userOpensLoginPage(self):
    self._todoist.navigateToLoginPage()

  def userIsLoggedIn(self):
    # self.userOpensLoginPage()
    # self._actions.userEntersCorrectCredentials()
    # self._checks.userChecksIfIsLoggedIn()
    self._todoist.navigateToMainPage()

  def userHasProjectCreated(self):
    self._test_data.defineProjectName("Projek z resta")
    self.userIsLoggedIn()
    # self._actions.userCreatesNewProject(projectName)
    response = self._request_context.post(url='/rest/v2/projects', data={"name": self._test_data.getProjectName()})
    body = response.json()
    self._todoist.navigateTo(body["url"])
    


