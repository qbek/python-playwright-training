import pytest
from steps.Given import Given
from steps.Then import Then
from steps.When import When


def test_userCanCompleteATodo(given: Given, when: When, then:Then): 
    todoName = 'Wykonane zadanie'

    given.userHasAppReady()
    given.userHasTodo(todoName)
    when.userCompletesTodo()
    then.userChecksTodoMarkedAsCompleted()


def test_checkActiveFilters(given: Given, when: When, then:Then):
    todoName = 'Wykonane zadanie'

    given.userHasAppReady()
    given.userHasCompletedTodo(todoName)
    when.userSelectsActiveFilter()
    then.userChecksTodosListEmpty()
    

def test_checkCompletedFilter(given: Given, when: When, then:Then): 
    todoName = 'Wykonane zadanie'

    given.userHasAppReady()
    given.userHasCompletedTodo(todoName)
    when.userSelectsCompletedFilter()
    then.userChecksTodoIsDisplayed(todoName)