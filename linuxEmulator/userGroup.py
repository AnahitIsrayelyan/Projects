from typing import List


class User:
    def __init__(self, name: str, password) -> None:
        self._name = name
        self._password = password
        self._groups: List['Group'] = []

    def addGroup(self, group):
        pass

    def getName(self):
        return self._name


class Group:
    def __init__(self, name: str) -> None:
        self._name = name
        self._users: List['User'] = []

    def addUser(self, user: User):
        # self._users.append(user)
        pass
