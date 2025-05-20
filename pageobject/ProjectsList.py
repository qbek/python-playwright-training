from playwright.sync_api import Page

class ProjectsList:
  def __init__(self, page: Page):
    self._page = page

  def clickMyProjectsMenu(self):
    self._page.locator('[aria-label="My projects menu"]').click()

  def getExistingProjects(self):
    return self._page.locator('#projects_list').inner_text()
  
  def getLastProjectName(self):
    return self._page.locator('[data-testid="project-list-item"]').inner_text()