import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMvc import TodoMvc
from pageobjects.TodosList import TodosList


def test_userCanCreateATodo(newTodoInput: NewTodoInput, app: TodoMvc, todosList: TodosList):
    app.openApp()
    todoName = 'Moje todo zmienie tylko raz'
    
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.check_todo_displayed(todoName)



def test_userCanCreateATodoPrim(pageObjects:dict):
    pageObjects['app'].openApp()
    todoName = 'Moje todo zmienie tylko raz'
    
    pageObjects['newTodoInput'].enter_todo_name(todoName)
    pageObjects['newTodoInput'].submit_todo()
    pageObjects['todosList'].check_todo_displayed(todoName)