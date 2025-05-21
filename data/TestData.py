from faker import Faker

class TestData:
  def __init__(self):
    self._projectName = None
    self._taskName = None
    self._fake = Faker()

  def defineProjectName(self, name):
    self._projectName = self._fake.company()

  def defineTaskName(self, name):
    self._taskName = self._fake.catch_phrase()
  
  def getProjectName(self):
    return self._projectName
  
  def getTaskName(self):
    return self._taskName