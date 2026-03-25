from playwright.sync_api import Page

_PROJECT_NAME_INPUT = 'input:focus'
_SUBMIT_BUTTON = 'form [type="submit"]'


class ProjectEditForm:
    def __init__(self, page: Page):
      self._page = page

    def enterProjectName(self, name: str):
       self._page.locator(_PROJECT_NAME_INPUT).fill(name)

    def submit(self):
       self._page.locator(_SUBMIT_BUTTON).click()
