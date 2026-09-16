import pytest

def test_userCanDeleteTodo(todoMvc, newTodoInput, todosList):
    todoName = 'Zadanie do skasowania'

    todoMvc.open_main_view()
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()

    todosList.hover_over_todo()
    todosList.delete_todo()

    todosList.check_todo_NOT_displayed()