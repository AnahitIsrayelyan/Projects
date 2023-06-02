from wordAndText import *

class Program:
    files = {
        '1.txt': 1, 
        '2.txt': 2
        }

    def write(self):
        for file in Program.files.keys():
            text = Text(input_file=file)
            text.executet() 
            text.write_in_file(Program.files[file])
            # with open('db.txt', 'r') as db:
            #     for line in db:
            #         print(line)

    def search(self):
        word  = input("enter a word: ")
        word = word.split()[0]
        with open('db.txt', 'r', encoding='utf-8') as db:
            for line in db:
                line = line.strip()
                if line.split(':')[0] == word:
                    print(f"The word '{word}' is found in file(s) {line.split(':')[1]}")
                    return
            print('Not found such a word.')

    def execute(self):
        self.write()
        self.search()




    
