class NewProjectForm:
  def __init__(self, page):
    self._page = page
  
  def enterProjectName(self, name):
    self._page.locator('[data-testid="modal-overlay"] input[name="name"]').fill(name)

  def submitForm(self):
    self._page.locator('[data-testid="modal-overlay"] [type="submit"]').click()