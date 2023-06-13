import tkinter as tk
from tkinter import messagebox
from toDo import ToDo
from datetime import datetime


def update():
    taskList.delete(0, tk.END)

    for task in todo._tasks:
        text = task.getText()

        lessDay = False
        if task.lessThanDay():
            lessDay = True
        elif task.closeToDeadline():
            text = "[Close to deadline] " + text
        elif task.isCompleted():
            text = "[Completed] " + text
            
        
        if task.getDeadline():
            text += " " + str(task.getDeadline())
        
        taskList.insert(tk.END, text)
        
    completedTasksLabel.config(text=todo.completedTasks())


def addTask():
    newText = entry.get()
    if newText:
        todo.createTask(text=newText)
        update()
        entry.delete(0, tk.END)

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



todo = ToDo()

window = tk.Tk()
window.title("ToDo List")

taskList = tk.Listbox(window, width=50)
# add paddings in pixels around widgets
taskList.pack(pady=10)

completedTasksLabel = tk.Label(window, text=todo.completedTasks())
# pack places the widget in the window based on available space and packing options
completedTasksLabel.pack()  

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

buttonAdd = tk.Button(window, text="Add Task", command=addTask)
buttonAdd.pack(pady=5)
buttonDelete = tk.Button(window, text="Delete Task", command=deleteTask)
buttonDelete.pack(pady=5)
buttonComplete = tk.Button(window, text="Mark as Completed", command=completeTask)
buttonComplete.pack(pady=5)
buttonComplete = tk.Button(window, text="Add deadline", command=addDeadline)
buttonComplete.pack(pady=5)
buttonEdit = tk.Button(window, text="Edit Task", command=editTask)
buttonEdit.pack(pady=5)


window.mainloop()