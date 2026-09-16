import pytest

def test_userCanCompleteTheTodo(todoMvc, newTodoInput, todosList, todoName):
    todoMvc.open_main_view()
    newTodoInput.enter_todo_name(todoName)
    newTodoInput.submit_todo()

    todosList.complete_todo()
    todosList.check_todo_marked_completed()
