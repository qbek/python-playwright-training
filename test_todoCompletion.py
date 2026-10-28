import pytest
from playwright.sync_api import Page
from pageobjects.Filters import Filters
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMvc import TodoMvc
from pageobjects.TodosList import TodosList




def test_userCanCompleteATodo(app: TodoMvc, newTodoInput:NewTodoInput, todosList:TodosList): 
    todoName = 'Wykonane zadanie'

    
    app.openApp()
    
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()

    todosList.check_complete_toggle()
    todosList.check_todo_marked_as_completed()


def test_checkActiveFilters(app: TodoMvc, newTodoInput: NewTodoInput, todosList: TodosList, filters: Filters):
    todoName = 'Wykonane zadanie'

    app.openApp()

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    
    todosList.check_complete_toggle()
    filters.goto_active()
    todosList.check_list_empty()    


def test_checkCompletedFilter(app: TodoMvc, newTodoInput: NewTodoInput, todosList: TodosList, filters: Filters): 
    todoName = 'Wykonane zadanie'

    app.openApp()

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()

    todosList.check_complete_toggle()

    filters.goto_completed()
    todosList.check_todo_displayed(todoName)