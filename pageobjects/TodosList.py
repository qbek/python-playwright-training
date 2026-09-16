from playwright.sync_api import Page, expect

TODO_LABEL = '#todo-list label'
TODO_ITEM = '#todo-list li'
TODO_COMPLETE_TOGGLE = '.toggle'
TODO_COMPLETED_MARK = ' completed'
TODO_DELETE = '.destroy'


class TodosList:

    def __init__(self, page: Page):
        self.page = page

    def check_todo_displayed(self, name):
        expect(self.page.locator(TODO_LABEL)).to_have_text(name)

    def check_todo_NOT_displayed(self):
        expect(self.page.locator(TODO_ITEM)).not_to_be_visible()

    def complete_todo(self):
        self.page.locator(TODO_COMPLETE_TOGGLE).check()

    def check_todo_marked_completed(self):
        expect(self.page.locator(TODO_ITEM)).to_have_attribute('class', ' completed')

    def hover_over_todo(self):
        self.page.locator(TODO_ITEM).click()

    def delete_todo(self):
        self.page.locator(TODO_DELETE).click()