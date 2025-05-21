from pageobject.LoginForm import LoginForm
from pageobject.NewProjectForm import NewProjectForm
from pageobject.ProjectsList import ProjectsList
from pageobject.ProjectsMenu import ProjectsMenu


class When:
  def __init__(self, page):
    self._login = LoginForm(page)
    self._projects = ProjectsList(page)
    self._projectsMenu = ProjectsMenu(page)
    self._newProjectForm = NewProjectForm(page)

  def userEntersCorrectCredentials(self):
    self._login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
    self._login.enterPassword('ti4FCvBL39i7mMq')
    self._login.submitForm()

  def userCreatesNewProject(self, projectName):
    self._projects.clickMyProjectsMenu()
    self._projectsMenu.clickAddProject()

    self._newProjectForm.enterProjectName(projectName)
    self._newProjectForm.submitForm()