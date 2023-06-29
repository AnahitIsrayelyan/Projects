from task import Task
from linuxEmulator import LinuxEmulator


"""commands and their options, to check student answers"""
COMMANDS = {
    'ls' : ['-l', '*', '.'],
    'mkdir' : [],
    'pwd' : [],
    'date' : [],
    'cal' : [],
    'rm' : ['-r'],
    'whoami' : [],
    'chmod' : ['+r', '-r', '+w', '-w', '+x', '-x', 
               'u+r', 'u-r', 'u+w', 'u-w', 'u+x', 'u-x', 
               'g+r', 'g-r', 'g+w', 'g-w', 'g+x', 'g-x',
               'o+r', 'o-r', 'o+w', 'o-w', 'o+x', 'o-x'],
    'su' : [],
    'mv' : [],
    'cd' : [],

    # etc.
}


class CommandInterpreter:
    def __init__(self, linuxEmulator: LinuxEmulator) -> None:
        self._linuxEmulator = linuxEmulator
        self._task = None


    def changeTask(self, task: Task):
        self._task = task


    def getTaskText(self):
        return self._task.getTask()


    """parse function reads the given string and determines the parts of the command: command, options, arguments"""
    def parse(self, task: Task):
        studentAnswer = task.getStudentAnswer()
        splittedAnswer = studentAnswer.split(" ")
        command = splittedAnswer[0]
        option = splittedAnswer[1] if (len(splittedAnswer) > 1) else None
        args = splittedAnswer[2:] if (len(splittedAnswer) > 2) else None
        if self._findCommand(command, option):
            return {'command': command, 
                'option' : option,
                'args': args}
        elif self._findCommand(command):
            if option != None and args != None:
                args = [option] + args
            elif option != None:
                args = [option]
            return {'command': command, 
                    'option' : None,
                    'args': args}
    

    def _findCommand(self, command, option = None):
        if command in COMMANDS.keys():
            if option:
                if option not in COMMANDS[command]:
                    return False
                return True
            return True
        return False


    """validate function checks if the given command(string) is valid"""
    def validate(self) -> bool:
        return (self._task.getStudentAnswer() in self._task.getValidInputs())


    """execute function delegates to task's execute()
    the function anyway calls the approperate function (command) to keep the valid state for upcoming tasks"""
    def execute(self):
        right = 0
        print(self.getTaskText())
        self._task.studentAnswer(input("Your answer: "))
        validate = self.validate()
        if validate:
            parsedCommand = self.parse(self._task)
            option = parsedCommand['option'] if (parsedCommand['option'] != None) else None
            args = parsedCommand['args'] if (parsedCommand['args'] != None) else None

            self._task.callCommand(self._linuxEmulator, option, args)
            right = 1
        return right
    
