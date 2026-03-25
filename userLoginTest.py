import pytest
from playwright.sync_api import Page, expect
from pageobjects.TodoistApp import TodoistApp
from pageobjects.LoginForm import LoginForm


@pytest.fixture
def loginForm(page: Page):
  return LoginForm(page)

@pytest.fixture
def todoistApp(page: Page):
  return TodoistApp(page)

def test_userCanLogin(loginForm: LoginForm, todoistApp: TodoistApp):
  # loginForm = LoginForm(page)
  # todoistApp = TodoistApp(page)

  todoistApp.gotoLoginPage()
 
  loginForm.enterLogin('gbinxeqerpnywwysux@awdrt.org')
  loginForm.enterPass('ti4FCvBL39i7mMq')
  loginForm.submitForm()
  todoistApp.waitForMainView()
  cookies = todoistApp.getCookies()

  # page.goto('https://app.todoist.com/auth/login')
  # page.locator('#element-0').fill('gbinxeqerpnywwysux@awdrt.org')
  # page.locator('#element-2').fill('ti4FCvBL39i7mMq')
  # page.locator('[type="submit"]').click()
  # page.wait_for_url('https://app.todoist.com/app/today')
  # cookies = page.context.cookies()

  assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"There is no expected 'todistd' cookie in: {cookies}"
  
def test_userCanCreateProject(loginForm: LoginForm, todoistApp: TodoistApp, page: Page):
  todoistApp.gotoLoginPage()
  loginForm.enterLogin('gbinxeqerpnywwysux@awdrt.org')
  loginForm.enterPass('ti4FCvBL39i7mMq')
  loginForm.submitForm()
  todoistApp.waitForMainView()

  page.locator('[aria-label="My projects menu"]').click()
  page.locator('[aria-label="Add project"]').click()
  page.locator('input:focus').fill('Moj projekt')
  page.locator('form [type="submit"]').click()

  # 1
  expect(page.locator('#projects_list')).to_contain_text('Moj projekt')
  print(page.locator('#projects_list').inner_text())

  # 2
  projects = page.locator('[data-testid="project-list-item"]').all_text_contents()
  assert 'Moj projekt' in projects

  # 3
  assert 'Moj projekt' == projects.pop()


  

