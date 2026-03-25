import pytest
from playwright.sync_api import Page, expect
from pageobjects.TodoistApp import TodoistApp
from pageobjects.LoginForm import LoginForm
from pageobjects.LeftSidebar import LeftSidebar
from pageobjects.NewProjectPopUp import NewProjectPopUp
from pageobjects.ProjectEditForm import ProjectEditForm


@pytest.fixture
def loginForm(page: Page):
  return LoginForm(page)

@pytest.fixture
def todoistApp(page: Page):
  return TodoistApp(page)

@pytest.fixture
def leftSidebar(page: Page):
  return LeftSidebar(page)


@pytest.fixture
def newProjectPopUp(page: Page):
  return NewProjectPopUp(page)

@pytest.fixture
def projectEditForm(page: Page):
  return ProjectEditForm(page)


def test_userCanLogin(loginForm: LoginForm, todoistApp: TodoistApp):
  # loginForm = LoginForm(page)
  # todoistApp = TodoistApp(page)

  # G user has app opened
  todoistApp.gotoLoginPage()
 
  # W user enters correct credentials
  loginForm.enterLogin('gbinxeqerpnywwysux@awdrt.org')
  loginForm.enterPass('ti4FCvBL39i7mMq')
  loginForm.submitForm()


  # T user checks if is logged in
  todoistApp.waitForMainView()
  cookies = todoistApp.getCookies()
  assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"There is no expected 'todistd' cookie in: {cookies}"
  
  # page.goto('https://app.todoist.com/auth/login')
  # page.locator('#element-0').fill('gbinxeqerpnywwysux@awdrt.org')
  # page.locator('#element-2').fill('ti4FCvBL39i7mMq')
  # page.locator('[type="submit"]').click()
  # page.wait_for_url('https://app.todoist.com/app/today')
  # cookies = page.context.cookies()

  
  
def test_userCanCreateProject(loginForm: LoginForm, todoistApp: TodoistApp, leftSidebar: LeftSidebar, newProjectPopUp: NewProjectPopUp,
                              projectEditForm: ProjectEditForm):
  projectName = 'Moj najlepszy projekt'
  todoistApp.gotoLoginPage()
  loginForm.enterLogin('gbinxeqerpnywwysux@awdrt.org')
  loginForm.enterPass('ti4FCvBL39i7mMq')
  loginForm.submitForm()
  todoistApp.waitForMainView()


  leftSidebar.clickAddProjectButton()
  newProjectPopUp.clickAddNewProject()
  
  projectEditForm.enterProjectName(projectName)
  projectEditForm.submit()

  # page.locator('[aria-label="My projects menu"]').click()
  # page.locator('[aria-label="Add project"]').click()
  # page.locator('input:focus').fill('Moj projekt')
  # page.locator('form [type="submit"]').click()

  # 1
  expect(leftSidebar.getProjectsListEl()).to_contain_text(projectName)
  # expect(page.locator('#projects_list')).to_contain_text('Moj projekt')
  # print(page.locator('#projects_list').inner_text())

  # 2 sprawdzenie czy projek jest w liscie
  projects = leftSidebar.getProjectsNames()
  # projects = page.locator('[data-testid="project-list-item"]').all_text_contents()
  assert projectName in projects

  # 3 sprawdzenie czy nowy projekt jest ostatni
  assert projectName == projects.pop()


  

