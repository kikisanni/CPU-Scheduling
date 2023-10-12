from file_list import read_file

# function to calculate the turnaround time of each process
def turnaround_time(processes):

   waiting_time = 0 # set waiting_time to 0

   for task in processes:
      name, priority, burst = task[0], task[1], task[2] 

      #slice = burst 

      #turnaround time is the sum of waiting time and burst time
      turnAround_time = waiting_time + int(burst) 

      #printing each process along with their turnaround time and waiting time
      print(f'Process {name} arrived at time 0 with a waiting time of {waiting_time}MS and ran for {burst}MS. It had a turn-around time of {turnAround_time}')

      waiting_time = turnAround_time


# function to0 calculate the average turnaround time
def avg_turnaround(processes):

   store = [] # a list to store the turnaround time for each process
   waiting_time = 0 # setting the waiting time of the first process to 0

   for task in processes:
      turnaround = waiting_time + int(task[2]) # turnaround time is the sum of waiting time and burst
      store.append(turnaround) # appending the turnaroubd time to the list
      waiting_time = turnaround # setting waiting time to the turnaround for the next process
      # the turnaround time of a process is the waiting time of the next process


   avg = sum(store) / len(store) #getting the average

   return avg


#function to calculate the average waiting time 
def avg_waiting(processes):

   store = [] # a list to store all the waitint times
   waiting_time = 0

   for i in range(len(processes) - 1):
      task = processes[i]
      waiting_time += int(task[2])
      store.append(waiting_time) # appendng each waiting time to the list

   avg = sum(store) / len(processes) # getting the average

   return avg


# function to print out the average waiting time and average turnaround time
def other_times(processes):

   print(f'The average turnaround time is {avg_turnaround(processes)}MS and average waiting time is {avg_waiting(processes)}MS') 
