import pytest


@pytest.fixture
def beforeEach():
    print('\n--------')
    print('Odpalam sie przed kazdym testem')

@pytest.fixture(scope='module')
def beforeAll():
    print('\n!!!!!!!!!!!!!!!!')
    print('ONE RING TO RULL THEM ALL!!!!')

@pytest.fixture
def beforeAndAfterEach():
    print('\n--------')
    print('to jest BEFORE')

    yield

    print('to jest AFTER!!!!')


@pytest.fixture
def prepareTodoName():
    return "TODO: jakas tam moja nazwa"


def test_noFixtures(beforeAll):
     print('\n===========')
     print('JESTEM GOLY I WESOLY')

def test_basicFixtureExample(beforeAll, beforeEach):
    print('\n===========')
    print('Dzialam!!!')

def test_beforAnAfterExample(beforeAll, beforeAndAfterEach):
    print('\n===========')
    print('Jestem pomiedzy Before i After')
    


def test_dataFixture(beforeAll, prepareTodoName: prepareTodoName):
    print('\n===========')
    print('Dzialam i mam daną!!!')
    print(prepareTodoName)
    print('TADAM!!!!')