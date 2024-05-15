from Task import Task

class TaskList(object):
    def __init__(self, taskList: list): 
        self.taskList = taskList

    def getTaskList(self):
        return self.taskList
    
    def setTaskList(self, taskList):
        self.taskList = taskList
    
    def __str__(self):
        return f"Type: {self.taskList}"
