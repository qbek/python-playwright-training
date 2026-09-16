from playwright.sync_api import Page

ACTIVE_TAB = '#filters [href="#/active"]'
COMPLETED_TAB = '#filters [href="#/completed"]'

class TodoFilters:

    def __init__(self, page: Page):
        self.page = page

    def goto_active_filter(self):
        self.page.locator(ACTIVE_TAB).click()

    def goto_completed_filter(self):
        self.page.locator(COMPLETED_TAB).click()