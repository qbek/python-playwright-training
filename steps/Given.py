from playwright.sync_api import Page

from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMvc import TodoMvc
from steps.Then import Then
from steps.When import When


class Given:

    def __init__(self, page:Page):
        self._app = TodoMvc(page)
        self._when = When(page)
        self._then = Then(page)

    def userHasAppReady(self):
        self._app.openApp()

    def userHasTodo(self, todoName):
        self._when.userCreatesATodo(todoName)

    def userHasCompletedTodo(self, todoName):
        self._when.userCreatesATodo(todoName)
        self._when.userCompletesTodo()