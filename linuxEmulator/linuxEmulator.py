from userGroup import User
from fileSystem import FileSystem, Directory


class LinuxEmulator:
    def __init__(self, user: User) -> None:
        self._users = [user]
        self._currentUser = user
        self._fileSystem = FileSystem(Directory("root", user))
        self._currendDirectory = self._fileSystem.getRoot()


    def changeUser(self, name: str):
        for user in self._users:
            if user.getName() == name:
                self._currentUser = user
                return
            
            
    def changeCurrentDirectory(self, dir: Directory):
        self._currendDirectory = dir
        

    def getFileSystem(self):
        return self._fileSystem
    
    def getCurrentDirectory(self):
        return self._currendDirectory
    
    def searchDirectory(self):
        pass

    def getCurrentUser(self):
        return self._currentUser
    
    def addUser(self, name: str):
        self._users.append(User(name))
