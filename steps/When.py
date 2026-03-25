from pageobjects.LeftSidebar import LeftSidebar
from pageobjects.LoginForm import LoginForm
from pageobjects.NewProjectPopUp import NewProjectPopUp
from pageobjects.ProjectEditForm import ProjectEditForm

class When:
  def __init__(self, page):
    self._loginForm = LoginForm(page)
    self._leftSidebar = LeftSidebar(page)
    self._newProjectPopUp = NewProjectPopUp(page)
    self._projectEditForm = ProjectEditForm(page)

  def loginWithCorrectCredentials(self):
    self._loginForm.enterLogin('gbinxeqerpnywwysux@awdrt.org')
    self._loginForm.enterPass('ti4FCvBL39i7mMq')
    self._loginForm.submitForm()

  def createNewProject(self, projectName):
    self._leftSidebar.clickAddProjectButton()
    self._newProjectPopUp.clickAddNewProject()
    
    self._projectEditForm.enterProjectName(projectName)
    self._projectEditForm.submit()
