from playwright.sync_api import Page
from confenv import TODOMVC_URL


class TodoMvc:

    def __init__(self, page:Page):
        self._page = page

    def openApp(self):
        self._page.goto(TODOMVC_URL)