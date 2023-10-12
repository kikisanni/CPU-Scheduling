
def schedule_priority(processes):
   # sorting the list based on priority
   return sorted(processes, key=lambda task: int(task[1]))
