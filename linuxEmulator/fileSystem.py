from abc import ABC, abstractmethod
from collections import deque
from typing import List
from userGroup import User


class Directory:
    pass


class BaseFile(ABC):
    def __init__(self, name: str, user: User, parent: Directory = None) -> None:
        super().__init__()
        self._name = name
        self._owner = user
        self._parent = parent
        self._permissions = 664


    def getName(self):
        return self._name
    

    def getUser(self):
        return self._owner


    def permissionsHelper(self):
        def miniHelper(num):
            minipermission = ''
            if num / 4 >= 1:
                minipermission += 'r'
                num //= 4
            else:
                minipermission += '-'

            if num / 2 >= 1:
                minipermission += 'w'
                num //= 2
            else:
                minipermission += '-'

            if num >= 1:
                minipermission += 'x'
            else:
                minipermission += '-'
            
            return minipermission
            
        permission = ''
        permission += miniHelper(self._permissions // 100)
        permission += miniHelper((self._permissions % 100) // 10)
        permission += miniHelper(self._permissions % 10)

        return permission
    
    
    def getPermissions(self):
        return self._permissions
    

    def changePermissions(self, newPermission: int):
        self._permissions = newPermission


    @abstractmethod
    def permissionsAsString(self):
        pass


    def chmod(self, user, operation, permission):
        try:
            if user == 'u':
                user_permissions = int(str(self._permissions)[0])
                new_permissions = self._apply_operation(user_permissions, operation, permission)
                self._permissions = int(str(new_permissions) + str(self._permissions)[1:])
            elif user == 'g':
                group_permissions = int(str(self._permissions)[1])
                new_permissions = self._apply_operation(group_permissions, operation, permission)
                self._permissions = int(str(self._permissions)[0] + str(new_permissions) + str(self._permissions)[2])
            elif user == 'o':
                others_permissions = int(str(self._permissions)[2])
                new_permissions = self._apply_operation(others_permissions, operation, permission)
                self._permissions = int(str(self._permissions)[:2] + str(new_permissions))
            elif user == None:
                if operation == '=':
                    self._permissions = permission
                elif operation == '-' or operation == '+':
                    user_permissions = int(str(self._permissions)[0])
                    group_permissions = int(str(self._permissions)[1])
                    others_permissions = int(str(self._permissions)[2])

                    user_new_permissions = self._apply_operation(user_permissions, operation, permission)
                    group_new_permissions = self._apply_operation(group_permissions, operation, permission)
                    other_new_permissions = self._apply_operation(others_permissions, operation, permission)

                    self._permissions = int(str(user_new_permissions) + str(group_new_permissions) + str(other_new_permissions))
        except:
            print('Invalide mode.')
 

    def _apply_operation(self, current_permissions, operation, permission):
        if operation == '+':
            new_permissions = current_permissions | permission
        elif operation == '-':
            new_permissions = current_permissions & ~permission
        return new_permissions


class Directory(BaseFile):
    def __init__(self, name: str, user: User, parent: Directory = None,) -> None:
        super().__init__(name, user, parent)
        self._children = []


    def permissionsAsString(self):
        return 'd' + super().permissionsHelper()


    def ls(self):
        names = ''
        for file in self._children:
            names += file.getName() + " "
        return names
    

    def lsl(self):
        info = []
        for file in self._children:
            info.append(str(file.permissionsAsString() + ' ' + file.getUser().getName() + ' ' + file.getName()))
        return info


    def pwd(self):
        print(self._name)


    def addChildDirectory(self, childrenNames: List[str], parent):
        for name in childrenNames:
            self._children.append(Directory(name, self._owner, parent))


    def rmr(self, args):
        pass


class RegularFile(BaseFile):
    def __init__(self, name: str, user: User, parent: Directory) -> None:
        super().__init__(name, user, parent)
        self._content = ''


    def permissionsAsString(self):
        return '-' + super().permissionsHelper()
    

    def chmod(self):
        pass
    

    def rm(self, args):
        pass


class Link(BaseFile):
    def __init__(self, name: str, baseFile: BaseFile, user: User) -> None:
        super().__init__(name, user)
        self._baseFile = baseFile


class SymbolicLink(Link):
    def __init__(self, name: str, baseFile: BaseFile, user: User) -> None:
        super().__init__(name, baseFile, user)


    def permissionsAsString(self):
        # return 'l' + super().permissionsHelper()
        pass


class FileSystem:
    def __init__(self, root: Directory) -> None:
        self._root = root


    def getRoot(self):
        return self._root
    

    def searchDirectory(self, path: str, linEm = None):
        path = path[0]
        try:
            if '/' in path:
                dir_names = path.split('/')
                if dir_names[0] == '.':
                    dir_names = dir_names[1:]
                    dir = linEm.getCurrentDirectory()
                dir = self._root
            else:
                dir_names = [path]
                dir = linEm.getCurrentDirectory()
            for dir_name in dir_names:
                dir = self._searchHelper(dir, dir_name)
                if dir is None:
                    return None
            return dir
        except:
            print("Invalid arguments.")
    

    def _searchHelper(self, dir: Directory, dir_name: str):
        for child in dir._children:
            if child._name == dir_name:
                return child    
        return None
        
    

   
