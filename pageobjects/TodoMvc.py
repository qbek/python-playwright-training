from playwright.sync_api import Page

TODOMVC_URL = 'https://todomvc.com/examples/jquery/dist/#/all'

class TodoMvc:

    def __init__(self, page:Page):
        self._page = page

    def openApp(self):
        self._page.goto(TODOMVC_URL)