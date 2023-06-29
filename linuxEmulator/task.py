from abc import ABC, abstractmethod
from typing import List
from command import Command


class Task(ABC):
    def __init__(self, taskText: str, command: Command, validInputs: List[str]) -> None:
        super().__init__()
        self._taskText = taskText
        self._command = command
        self._validInputs = validInputs
        self._studentAnswer = ''
    

    def getTask(self):
        return self._taskText
    

    def getValidInputs(self):
        return self._validInputs
    

    def getStudentAnswer(self):
        return self._studentAnswer
    

    def studentAnswer(self, answer):
        self._studentAnswer = answer


    def callCommand(self, linEm, option, args):
        output = self._command.execute(linEm, option=option, args=args)
        if output:
            return output
        return None
