import pytest
from faker import Faker
from steps.Given import Given
from steps.Then import Then
from steps.When import When


@pytest.fixture
def projectName():
  fake = Faker()
  return fake.name()

def test_userCanCreateProject(given: Given, when: When, then: Then, projectName):
  given.userIsLoggedIn()
  when.createNewProject(projectName)
  then.checkIfProjectIsCreated(projectName)