import re
import os


class Word:
    def __init__(self, word: str) -> None:
        self._word = word

    def normalize(self):
        self._word = re.sub(r'[^a-zA-Z]', '', self._word).lower()
    
    # remove 's' or other changes
    def modify(self):
        if not self._word:
            return Word('')
        return Word(self._word[:-1]) if self._word[-1] == 's' and len(self._word) != 0 else Word(self._word)
    
    def get(self):
        return self._word
    
    def search(self, dict = 'words_alpha.txt') -> bool:
        with open(dict, 'r') as file:
            for line in file:
                line = line.strip()  
                if line == self._word:
                    return True
        return False
   

class Text:
    def __init__(self, input_file, word_alpha = 'words_alpha.txt') -> None:
        self._input_file = input_file
        self._words_alpha = word_alpha
        self._raw_text = ''
        self._words = []

    # all words in the file are normalized and saved as Word objects in self._words
    def executet(self):
        self.read_text()
        self.split_text()
        self.normalize_text()

    # read the text, remove '/n'-s, and save the whole text in self._raw_text data member
    def read_text(self):
        with open(self._input_file, 'r', encoding='utf-8') as file:  
            for line in file:
                line = line.strip()
                self._raw_text = self._raw_text + line + ' '
    
    # from _raw_text create an array from words, save all the words in self._words as Word objects
    # the result of this function is self._words from Word objects which are not normalized
    def split_text(self):
        self._words = self._raw_text.split()
        for i in range(len(self._words)):
            self._words[i] = Word(self._words[i])
        self._raw_text = None
    
    # normalize all words in self._words, if data of Word obj is in dictionary, 
    # append that obj to a new list normalized
    # if not, modify and search again, if it's ok, append to normalized list, if not, skip
    # the result is that all words in self._words are normalized, here are saved Word objects
    def normalize_text(self):
        normalized = []
        for i in range(len(self._words)):
            self._words[i].normalize()
            if self._words[i]:
                if self._words[i].search():
                    normalized.append(self._words[i])
                elif self._words[i].modify().search():
                    normalized.append(self._words[i].modify())
        self._words = normalized
        # here are stored 'Word' objects 


    def write_in_file(self, filenum: int, db = 'db.txt'):
        with open(db, 'r', encoding='utf-8') as db:
            with open('tmp.txt', 'w', encoding='utf-8') as tmp:
                for word_obj in self._words:
                    pr = False
                    db.seek(0) 
                    for line_curr in db:
                        line = str(line_curr.strip())
                        line = line.split(':')[0]
                        # print(line, word_obj.get())
                        if line == word_obj.get():
                            txt = line_curr.strip() + ',' + str(filenum)
                            tmp.write(txt + '\n')
                            pr = True
                            break
                    if not pr:
                        tmp.write(word_obj.get() + ':' + str(filenum) + '\n')

        os.remove('db.txt')
        os.rename('tmp.txt', 'db.txt')


    
if __name__ == "__main__":
    word = Word("helllos")
    word = word.modify()
    print(word.get())
    # print(word.search())

    # text = Text('1.txt')
    # text.executet()
    # text.read_text()
    # print(text._raw_text)
    # text.split_text()
    # print("split is done")
    # text.normalize_text()
    # for i in text._words:
    #     print(i.get())
    # text.write_in_file(1)

