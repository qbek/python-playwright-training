from playwright.sync_api import Page

NEW_TODO_INPUT = '#new-todo'

class NewTodoInput:

    def __init__ (self, page: Page):
        self.page = page

    def enter_todo_name(self, name): 
        self.page.locator(NEW_TODO_INPUT).fill(name)

    def submit_todo(self):
        self.page.keyboard.press('Enter')
