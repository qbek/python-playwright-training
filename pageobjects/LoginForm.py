from playwright.sync_api import Page

_EMAIL_INPUT = '#element-0'
_PASS_INPUT = '#element-2'
_SUBMIT_BUTTON = '[type="submit"]'


class LoginForm:
  def __init__(self, page: Page):
    self._page = page
   

  def enterLogin(self, login):
    self._page.locator(_EMAIL_INPUT).fill(login)
    
  def enterPass(self, password):
    self._page.locator(_PASS_INPUT).fill(password)

  def submitForm(self):
    self._page.locator(_SUBMIT_BUTTON).click()