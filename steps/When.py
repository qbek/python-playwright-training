from playwright.sync_api import Page

from pageobjects.Filters import Filters
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodosList import TodosList


class When:
    def __init__(self, page: Page):
        self._newTodoInput = NewTodoInput(page)
        self._todosList = TodosList(page) 
        self._filters = Filters(page)

    def userCreatesATodo(self, todoName):
        self._newTodoInput.enter_todo_name(todoName)
        self._newTodoInput.submit_todo()

    def userDeletesATodo(self):
        self._todosList.hover_over_todo()
        self._todosList.delete_todo()

    def userCompletesTodo(self):
        self._todosList.check_complete_toggle()


    def userSelectsActiveFilter(self):
        self._filters.goto_active()

    def userSelectsCompletedFilter(self):
            self._filters.goto_completed()