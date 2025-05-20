import pytest
from pageobject.NewProjectForm import NewProjectForm
from pageobject.ProjectsList import ProjectsList
from pageobject.LoginForm import LoginForm
from pageobject.ProjectsMenu import ProjectsMenu
from pageobject.TodoistApp import TodoistApp

from playwright.sync_api import Page, expect, Playwright

@pytest.fixture
def login(page: Page):
  return LoginForm(page)

@pytest.fixture
def todoist(page: Page):
  return TodoistApp(page)

@pytest.fixture
def projects(page: Page):
  return ProjectsList(page)

@pytest.fixture
def projectsMenu(page: Page):
  return ProjectsMenu(page)

@pytest.fixture
def newProjectForm(page: Page):
  return NewProjectForm(page)


def test_userCanLogIn(login, todoist):
  #Given
  todoist.navigateToLoginPage()

  #When
  login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  login.enterPassword('ti4FCvBL39i7mMq')
  login.submitForm()

  #Then
  cookies = todoist.getAllCookies()
  assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"Expected cookie todoistd dosn't exists in: {cookies}"

def test_userCanCreateProject(login: LoginForm, todoist: TodoistApp, projects: ProjectsList, projectsMenu: ProjectsMenu, newProjectForm: NewProjectForm):
  projectName = 'Moj testowy projekt'
  
  todoist.navigateToLoginPage()
  login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  login.enterPassword('ti4FCvBL39i7mMq')
  login.submitForm()

  projects.clickMyProjectsMenu()
  projectsMenu.clickAddProject()

  newProjectForm.enterProjectName(projectName)
  newProjectForm.submitForm()

  existingProjects = projects.getExistingProjects()
  print (existingProjects)
  assert existingProjects.pop() == projectName
  # assert projectName in existingProjects

  # Jezeli chcecie korzystac z asercji Playwright to z PO zwracajcie sobie element do sprawdzenia
  # allProjects = projects.getAllProjectItemEl()
  # expect(allProjects).to_contain_text(projectName)


# def test_checkProjectListExample(login: LoginForm, todoist: TodoistApp, page: Page):
  # todoist.navigateToLoginPage()
  # login.enterEmail('gbinxeqerpnywwysux@awdrt.org')
  # login.enterPassword('ti4FCvBL39i7mMq')
  # login.submitForm()
  # page.wait_for_selector('#projects_list')
  # expect().to_have_text(['1', '2', '3'])
  # items = ['1', '2', '4', '3']
  # assert set(['1', '2', '5']).issubset(items) 
