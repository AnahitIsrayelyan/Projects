from abc import ABC, abstractmethod
from datetime import datetime
import calendar
from collections import deque


class Command(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._commandCallStrings = []


    @abstractmethod
    def execute(self):
        pass


class DateCommand(Command):
    def execute(self, linEm = None, option = None, args = None):
        print(datetime.now())
        return None
    

class CalCommand(Command):
    def execute(self, linem = None, option = None, args = None):
        year = datetime.now().year
        month = datetime.now().month
        cal = calendar.monthcalendar(year, month)
        print(calendar.month_name[month], year)
        print(" Mo Tu We Th Fr Sa Su")
        
        for week in cal:
            line = ""
            for day in week:
                if day == 0:
                    line += "   "
                else:
                    line += f"{day:2d} "
            print(line)
        return None


class PWDCommand(Command):
    def execute(self, linEm, option = None, args = None):
        linEm.getCurrentDirectory().pwd()


class LSCommand(Command):
    def execute(self, linEm, option = None, args = None):
        try:
            if option is None:
                if args is None or args in ['*', '.']:
                    print(linEm.getCurrentDirectory().ls())
                else:
                    info = []
                    for path in args:
                        dir = linEm.getFileSystem.searchDirectory(path)
                        if dir is not None:
                            info += dir.ls()
                    for i in info:
                        print(i)
            elif option in ['-l']:
                if args is None or args in ['*', '.']:
                    print(linEm.getCurrentDirectory().lsl())
                else:
                    info = []
                    for path in args:
                        dir = linEm.getFileSystem.searchDirectory(path)
                        if dir is not None:
                            info += dir.lsl()
                    for i in info:
                        print(i)
        except:
            print('Invalid command.')


class MKDirCommand(Command):
    def execute(self, linEm, option = None, args = None):
        linEm.getCurrentDirectory().addChildDirectory(args, linEm.getCurrentDirectory())


class WhoAmICommand(Command):
    def execute(self, linEm, option = None, args = None):
        print(linEm.getCurrentUser().getName())


class CHMODCommand(Command):
    def execute(self, linEm, option = None, args = None):
        try:
            file = linEm.getFileSystem().searchDirectory(args, linEm)
            if not file:
                linEm.getCurrentDirectory()
            if option[0] == '=':
                user = None
                operation = '='
                permission = int(option[1:])
            else:
                user = option[0]
                operation = option[1]
                permission = option[2:]
            file.chmod(user, operation, permission)
        except:
            print('Invalid command.')

        
class CDCommand(Command):
    def execute(self, linEm, option = None, args = None):
        dir = linEm.getFileSystem().searchDirectory(args, linEm)
        if dir:
            linEm.changeCurrentDirectory(dir)
        else:
            print('Invalid command.')


class UserAddCommand(Command):
    def execute(self, linEm, option = None, args = None):
        pass


class SUCommand(Command):
    def execute(self, linEm, option = None, args = None):
        pass


class RMCommand(Command):
    def execute(self, linEm, option = None, args = None):
        pass


class TouchCommand(Command):
    pass


class MVCommand(Command):
    pass




