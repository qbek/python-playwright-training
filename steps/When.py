
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoFilters import TodoFilters
from pageobjects.TodosList import TodosList


class When:
    def __init__(self, page):
        self.newTodoInput = NewTodoInput(page)
        self.todosList = TodosList(page)
        self.todoFilters = TodoFilters(page)

    def create_todo(self, name):
        self.newTodoInput.enter_todo_name(name)
        self.newTodoInput.submit_todo()

    def complete_todo(self):
        self.todosList.complete_todo()

    def goto_active_todos(self):
        self.todoFilters.goto_active_filter()