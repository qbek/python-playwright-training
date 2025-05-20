import pytest

pytest.fixture(scope='module')
def beforeAll():
  print('BeforeAll: Start testów')

  yield

  print('AfterAll: Koniec testów')

@pytest.fixture
def beforeHook():
  print('Before: Przed testem')
  
  yield

  print('After: Koniec testu')

@pytest.fixture
def createData():
  data = { 'name': 'Kuba', 'city': 'Lodz'}
  return data

def test_beforeHook(beforeHook, createData, beforeAll):
  print('To jest test')
  print(createData)
  print(createData['name'])

def test_drugi(beforeHook):
  print('Test 2')