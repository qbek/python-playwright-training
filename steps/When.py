from pageobject.LoginForm import LoginForm


class When:
  def __init__(self, page):
    self._login = LoginForm(page)

  def userEntersCorrectCredentials(self):
     #User enters correct credentials
    self._login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
    self._login.enterPassword('ti4FCvBL39i7mMq')
    self._login.submitForm()