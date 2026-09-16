import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodosList import TodosList
from pageobjects.TodoMVCApp import TodoMVCApp




def test_userCanCreateATodo(page: Page):
    todoName = 'To jest moje lepsze zadanie'
    todoMvc = TodoMVCApp(page)
    newTodoInput = NewTodoInput(page)
    todosList = TodosList(page)

    
    todoMvc.open_main_view()
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.check_todo_displayed(todoName)
    

