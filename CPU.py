#!/usr/bin/env python3


def run(allTasks, slice):


   for task in allTasks:
      name, priority, burst = task[0], task[1], task[2]
      slice = burst

      print("Running task = {} {} {} for {} units.".format(name, priority, burst, slice)) 

