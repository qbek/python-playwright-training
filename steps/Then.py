from pageobject.ProjectView import ProjectView
from pageobject.ProjectsList import ProjectsList
from pageobject.TodoistApp import TodoistApp


class Then:
  def __init__(self, page):
    self._todoist = TodoistApp(page)
    self._projects = ProjectsList(page)
    self._projectView = ProjectView(page)

  def userChecksIfIsLoggedIn(self):
    cookies = self._todoist.getAllCookies()
    assert any(cookie['name'] == 'todoistd' for cookie in cookies), f"Expected cookie todoistd dosn't exists in: {cookies}"
    self._todoist.saveSession()

  def userVerifiesCreatedProject(self, projectName):
    existingProjects = self._projects.getExistingProjects()
    print (existingProjects)
    assert existingProjects.pop() == projectName

    # assert projectName in existingProjects

    # Jezeli chcecie korzystac z asercji Playwright to z PO zwracajcie sobie element do sprawdzenia
    # allProjects = projects.getAllProjectItemEl()
    # expect(allProjects).to_contain_text(projectName)

  def userChecksIfTaskIsCreated(self, taskName):
    existingTasks = self._projectView.getAllTasksNames()
    assert existingTasks.pop() == taskName