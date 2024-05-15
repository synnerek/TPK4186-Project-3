import random
import pandas as pd
import numpy as np
import random


# Youtubevideo
# https://www.youtube.com/watch?v=UXPeO2d9nSs


class Task(object):
    def __init__(self, type: str, activity: str, description: str, durations: list, predecessors: list):
        # må legge til minimum, expected and maximum duration.
        self.type = type
        self.activity = activity
        self.description = description
        self.durations = durations
        self.predecessors = predecessors
        self.successors = []
        self.duration = 0
        self.earlyStart = 0
        self.earliestFinish = 0
        self.latestStart = 0
        self.latestFinish = 0
        self.slack = 0
        self.critical = ''

        self.mindur = int(durations[0])
        self.maxdur = int(durations[2])
        self.expdur = int(durations[1])

        self.distr = durations

        e_duration = durations[1]*1  # r=1
        if e_duration < durations[0]:
            self.mindur = e_duration
        elif e_duration > durations[2]:
            self.maxdur = e_duration
        else:
            self.expdur = e_duration

        self.days = random.triangular(self.mindur, self.expdur, self.maxdur)

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getActivity(self):
        return self.activity

    def setActivity(self, activity):
        self.activity = activity

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getDuration(self):
        return self.duration

    def getMindur(self):
        return self.mindur

    def getMiddur(self):
        return self.middur

    def getMaxdur(self):
        return self.maxdur

    def setDuration(self, duration):
        self.duration = duration

    def getDurations(self):
        return self.durations

    def setDurations(self, durations):
        self.durations = durations

    def getPredecessors(self):
        return self.predecessors

    def setPredecessors(self, predecessors):
        self.predecessors = predecessors

    def addPredecessor(self, task):
        task.addSuccesor(self)
        self.predecessors.append(task)

    def getSuccessors(self):
        return self.successors

    def setSuccessors(self, successors):
        self.successors = successors

    def addSuccesor(self, task):
        self.successors.append(task)

    def getDays(self):
        return self.days

    def setDays(self, days):
        self.days = days

    def getEarlyStart(self):
        return self.earlyStart

    def setEarlyStart(self, earlyStart):
        self.earlyStart = earlyStart

    def getEarliestFinish(self):
        return self.earliestFinish

    def setEarliestFinish(self, earliestFinish):
        self.earliestFinish = earliestFinish

    def getLatestStart(self):
        return self.latestStart

    def setLatestStart(self, latestStart):
        self.latestStart = latestStart

    def getLatestFinish(self):
        return self.latestFinish

    def setLatestFinish(self, latestFinish):
        self.latestFinish = latestFinish

    def getSlack(self):
        return self.slack

    def setSlack(self, slack):
        self.slack = slack

    def computeSlack(self):
        slack = self.latestFinish - self.earliestFinish
        if slack > 0:
            self.critical = "NO"
        else:
            self.critical = "YES"

    def getCritical(self):
        return self.critical

    def setCritical(self, critical):
        self.computeSlack()
        self.critical = critical

    def __repr__(self):
        # \nPredecessors: {self.predecessors}"
        return f"\nType: {self.type} \nActivity: {self.activity} \nDescription: {self.description} \nDurations: {self.durations} \nPredecessors: {self.predecessors}"
