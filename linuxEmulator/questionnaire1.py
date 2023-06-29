from command import DateCommand, CalCommand, PWDCommand, LSCommand, MKDirCommand, WhoAmICommand, CHMODCommand, CDCommand
from questionnaire import Questionnaire
from task import Task
from userGroup import *

# questionnaire 1

task1 = Task("Type in the command to display the current date and time.", DateCommand(), ["date"])
task2 = Task("Type in the command to display the calendar of the current month.", CalCommand(), ["cal"])
task3 = Task("Type in the command to display the current working directory.", PWDCommand(), ["pwd"])
task4 = Task("Write the correct command that shows the current directory contents.", LSCommand(), ["ls", "ls -l", "ls .", "ls *", "ls -l .", "ls -l *"])
task5 = Task("What command in Linux reveals the identity of the current user?", WhoAmICommand(), ["whoami"])
task6 = Task("Create a directory 'dir1' in the current directory using a relative path", MKDirCommand(), ["mkdir ./dir1", "mkdir dir1"])
task7 = Task("Write the correct command that shows the current directory contents in long format.", LSCommand(), ["ls -l", "ls -l .", "ls -l *"])
task8 = Task("Modify the permissions of 'dir1' to revoke the reading ability for all users", CHMODCommand(), ["chmod -r dir1", "chmod -r ./dir1"])
task9 = Task("Change current directory to dir1", CDCommand(), ["cd dir1", "chmod ./dir1"])
task10 = Task("Write the correct command that shows the current directory contents in long format.", LSCommand(), ["ls -l", "ls -l .", "ls -l *"])


questionBank1 = Questionnaire()
questionBank1.addTasks(task1, task2, task3, task4, task5, task6, task7, task8, task9, task10)



