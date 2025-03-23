""" Challeng create TodoList App """

class Task:
    def __init__(self,title, completed =False):
        self.title = title
        self.completed = completed
    def mark_done(self):
        self.completed = True
     
    def display(self):
        status = "Completed" if self.completed else "Not completed"
        return f"the status of taks : {self.title} status :{status} "

class TodoList :
    def __init__(self):
        self.task = []
    
    def add_task (self,title):
        self.task.append(title)
    
    def list_task(self):
        for task in self.task:
            status = "compled" if task.completed else "Not completed"
            print(f"task : {task.title} and status :{status}")
        return f"No Task is found"
    def complete_task(self,title):
        for task in self.task:
            if task.title.lower()==title.lower():
                task.mark_done()
                return f"the task is marked done"
        return f"not found task or already is completed"

task1 = Task("Running")
task2 =Task("Assigmnet")

todolist = TodoList()

todolist.add_task(task1)
todolist.add_task(task2)

todolist.list_task()
todolist.complete_task("Running")
print("After completing")
todolist.list_task()