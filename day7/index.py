"""📢 Day 7 – Daily Python Challenge 🐍
🚀 Challenge:
Aaj ka challenge ek mini project hoga! Tumhe ek "To-Do List CLI App" banani hai jo user se tasks store kare, show kare aur delete bhi kar sake! 📝✅❌

🔥 Requirements:
⿡ Task Add Karein: User new task input kare aur list me add ho jaye.
⿢ Task Show Karein: Jo tasks add hue hain, unko show karein.
⿣ Task Delete Karein: User kisi task ko delete kar sake.
⿤ Quit Option: Program exit hone ka option bhi ho.

📌 Example:

"""
# Solution:

from os import system
from time import sleep

def add_task(tasks, task):
    tasks.append(task)
    print('Task added successfully!')
    sleep(1)
    system('cls')  # Use 'cls' for Windows

def show_tasks(tasks):
    if len(tasks) == 0:
        print('No tasks added yet!')
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
    sleep(2)
    system('cls')  # Use 'cls' for Windows

def delete_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print('Task deleted successfully!')
    else:
        print('Task not found!')
    sleep(2)
    system('cls')  # Use 'cls' for Windows

def main():
    tasks = []
    while True:
        print('1. Add Task')
        print('2. Show Tasks')
        print('3. Delete Task')
        print('4. Quit')
        choice = input('Enter your choice: ')
        system('cls')  # Use 'cls' for Windows
        if choice == '1':
            task = input('Enter task: ')
            add_task(tasks, task)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            task = input('Enter task to delete: ')
            delete_task(tasks, task)
        elif choice == '4':
            break
        else:
            print('Invalid choice!')
            sleep(1)
            system('cls')  # Use 'cls' for Windows

if __name__ == '__main__':
    main()
