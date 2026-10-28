import pytest
from steps.Given import Given
from steps.Then import Then
from steps.When import When
from testdata.TodoNameGenerator import TodoNameGenerator


testData = TodoNameGenerator()


def test_userCanCompleteATodo(given: Given, when: When, then:Then): 
    todoName = testData.getTodoName()
    
    given.userHasAppReady()
    given.userHasTodo(todoName)
    when.userCompletesTodo()
    then.userChecksTodoMarkedAsCompleted()


def test_checkActiveFilters(given: Given, when: When, then:Then):
    todoName = testData.getTodoName()

    given.userHasAppReady()
    given.userHasCompletedTodo(todoName)
    when.userSelectsActiveFilter()
    then.userChecksTodosListEmpty()
    

def test_checkCompletedFilter(given: Given, when: When, then:Then): 
    todoName = testData.getTodoName()

    given.userHasAppReady()
    given.userHasCompletedTodo(todoName)
    when.userSelectsCompletedFilter()
    then.userChecksTodoIsDisplayed(todoName)

def test_jaksTamfun(given: Given, when: When, then:Then):
    todoName = testData.getTodoName()

    given.userHasAppReady()
    given.userHasCompletedTodo(todoName)
    when.userDeletesATodo()
    then.userChecksTodosListEmpty()