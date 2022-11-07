from unittest import TestCase
from WorkBreakdownStructure import WorkBreakdownStructure

class TestWorkBreakdownStructure(TestCase):
    def setUp(self):
        self.work = WorkBreakdownStructure()

    def test_get_name(self):
        work = "work"
        self.work.setName(work)
        self.assertEqual(self.work.getName(),work)

    def test_get_the_tasks(self):
        task = "tarea"
        self.work.setTheTask(task)
        self.assertEqual(self.work.getTheTasks(),task)
