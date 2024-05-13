import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []
 
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"Task": task, "Status": "Pending"})
        clear_entries()
        show_tasks()
        save_tasks_to_file() 
        messagebox.showinfo("Task Added", "Task added successfully!")
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def prompt_update_task():
    index = simpledialog.askinteger("Update Task", "Enter the index of the task you want to update")
    if index is not None and 1 <= index <= len(tasks):
        selected_task = tasks[index - 1]

        update_window = tk.Toplevel(root)
        update_window.title("Update Task")

        task_label = tk.Label(update_window, text="Task")
        task_label.pack()
        task_entry = tk.Entry(update_window, width=30, font=("Times", 12), bg="black", fg="white")
        task_entry.insert(0, selected_task["Task"])
        task_entry.pack(pady=5)

        def update_task():
            selected_task["Task"] = task_entry.get()
            show_tasks()
            update_window.destroy()
            save_tasks_to_file()  
            messagebox.showinfo("Task Updated", "Task updated successfully!")

        update_button = tk.Button(update_window, text="Update Task", command=update_task, background="#20b35a")
        update_button.pack(pady=5)
    else:
        messagebox.showwarning("Invalid Index", "Please enter a valid index.")

def prompt_delete_task():
    index = simpledialog.askinteger("Delete Task", "Enter the index of the task you want to delete")
    if index is not None and 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        clear_entries()
        show_tasks()
        save_tasks_to_file()  
        messagebox.showinfo("Task Deleted", "Task deleted successfully!")
    else:
        messagebox.showwarning("Invalid Index", "Please enter a valid index.")

def prompt_toggle_status():
    index = simpledialog.askinteger("Toggle Status", "Enter the index of the task you want to toggle status")
    if index is not None and 1 <= index <= len(tasks):
        task = tasks[index - 1]
        task["Status"] = "Completed" if task["Status"] == "Pending" else "Pending"
        show_tasks()
        save_tasks_to_file()  
    else:
        messagebox.showwarning("Invalid Index", "Please enter a valid index.")

def clear_entries():
    task_entry.delete(0, tk.END)

def show_tasks():
    tasks_text.delete(1.0, tk.END)
    for idx, task in enumerate(tasks, start=1):
        tasks_text.insert(tk.END, f"{idx}. Task: {task['Task']}\n   Status: {task['Status']}\n\n")

def save_tasks_to_file(filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"Task: {task['Task']}\nStatus: {task['Status']}\n\n")

def clear_all_tasks():
    tasks.clear()
    show_tasks()
    messagebox.showinfo("Tasks Cleared", "All tasks have been cleared!")
    save_tasks_to_file()  

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x600")  
root.resizable(False, False)
root.configure(background="#051f1f")

title_label = tk.Label(root, text="ToDo List", width=25, font=("Times", 20, "bold"), bg="#C70039", fg="white")
title_label.pack(pady=20)

task_label = tk.Label(root, text="Enter Task", font=("Times", 14, "bold"), bg="#1877F2", fg="white")
task_label.pack()
task_entry = tk.Entry(root, width=30, font=("Times", 14), bg="white", fg="black")
task_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", font=("Times", 12, "bold"), command=add_task, bg="green", fg="white")
add_button.grid(row=0, column=0, padx=5, pady= 10)

update_button = tk.Button(button_frame, text="Update Task", font=("Times", 12, "bold"), command=prompt_update_task, bg="blue", fg="white")
update_button.grid(row=0, column=1, padx=5, pady= 10)

delete_button = tk.Button(button_frame, text="Delete Task", font=("Times", 12, "bold"), command=prompt_delete_task, bg="red", fg="white")
delete_button.grid(row=1, column=0, padx=5, pady= 10)

status_button = tk.Button(button_frame, text="Toggle Status", font=("Times", 12, "bold"), command=prompt_toggle_status, bg="purple", fg="white")
status_button.grid(row=1, column=1, padx=5, pady= 10)

clear_button = tk.Button(button_frame, text="Clear All Tasks", font=("Times", 12, "bold"), command=clear_all_tasks, bg="darkorange", fg="white", width=20)
clear_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

task_list = tk.Label(root, text="My Tasks", width=30, font=("Times", 16, "bold"), bg="brown", fg="white")
task_list.pack(padx=5, pady= 5)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_text = tk.Text(root, font=("Times", 14), bg="white", fg="black", yscrollcommand=scrollbar.set)
tasks_text.pack(expand=True, fill="both")
scrollbar.config(command=tasks_text.yview)

root.mainloop()
