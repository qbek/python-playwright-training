class ProjectsMenu:
  def __init__(self, page):
    self._page = page

  def clickAddProject(self):
    self._page.locator('[aria-label="Add project"]').click()