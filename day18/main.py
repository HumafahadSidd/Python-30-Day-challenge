"""
📢 Day 18 – Daily Python Challenge 🐍
🚀 Challenge: To-Do List App with GUI! ✅📋

🔥 Project Goal: Create a To-Do List App using Tkinter where users can add, delete, and mark tasks as completed.

📌 Features to Implement:
✅ Add Tasks: Users can type a task and click “Add” to include it in the list.
✅ Mark Completed: Clicking a task should mark it as completed (change color or strike-through text).
✅ Delete Task: Users should be able to remove tasks from the list.
✅ Save Data: Save tasks to a file (tasks.txt) so they persist after closing the app.

"""


# Importing Required Libraries
from tkinter import *
from tkinter import messagebox  
import os

# Creating a Window
root = Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(0, 0)

# Creating a List
tasks = []

# Function to Add Task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to Delete Task
def delete_task():
    task = listbox.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()
    
# Function to Mark Task as Completed
def mark_task():
    task = listbox.get("active")
    if task in tasks:
        tasks.remove(task)
        tasks.append(f"{task} (Completed)")
        update_listbox()

# Function to Update Listbox
def update_listbox():
    listbox.delete(0, "end")
    for task in tasks:
        listbox.insert("end", task)

# Function to Save Tasks
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")
    messagebox.showinfo("Info", "Tasks have been saved.")

# Function to Load Tasks
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            tasks = f.read().split("\n")
            update_listbox()

# Creating a Label
label = Label(root, text="Enter Task:")
label.pack(pady=10)

# Creating an Entry
entry = Entry(root, width=30)
entry.pack(pady=10)

# Creating a Frame
frame = Frame(root)
frame.pack(pady=20)

# Creating a Listbox
listbox = Listbox(frame, width=50, height=10)
listbox.pack(side="left", fill="y")

# Creating a Scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Configuring Listbox and Scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Creating Buttons
add_button = Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10, fill="x")

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=10, fill="x")

mark_button = Button(root, text="Mark Completed", command=mark_task)
mark_button.pack(pady=10, fill="x")

save_button = Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=10, fill="x")

load_button = Button(root, text="Load Tasks", command=load_tasks)
load_button.pack(pady=10, fill="x")

# Loading Tasks
load_tasks()

# Running the Main Loop
root.mainloop()

