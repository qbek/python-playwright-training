from pageobject.LoginForm import LoginForm
from pageobject.NewProjectForm import NewProjectForm
from pageobject.ProjectView import ProjectView
from pageobject.ProjectsList import ProjectsList
from pageobject.ProjectsMenu import ProjectsMenu
from pageobject.TaskEditorForm import TaskEditorForm


class When:
  def __init__(self, page):
    self._login = LoginForm(page)
    self._projects = ProjectsList(page)
    self._projectsMenu = ProjectsMenu(page)
    self._newProjectForm = NewProjectForm(page)
    self._projectView = ProjectView(page)
    self._taskEditorForm = TaskEditorForm(page)

  def userEntersCorrectCredentials(self):
    self._login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
    self._login.enterPassword('ti4FCvBL39i7mMq')
    self._login.submitForm()

  def userCreatesNewProject(self, projectName):
    self._projects.clickMyProjectsMenu()
    self._projectsMenu.clickAddProject()
    self._newProjectForm.enterProjectName(projectName)
    self._newProjectForm.submitForm()

  def userAddTaskToTheProject(self, taskName):
    self._projectView.clickAddTaskButton()
    self._taskEditorForm.enterTaskName(taskName)
    self._taskEditorForm.submitForm()
