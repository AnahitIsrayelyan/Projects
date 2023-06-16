from typing import List
from abc import ABC, abstractmethod


class BaseEncrypter(ABC):
    def __init__(self, text) -> None:
        self._text = text
        self._splitted = []
        self._splitted_key = []


    def rotate_right(self, p) -> str:
        tmp = ''
        tmp = p[4] + p[0] + p[3] + p[7] + p[5] + p[1] + p[2] + p[6]
        return tmp


    def rotate_left(self, p) -> str:
        tmp = ''
        tmp = p[1] + p[5] + p[6] + p[2] + p[0] + p[4] + p[7] + p[3]
        return tmp

    def rotate_up(self, p) -> str:
        tmp = ''
        tmp = p[3] + p[2] + p[6] + p[7] + p[0] + p[1] + p[5] + p[4]
        return tmp

    def rotate_down(self, p) -> str:
        tmp = ''
        tmp = p[4] + p[5] + p[1] + p[0] + p[7] + p[6] + p[2] + p[3]
        return tmp

    def split8elems(self) -> List[str]:
        i = 0
        while (i + 8) <= len(self._text):
            self._splitted.append(self._text[i: i + 8])
            i += 8
        if i < len(self._text):
            part = self._text[i:]
            while len(part) < 8:
                part += '$'
            self._splitted.append(part)
        return self._splitted
    
    def split_key(self):
        self._splitted_key = self._key.split(":")

    
    @abstractmethod
    def execute(self):
        pass