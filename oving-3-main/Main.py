import Reader
from Task import Task
import utils
from TaskList import TaskList
import Printer


taskObjects = Reader.readTasksFromExcel(
    "/Users/emmastanger/Documents/Dokumenter - Emma’s MacBook Pro/OneDrive - NTNU/V23/TPK4186/oving-4/oving-3-1/Warehouse.xlsx")


'''
for task in taskObjects:
    plist = []
    for p in task.getPredecessors():
        plist.append(p.getActivity())
    slist = []
    for s in task.getSuccessors():
        slist.append(s.getActivity())
    print(f"{task.getActivity()}:\nPredecessors: {plist}\nSuccessors: {slist} \n")
'''

# utils.computeSuccessors(taskObjects)
print("\nEARLIEST FINISH DATE")
for task in taskObjects:
    print(f"{task.getActivity()}: {task.getEarliestFinish()}")

utils.calculate_early_dates(taskObjects)

print("\nEARLIEST FINISH DATE AFTER calculate_early_dates")
for task in taskObjects:
    print(f"{task.getActivity()}: {task.getEarliestFinish()}")


print("\LATEST FINISH DATE ")
for task in taskObjects:
    print(f"{task.getActivity()}: {task.getLatestFinish()}")

utils.calculate_late_days(taskObjects)

print("\LATEST FINISH DATE AFTER calculate_late_days")
for task in taskObjects:
    print(f"{task.getActivity()}: {task.getLatestFinish()}")

for task in taskObjects:
    task.computeSlack()

Printer.printDataframe(taskObjects, 'Warehouse_test.xlsx')
