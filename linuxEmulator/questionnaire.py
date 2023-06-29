from typing import List
from task import Task


class Questionnaire:
    def __init__(self):
        self._tasks: List['Task'] = []


    def addTasks(self, *args):
        for arg in args:
            self._tasks.append(arg)
