import pytest
from steps.Given import Given
from steps.Then import Then
from steps.When import When


def test_userCanLogin(given: Given, when: When, then: Then):
  given.todoistLogginIsOpened()
  when.loginWithCorrectCredentials()
  then.checkIfLoggedIn()
