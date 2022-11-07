from unittest import TestCase
from Task import Task

class TestTask(TestCase):
    def setUp(self):
        self.tasks = Task()

    def test_get_name(self):
        tareas = ["Extract Program", "Validation", "Conversion", "Import", "Extract Program", "Validation",
                  "Conversion", "Import", "Extract Program", "Validation", "Conversion", "Import"]

        for i in tareas:
            self.tasks.setName(i)
            self.assertEqual(self.tasks.getName(),i)

    def test_get_the_resources(self):
        res = "resource"
        self.tasks.setTheResources(res)
        self.assertEqual(self.tasks.getTheResources(),res)

    def test_get_the_employees(self):
        emp = "employee"
        self.tasks.setTheEmployees(emp)
        self.assertEqual(self.tasks.getTheEmployees(),emp)