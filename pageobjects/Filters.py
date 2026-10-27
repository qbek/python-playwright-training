from playwright.sync_api import Page

ACTIVE_FILTER = '[href="#/active"]'
COMPLETED_FILTER = '[href="#/completed"]'

class Filters:

    def __init__ (self, page: Page):
        self._page = page

    def goto_active(self):
        self._page.locator(ACTIVE_FILTER).click()

    def goto_completed(self):
        self._page.locator(COMPLETED_FILTER).click()