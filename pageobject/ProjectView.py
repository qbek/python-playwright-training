from playwright.sync_api import Page
_PROJECT_LIST_VIEW = '[data-testid="project-list-view"]' 
_ADD_TASK_BUTTON = '[data-testid="project-list-view"] li.task_actions'
_TASK_ITEM = f'{_PROJECT_LIST_VIEW} .task_list_item'

class ProjectView:
  def __init__(self, page: Page):
    self._page = page

  def clickAddTaskButton(self):
    self._page.locator(_ADD_TASK_BUTTON).click()

  def getAllTasksNames(self):
    return self._page.locator(_TASK_ITEM).all_text_contents()