from datetime import datetime
from task import Task


class ToDo:
    def __init__(self) -> None:
        self._tasks = []
        self._tasksNum = 0
        self._completedTasksNum = 0

    def completedTasks(self):
        return f"Completed tasks: {self._completedTasksNum} / {self._tasksNum}"
    
    def createTask(self, text: str, deadline: datetime = None):
        self._tasks.append(Task(text=text, deadline=deadline))
        self._tasksNum += 1

    def deleteTask(self, task: Task):
        self._tasks.remove(task)
        self._tasksNum -= 1
        if task.isCompleted():
            self._completedTasksNum -= 1

    def completeTask(self, task: Task):
        task.complete()
        self._completedTasksNum += 1

    def editTask(self, task: Task, text: str = None, deadline: datetime = None):
        task.edit(text, deadline)
