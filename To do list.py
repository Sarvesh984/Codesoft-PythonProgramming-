import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.task_number = tk.Label(root, text="Tasks: 0")
        self.task_number.pack()

        self.new_task = tk.Entry(root, width=40)
        self.new_task.pack()

        self.add_task_button = tk.Button(root, text="Add task", command=self.add_task)
        self.add_task_button.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        self.delete_task_button = tk.Button(root, text="Delete task", command=self.delete_task)
        self.delete_task_button.pack()

    def add_task(self):
        task = self.new_task.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.new_task.delete(0, tk.END)
            self.task_number['text'] = f"Tasks: {len(self.tasks)}"
        else:
            messagebox.showwarning("Warning!", "You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
            self.tasks.pop(task_index)
            self.task_number['text'] = f"Tasks: {len(self.tasks)}"
        except:
            messagebox.showwarning("Warning!", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
