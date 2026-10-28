import pytest
from steps.Given import Given
from steps.Then import Then
from steps.When import When


def test_userCanDeleteTodo(given: Given, when: When, then:Then):
    todoName = "Do usunięcia!!! NATYCHMIAST!!!"

    given.userHasAppReady()
    given.userHasTodo(todoName)
    when.userDeletesATodo()
    then.userChecksTodosListEmpty()
