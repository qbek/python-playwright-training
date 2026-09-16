import pytest

def test_userCanCompleteTheTodo(given, when, then, todoName):
    given.todoMvc_app_is_opened()
    when.create_todo(todoName)
    when.complete_todo()
    then.check_todo_completed()
