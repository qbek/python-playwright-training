from playwright.sync_api import Page, expect

from pageobjects.LeftSidebar import LeftSidebar
from pageobjects.TodoistApp import TodoistApp



class Then:

  def __init__(self, page:Page):
    self._todoistApp = TodoistApp(page)
    self._leftSidebar = LeftSidebar(page)
    
  def checkIfLoggedIn(self):
    self._todoistApp.waitForMainView()
    cookies = self._todoistApp.getCookies()
    assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"There is no expected 'todistd' cookie in: {cookies}"
    self._todoistApp.saveSession()

  def checkIfProjectIsCreated(self, projectName):
     # 1
    expect(self._leftSidebar.getProjectsListEl()).to_contain_text(projectName)
    # expect(page.locator('#projects_list')).to_contain_text('Moj projekt')
    # print(page.locator('#projects_list').inner_text())

    # 2 sprawdzenie czy projek jest w liscie
    projects = self._leftSidebar.getProjectsNames()
    # projects = page.locator('[data-testid="project-list-item"]').all_text_contents()
    assert projectName in projects

    # 3 sprawdzenie czy nowy projekt jest ostatni
    assert projectName == projects.pop()

