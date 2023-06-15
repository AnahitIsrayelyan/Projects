import re
import os
import PyPDF2

"""
PDFReader is a class that allows you to extract text from a PDF file, 
normalize and search for words within it, and generate an output file 
containing the found words. This class makes use of the PyPDF2 library for PDF processing.
"""

""" 
Some parts of the code are taken from searchEngine project, 
but as long as the domains of the tasks are different
here we don't use already implemented parts from the previous one.
"""

"""
We assume that the files are large enough to download to RAM, 
so we work directly with files, which, however, makes the program work longer.
"""

class PDFReader:
    def __init__(self, inputFile, outputFile, dictt) -> None:
        self._inputFile = inputFile
        self._outputFile = outputFile
        self._dict = dictt


    def normalize(self, word: str):
        return re.sub(r'[^a-zA-Z]', '', word).lower()
    

    def modify(self, word):
        if not word:
            return ''
        return word[:-1] if word[-1] == 's' and len(word) != 0 else word


    def search(self, word, dictt = None) -> bool:
        if not word or word == "":
            return False
        if not dictt:
            dictt = self._dict
        with open(dictt, 'r') as file:
            for line in file:
                line = line.strip()  
                if word != "" and line == word:
                    return True
        return False
    

    def execute(self):
        with open(self._inputFile, 'rb') as ifile, open(self._outputFile, 'a+') as ofile:
            reader = PyPDF2.PdfReader(ifile)
            for page in reader.pages:
                text = page.extract_text()
                words = text.split()
                for word in words:
                    normWord = self.normalize(word)
                    if self.search(normWord):
                        pass
                    elif self.search(self.modify(normWord)):
                        normWord = self.modify(normWord)
                    else:
                        continue

                    # if not self.search(normWord, self._outputFile):
                    #     ofile.write(normWord + '\n')
                    ofile.seek(0)
                    if normWord not in ofile.read():
                        ofile.seek(0, os.SEEK_END)
                        ofile.write(normWord + '\n')




if __name__ == "__main__":
    inputPath = "C:\\Users\\XPS\\Desktop\\VS\\AlgorithmsDataStructures\\pdf2txt\\input.pdf"
    outputPath = "C:\\Users\\XPS\\Desktop\\VS\\AlgorithmsDataStructures\\pdf2txt\\output.txt"
    dictt = "C:\\Users\\XPS\\Desktop\\VS\\AlgorithmsDataStructures\\pdf2txt\\words_alpha.txt"

    reader = PDFReader(inputPath, outputPath, dictt)
    reader.execute()
