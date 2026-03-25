import pytest

@pytest.fixture(scope="module")
def moduleHook():
  print("before module")

  yield

  print("after module")


@pytest.fixture
def beforeAndAfterHook():
  print("before hook")

  yield

  print("after hook")



def test_sample1(moduleHook, beforeAndAfterHook):
  print("test execution 1")


def test_sample2(moduleHook, beforeAndAfterHook):
  print("test execution 2")



def prepareData():
  data = { "name": "Kuba", "city": "Lodz"}
  return data


@pytest.fixture
def dataFixture():
  return prepareData()

@pytest.fixture
def richDataFixture():
  data = prepareData()
  data['name'] = 'Jakub'
  return data

def test_sample3(dataFixture, richDataFixture):
  print(dataFixture['name'])
  print(richDataFixture['name'])
  # print(richDataFixture['street'])
  # print(dataFixture['street'])


  
