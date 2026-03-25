from playwright.sync_api import Page


_ADD_PROJECT_LABEL = '[aria-label="Add project"]'


class NewProjectPopUp:
    def __init__(self, page: Page):
      self._page = page

    def clickAddNewProject(self):
       self._page.locator(_ADD_PROJECT_LABEL).click()