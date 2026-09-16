from playwright.sync_api import Page


TODOMVC_URL = 'https://todomvc.com/examples/jquery/dist/#/all'

class TodoMVCApp:

    def __init__(self, page: Page):
        self.page = page

    def open_main_view(self):
        self.page.goto(TODOMVC_URL)