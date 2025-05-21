from playwright.sync_api import Page
_TASK_EDIT_FORM = '[data-testid="task-editor"]'

_TASK_NAME_INPUT = '[data-placeholder="Task name"]'
_ADD_TASK_BUTTON = '[data-testid="task-editor-submit-button"]'

class TaskEditorForm:
  def __init__(self, page: Page):
    self._page = page

  def enterTaskName(self, taskName):
    # self._page.locator(_TASK_NAME_INPUT).fill(taskName)
    self._page.wait_for_selector(_TASK_EDIT_FORM)
    self._page.keyboard.type(taskName)

  def submitForm(self):
    self._page.locator(_ADD_TASK_BUTTON).click()