from exam import *
from questionnaire1 import questionBank1


if __name__ =="__main__":
    exam = Exam(questionBank1)
    print(exam.start())