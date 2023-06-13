from datetime import datetime, timedelta

class Task:
    def __init__(self, text: str, deadline: datetime = None) -> None:
        self._text = text
        self._deadline = deadline
        self._completed = False

    def complete(self):
        self._completed = True

    def edit(self, text: str = None, deadline: datetime = None):
        if text:
            self._text = text
        if deadline:
            self._deadline = deadline

    def isCompleted(self):
        return self._completed
    
    def getText(self):
        return self._text
    
    def getDeadline(self):
        return self._deadline
    
    def closeToDeadline(self):
        if self._deadline:
            curr = datetime.now()
            return (curr < self._deadline) and (self._deadline - curr).total_seconds() < 3600
        return False
    
    def lessThanDay(self):
        if self._deadline:
            diff = self._deadline - datetime.now()
            if diff < timedelta(days=1):
                return True
        return False
    
