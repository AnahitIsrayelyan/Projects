from questionnaire import Questionnaire
from commandInterpreter import CommandInterpreter
from linuxEmulator import LinuxEmulator
from userGroup import *

class Exam:
    def __init__(self, questionBank: Questionnaire) -> None:
        self._questionbank = questionBank
        self._linuxEmulator = LinuxEmulator(User("user1", 1111))
        self._commandInterpreter = CommandInterpreter(self._linuxEmulator)
        self._rightAnswers = 0
        self._allAnswers = 0

    def getLinuxEmulator(self):
        return self._linuxEmulator


    def start(self):
        for task in self._questionbank._tasks:
            self._commandInterpreter.changeTask(task)
            self._rightAnswers += self._commandInterpreter.execute()
            self._allAnswers += 1
        return self.getResult()
    

    def getResult(self):
        if (self._rightAnswers / self._allAnswers) >= 0.9:
            res = "PASSED"
        else:
            res = "Ops! Let's try the next time."
        return f"{self._rightAnswers} / {self._allAnswers}, {res}"


    """ Write all answers in a file along with corresponding questions and correct answers. 
    This file can be used for purposes such as grade review, archiving exam results, and more."""

    # def start(self):
        # studentName = input("Your name, surename: ")
        # group = input("Your wave, group: ")

        # filePath = "C://Users//XPS//Desktop//VS//LinuxEmulator//" + '.'.join(studentName.split(" ")) + ".txt"
        
        # with open(filePath, 'a') as file:
        #     for task in self._questionbank._tasks:
        #         self._commandInterpreter.changeTask(task)
        #         file.write(task.getTask())
        #         file.write(task.getValidInputs())
        #         file.write(task.getStudentAnswer())
        #         self._rightAnswers += self._commandInterpreter.execute()
        #         self._allAnswers += 1
        # return self.getResult()
