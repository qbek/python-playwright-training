from pageobjects.TodosList import TodosList


class Then:

    def __init__(self, page):
        self.todosList = TodosList(page)

    def check_todo_created(self, name):
        self.todosList.check_todo_displayed(name)

    def check_todos_list_is_emtpy(self):
        self.todosList.check_todo_NOT_displayed()


    def check_todo_completed(self):
        self.todosList.check_todo_marked_completed()