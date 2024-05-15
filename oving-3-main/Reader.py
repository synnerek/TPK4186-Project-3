import pandas as pd
from Task import Task


# The predecessor is known as before numbers (that appear just before) and the successor is known as after numbers (that appear just after).

# Function to read from excel file
def readFromExcel(file):
    df = pd.read_excel(file)
    print(df)
    return df


def readTasksFromExcel(file):
    df = pd.read_excel(file, sheet_name=0).dropna(subset=['Codes'], how='any')
    # Get the number of cells in column A
    num_cells = len(df['Codes'])
    taskObjects = []
    oldPredecessorList = []
    for row in range(num_cells):
        row_list = df.iloc[row].tolist()
        if row_list[0] == "Gate":
            task = Task(row_list[0], row_list[1], row_list[2],
                        (0, 0, 0), [])
        else:
            durlist = str(row_list[3]).strip(' () ').split(',')
            task = Task(row_list[0], row_list[1], row_list[2], [
                        int(durlist[0]), int(durlist[1]), int(durlist[2])], [])
        taskObjects.append(task)
        oldPredecessorList.append(str(row_list[4]).split(','))

    predecessorList = []

    for predecessorlist in oldPredecessorList:
        if len(predecessorlist) >= 2:
            element = [predecessorlist[0]]
            for i in range(len(predecessorlist)):
                if i != 0:
                    element.append(predecessorlist[i][1])
            predecessorList.append(element)
        else:
            predecessorList.append(predecessorlist)

    for i in range(len(taskObjects)):
        predecessors = predecessorList[i]
        if not predecessors[0] == 'nan':
            for predecessor in predecessors:
                for task in taskObjects:
                    if predecessor == task.getActivity():
                        taskObjects[i].addPredecessor(task)
    return taskObjects


# readFromExcel("/Users/emmastanger/Documents/Dokumenter - Emma’s MacBook Pro/OneDrive - NTNU/V23/TPK4186/oving-4/Warehouse.xlsx")
# readFromExcel("/Users/emmastanger/Documents/Dokumenter - Emma’s MacBook Pro/OneDrive - NTNU/V23/TPK4186/oving-4/Villa.xlsx")
# readTasksFromExcel("/Users/emmastanger/Documents/Dokumenter - Emma’s MacBook Pro/OneDrive - NTNU/V23/TPK4186/oving-4/Villa.xlsx")
