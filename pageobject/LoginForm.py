from playwright.sync_api import Page

_EMAIL_INPUT = '#element-0'
_PASSWORD_INPUT = '#element-2'
_LOGIN_BUTTON = '[type="submit"]'

class LoginForm:

  def __init__(self, page: Page):
    self._page = page

  def enterEmail(self, mail):
    self._page.locator(_EMAIL_INPUT).fill(mail)

  def enterPassword(self, password):
    self._page.locator(_PASSWORD_INPUT).fill(password)

  def submitForm(self):
    self._page.locator(_LOGIN_BUTTON).click()



  
  
  