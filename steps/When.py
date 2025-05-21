from data.TestData import TestData
from pageobject.LoginForm import LoginForm
from pageobject.NewProjectForm import NewProjectForm
from pageobject.ProjectView import ProjectView
from pageobject.ProjectsList import ProjectsList
from pageobject.ProjectsMenu import ProjectsMenu
from pageobject.TaskEditorForm import TaskEditorForm


class When:
  def __init__(self, page, test_data: TestData):
    self._login = LoginForm(page)
    self._projects = ProjectsList(page)
    self._projectsMenu = ProjectsMenu(page)
    self._newProjectForm = NewProjectForm(page)
    self._projectView = ProjectView(page)
    self._taskEditorForm = TaskEditorForm(page)
    self._test_data = test_data

  def userEntersCorrectCredentials(self):
    self._login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
    self._login.enterPassword('ti4FCvBL39i7mMq')
    self._login.submitForm()

  def userCreatesNewProject(self):
    self._test_data.defineProjectName("Projekt testowy")
    self._projects.clickMyProjectsMenu()
    self._projectsMenu.clickAddProject()
    self._newProjectForm.enterProjectName(self._test_data.getProjectName())
    self._newProjectForm.submitForm()

  def userAddTaskToTheProject(self):
    self._test_data.defineTaskName("testowe zadanie")
    self._projectView.clickAddTaskButton()
    self._taskEditorForm.enterTaskName(self._test_data.getTaskName())
    self._taskEditorForm.submitForm()
