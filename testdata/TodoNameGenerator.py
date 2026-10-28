from faker import Faker

class TodoNameGenerator:

    def __init__(self):
        self._faker = Faker()

    def getTodoName(self):
        return self._faker.catch_phrase()
