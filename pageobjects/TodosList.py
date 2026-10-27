from playwright.sync_api import Page, expect

TODO_LABEL = '#todo-list label'

TODO = '#todo-list li'
TODO_COMPLETE_TOGGLE = '.toggle'
TODOS_LIST = '#todo-list'

class TodosList:

    def __init__(self, page: Page):
        self._page = page

    def check_todo_displayed(self, name):
        expect(self._page.locator(TODO_LABEL)).to_have_text(name)

    def check_complete_toggle(self):
        self._page.locator(TODO_COMPLETE_TOGGLE).check()

    def check_todo_marked_as_completed(self):
        expect(self._page.locator(TODO)).to_have_attribute('class', ' completed')

    def check_list_empty(self):
        expect(self._page.locator(TODOS_LIST)).to_be_empty()