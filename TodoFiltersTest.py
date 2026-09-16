import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoFilters import TodoFilters
from pageobjects.TodosList import TodosList
from pageobjects.TodoMVCApp import TodoMVCApp



def test_userCanFilterActiveTodos(given, when, then, todoName):
    given.todoMvc_app_is_opened()
    given.completed_todo(todoName)
    when.goto_active_todos()
    then.check_todos_list_is_emtpy()

def test_userCanFilterCompletedTodos(newTodoInput, todosList, todoFilters, todoMvc, todoName):
    todoMvc.open_main_view()

    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()
    todosList.complete_todo()
    todoFilters.goto_completed_filter()
    todosList.check_todo_displayed(todoName)