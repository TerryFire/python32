import csv
import os.path

from TaskDescriptors.CompletedDescriptor import CompletedDescriptor
from TaskDescriptors.DescriptionDescriptor import DescriptionDescriptor
from TaskDescriptors.TitleDescriptor import TitleDescriptor
from TaskManagerDescriptors.FileNameDescriptor import FileNameDescriptor


class Task:
    title = TitleDescriptor()
    description = DescriptionDescriptor()
    completed = CompletedDescriptor()

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False


class TaskManager:
    filename = FileNameDescriptor()

    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks()

    def show_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not completed"
            print(f"{index}. {task.title} ({status})")

    def edit_task(self, index: int, title: str, description: str):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.title = title
            task.description = description
            self.save_tasks()
        else:
            print("Unknown option")

    def delete_task(self, index: int):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            self.save_tasks()
        else:
            print("Unknown option")

    def complete_task(self, index: int):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.completed = True
            self.save_tasks()
        else:
            print("Unknown option")

    def import_from_file(self, import_filename):
        try:
            with open(import_filename, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    title, description, completed = row
                    task = Task(title, description)
                    task.completed = bool(int(completed))
                    self.tasks.append(task)
                self.save_tasks()
                print(f"Tasks imported from file {import_filename}")
        except FileNotFoundError:
            print(f"File not found by name: {import_filename}")

    def export_from_file(self, export_filename):
        try:
            with open(export_filename, "w", newline="") as f:
                writer = csv.writer(f)
                for task in self.tasks:
                    writer.writerow([task.title, task.description, int(task.completed)])

                print(f"Tasks exported in file {export_filename}")
        except FileNotFoundError:
            print(f"File not found by name: {export_filename}")

    def save_tasks(self):
        try:
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                for task in self.tasks:
                    writer.writerow([task.title, task.description, int(task.completed)])

        except FileNotFoundError:
            print(f"File not found by name: {self.filename}")

    def load_tasks(self):
        if os.path.exists(os.path.normpath(self.filename)):
            with open(self.filename, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    title, description, completed = row
                    task = Task(title, description)
                    task.completed = bool(int(completed))
                    self.tasks.append(task)
                self.save_tasks()

    def delete_tasks_withstatus(self, status: bool):
        self.tasks = [task for task in self.tasks if task.completed != status]
        self.save_tasks()
        print(f"All {'' if status else 'not'} completed tasks deleted")

    def menu(self):
        while True:
            print('''
            \nTask Manager
            1. Add task
            2. Show Tasks
            3. Edit task
            4. Delete task
            5. Mark tasks as completed
            6. Import all tasks from file
            7. Export tasks to file
            8. Delete all completed tasks
            9. Delete all uncompleted tasks
            10. Exit
            ''')

            choise = input("Choose option: ")

            if choise == "1":
                title = input("Task name: ")
                description = input("Enter description: ")

                self.add_task(title, description)
            elif choise == "2":
                self.show_tasks()
            elif choise == "3":
                index = int(input("Enter index: "))
                title = input("Enter task title: ")
                description = input("Enter description: ")
                self.edit_task(index, title, description)
            elif choise == "4":
                index = int(input("Enter index: "))
                self.delete_task(index)
            elif choise == "5":
                index = int(input("Enter index: "))
                self.complete_task(index)
            elif choise == "6":
                import_filename = os.path.normpath(input("Enter path to task file (.csv): "))
                self.import_from_file(import_filename)
            elif choise == "7":
                export_filename = os.path.normpath(input("Enter path to save task file (.csv): "))
                self.export_from_file(export_filename)
            elif choise == "8":
                self.delete_tasks_withstatus(True)
            elif choise == "9":
                self.delete_tasks_withstatus(False)
            elif choise == "10":
                break
            else:
                print("Choose option: ")
