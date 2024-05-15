import pandas as pd
import openpyxl


# Design a printer to print projects, including the list of successors of each task, their early and late dates, and their criticality. 
# Use this printer to test both the data structures you designed in Task 1. and your loader.




def printDataframe(taskObjects, path):
    objects = []
    for task in taskObjects:
        predecessors = []
        successors = []
        for predecessor in task.getPredecessors():
            predecessors.append(predecessor.getActivity())
        for successor in task.getSuccessors():
            successors.append(successor.getActivity())
        objects.append((task.getType(), task.getActivity(), task.getDescription(), predecessors, successors, task.getEarlyStart(), 
                       task.getEarliestFinish(), task.getLatestStart(), task.getLatestFinish(), task.getCritical()))



    df = pd.DataFrame(objects,
        columns = ('Codes', 'Activity', 'Description', 'Predecessors', 'Successors', 'Early start', 'Early finish', 'Late start', 'Late finish', 'Critical')
    )
    print(df)
    df.to_excel(path)
    '''
    with pd.ExcelWriter(path) as writer:
        writer.book = openpyxl.load_workbook(path)
        df.to_excel(writer, sheet_name='new_sheet1')
    '''