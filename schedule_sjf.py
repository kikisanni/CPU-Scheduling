def schedule_sjf(processes):
   #sorting the list based on burst
   return sorted(processes, key=lambda task: int(task[2]))
