import pytest
from steps.Given import Given
from steps.Then import Then
from steps.When import When


def test_userCanCreateATodo(given: Given, when: When, then: Then):
    todoName = 'Moje todo zmienie tylko raz'
    given.userHasAppReady()
    when.userCreatesATodo(todoName)
    then.userChecksTodoIsDisplayed(todoName)



def test_userCanCreateATodoPrim(pageObjects:dict):
    pageObjects['app'].openApp()
    todoName = 'Moje todo zmienie tylko raz'
    
    pageObjects['newTodoInput'].enter_todo_name(todoName)
    pageObjects['newTodoInput'].submit_todo()
    pageObjects['todosList'].check_todo_displayed(todoName)