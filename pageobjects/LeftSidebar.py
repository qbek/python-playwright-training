from playwright.sync_api import Page


_NEW_PROJECT_PLUS_BUTTON = '[aria-label="My projects menu"]'
_PROJECTS_LIST = '#projects_list'
_PROJECT_LIST_ITEM = '[data-testid="project-list-item"]'

class LeftSidebar:
  def __init__(self, page: Page):
    self._page = page

  def clickAddProjectButton(self):
    self._page.locator(_NEW_PROJECT_PLUS_BUTTON).click()

  def getProjectsNames(self):
    return self._page.locator(_PROJECT_LIST_ITEM).all_text_contents()
  
  def getProjectsListEl(self):
    return self._page.locator(_PROJECTS_LIST)