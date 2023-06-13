import tkinter as tk
from tkinter import messagebox
from toDo import ToDo
from datetime import datetime


# functions for button commands
def update():
    taskList.delete(0, tk.END)

    for task in todo._tasks:
        text = task.getText()

        if task.isCompleted():
            text = "[Completed] " + text
        elif task.closeToDeadline():
            text = "[Close to deadline] " + text
        elif task.lessThanDay():
            text = "[Less than a day] " + text
            
        
        if task.getDeadline():
            text += " " + str(task.getDeadline())
        
        taskList.insert(tk.END, text)
        
    completedTasksLabel.config(text=todo.completedTasks())
    entry.delete(0, tk.END)


def addTask():
    newText = entry.get()
    if newText:
        todo.createTask(text=newText)
        update()
        

def deleteTask():
    currTasks = taskList.curselection()
    if currTasks:
        currind = currTasks[0]
        currTask = todo._tasks[currind]
        todo.deleteTask(currTask)
        update()

def completeTask():
    currTasks = taskList.curselection()
    if currTasks:
        currind = currTasks[0]
        currTask = todo._tasks[currind]
        todo.completeTask(currTask)
        update()

def addDeadline():
    taskDeadline = entry.get()
    currTasks = taskList.curselection()
    if taskDeadline and currTasks:
        currind = currTasks[0]
        currTask = todo._tasks[currind]
        # date_string = "2023-06-13 10:30:00"
        date_format = "%Y-%m-%d %H:%M:%S"
        currTask.edit(deadline=datetime.strptime(taskDeadline, date_format))
        update()

def editTask():
    newText = entry.get()
    currTasks = taskList.curselection()
    if newText and currTasks:
        currind = currTasks[0]
        currTask = todo._tasks[currind]
        currTask.edit(text = newText)
        update()



# window and it attributes 
todo = ToDo()

window = tk.Tk()
window.title("ToDo List")

taskList = tk.Listbox(window, width=50)
# add paddings in pixels around widgets
taskList.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

completedTasksLabel = tk.Label(window, text=todo.completedTasks())
# pack places the widget in the window based on available space and packing options
completedTasksLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entry = tk.Entry(window, width=40)
entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

buttonAdd = tk.Button(window, text="Add Task", command=addTask)
buttonAdd.grid(row=3, column=0, padx=5, pady=5)

buttonDelete = tk.Button(window, text="Delete Task", command=deleteTask)
buttonDelete.grid(row=3, column=1, padx=5, pady=5)

buttonComplete = tk.Button(window, text="Mark as Completed", command=completeTask)
buttonComplete.grid(row=4, column=0, padx=5, pady=5)

buttonDeadline = tk.Button(window, text="Add Deadline", command=addDeadline)
buttonDeadline.grid(row=4, column=1, padx=5, pady=5)

buttonEdit = tk.Button(window, text="Edit Task", command=editTask)
buttonEdit.grid(row=5, column=0, columnspan=2, pady=5)


window.mainloop() 