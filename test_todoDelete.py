import pytest
from playwright.sync_api import Page
from pageobjects.NewTodoInput import NewTodoInput
from pageobjects.TodoMvc import TodoMvc
from pageobjects.TodosList import TodosList


def test_userCanDeleteTodo(newTodoInput: NewTodoInput, todosList: TodosList, app: TodoMvc):
    todoName = "Do usunięcia!!! NATYCHMIAST!!!"

    app.openApp()
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()


    todosList.hover_over_todo()
    todosList.delete_todo()

    todosList.check_list_empty()