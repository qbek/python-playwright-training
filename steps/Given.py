from pageobjects.TodoMVCApp import TodoMVCApp
from steps.When import When


class Given:
    def __init__(self, page):
        self.todoMvcApp = TodoMVCApp(page)
        self.when = When(page)

    def todoMvc_app_is_opened(self):
        self.todoMvcApp.open_main_view()

    def completed_todo(self, name):
        self.when.create_todo(name)
        self.when.complete_todo()
