import pandas as pd
import re
import numpy as np
import random
from Task import Task


# Function to calculate early dates
# 1. Start with the list of all tasks.
# 2. While it remains a task in the list,
# – Find a task in the list whose all predecessors are not in the list.
# – Remove this task from the list.
# – Calculate the early dates for this task.

def calculate_early_dates(tasks):
    for task in tasks:
        if task.getActivity() == "Start":
            task.setEarlyStart(0)
            task.setEarliestFinish(0)
        elif task.getActivity() == "End":
            es = [0]
            for p in task.getPredecessors():
                es.append(p.getEarliestFinish())
            task.setEarlyStart(max(es))
            task.setEarliestFinish(max(es))
        else:
            es = [0]
            for p in task.getPredecessors():
                es.append(p.getEarliestFinish())
            task.setEarlyStart(max(es))
            task.setEarliestFinish(int(max(es))+int(task.getDays()))

# Function to calculate late dates
# 1. Start with the list of all tasks.
# 2. While it remains a task in the list,
# – Find a task in the list whose all successors are not in the list.
# – Remove this task from the list.
# – Calculate the late dates for this task.

def successor_exist(t, task_list):
    if len(t.getSuccessors()) == 0:
        return False
    else:
        for s in t.getSuccessors():
            for task in task_list:
                if s == task:
                    return True


def get_early_completion_dates(tasks):
    early_completion_dates = []
    for task in tasks:
        early_completion_dates.append(task.getEarliestFinish())
    return early_completion_dates


def find_successor_with_min_late_start(task, task_list):
    min_start_date = float('inf')
    for successor in task.successors:
        for task in task_list:
            if successor == task:
                if task.getLatestStart() < min_start_date:
                    min_start_date = task.getLatestStart()
    return min_start_date


def calculate_late_days(tasks: list, exp_dur=None):
    copy_tasks = tasks.copy()
    early_completion_dates = get_early_completion_dates(tasks)
    totalduration = max(
        [date for date in early_completion_dates if date is not 0] + [float('-inf')])
    while copy_tasks:
        for task in reversed(copy_tasks):
            if not successor_exist(task, copy_tasks):
                copy_tasks.remove(task)
                if len(task.getSuccessors()) == 0 or task.getSuccessors()[0] == 'Gate':
                    task.setLatestStart(totalduration)
                    task.setLatestFinish(totalduration)
                else:
                    min_late_start = find_successor_with_min_late_start(
                        task, tasks)
                    task.setLatestFinish(min_late_start)
                    if exp_dur == None:
                        if task.getActivity() == "Start":
                            task.setLatestStart(0)
                            task.setLatestFinish(0)
                        else:
                            task.setLatestStart(
                                task.getLatestFinish() - task.days)
                    else:
                        task.setLatestStart(
                            task.getLatestFinish() - task.expdur)


def calcLateDates(taskList: list):

    # Helper function to check if all successors of a task are already in the list
    def all_successors_in_list(task, task_list):
        for successor in task.getSuccessors():
            for t in task_list:
                if successor == t:
                    return False
        return True

    # Initialize the list of tasks with their early start and finish times
    task_list = []
    for task in taskList:
        task.setLatestFinish(0)
        task.setLatestStart(0)
        if (task.getActivity() == "Start") or (task.getActivity() == "End"):
            task.days = 0
        task_list.append(task)

    task_list.reverse()

    # The late completion date of a task is the maximum of the late start dates of its successors,
    # and the project duration if it has no successor.
    # The late start date of a task is its late completion date minus its duration.
    while len(task_list) > 0:
        # for hver task i den gjenstående listen
        for task in task_list:
            # sjekker om alle successorene er i listen
            if all_successors_in_list(task, task_list):
                task_list.remove(task)
                startDatesSuccessors = []
                finishDatesSuccessors = []
                if len(task.getSuccessors()) > 0:
                    for successor in task.getSuccessors():
                        startDatesSuccessors.append(successor.getLatestStart())
                        finishDatesSuccessors.append(
                            successor.getLatestFinish())
                    task.setLatestFinish(max(startDatesSuccessors))
                    task.setLatestStart(
                        int(task.getLatestFinish()) - int(task.getDays()))
                else:
                    task.setLatestFinish('duration')
                break


