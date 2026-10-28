from playwright.sync_api import Page

from pageobjects.TodosList import TodosList

class Then:
    def __init__(self, page: Page):
        self._todosList = TodosList(page)

    def userChecksTodoIsDisplayed(self, todoName):
        self._todosList.check_todo_displayed(todoName)

    def userChecksTodosListEmpty(self):
        self._todosList.check_list_empty()

    def userChecksTodoMarkedAsCompleted(self):
        self._todosList.check_todo_marked_as_completed()