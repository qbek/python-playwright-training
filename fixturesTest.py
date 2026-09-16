import pytest

@pytest.fixture(scope='module')
def beforeAll():
    print('\n I will be executed only ONCE!!!')

@pytest.fixture
def beforeAndAfter():
    print('\n DO IT BEFORE TEST')

    yield

    print('\n DO IT AFTER')


def test_sample_1(beforeAll, beforeAndAfter):
    print('')
    print('To jest test 1')

def test_sample_2(beforeAll, beforeAndAfter):
    print('\n to jest test 2')


@pytest.fixture
def prepareData():
    return "Jestem przygotowana daną"

def test_sample_3(prepareData):
    print('\n start testu')
    print(prepareData)