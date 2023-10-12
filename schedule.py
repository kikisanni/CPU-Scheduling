from file_list import read_file
from schedule_fcfs import schedule_fcfs
from schedule_sjf import schedule_sjf
from schedule_priority import schedule_priority
from schedule_rr import allData
from times import *
from CPU import run


# this function calls all other functions from other files
def schedule(processes):

   print("\nThese are the processes to be executed:\n")

   #this function prints the tasks to be executed
   run(processes, slice)

   print("\n\n")

   print("FCFS SCHEDULING\n")

   #this function prints the turnaround time
   turnaround_time(schedule_fcfs(processes))
   #this function prints the average turnaround and average waiting time
   other_times(schedule_fcfs(processes))

   print("\n\n")


   print("SJF SCHEDULING\n")

   #this function prints the turnaround time
   turnaround_time(schedule_sjf(processes))
   #this function prints the average turnaround and average waiting time
   other_times(schedule_sjf(processes))

   print("\n\n")



   print("PRIORITY SCHEDULING\n")

   #this function prints the turnaround time
   turnaround_time(schedule_priority(processes))
   #this function prints the average turnaround and average waiting time
   other_times(schedule_priority(processes))

   print("\n\n")


   print("ROUND ROBIN SCHEDULING\n")

   #this function prints the turnaround time, the average turnaround time, and the average waiting time
   allData(processes, 10)
