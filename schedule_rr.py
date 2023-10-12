# find the waiting time for each process
def waitingTime(processes, wt, quantum):

    n = len(processes)

    # create a list to store the remaining burst time
    rem = [0] * n 

    for i in range(n):
        rem[i] = int(processes[i][2]) # copy the burst time into rem for updating purpose
    
    # current time
    time = 0
    # print(rem)

    # traverse the list of processes until done is True
    while(1):
        done = True

        # traverse the list one after the other repeatedly
        for i in range(n):
            # if burst is greater than 0, then we we check if itis greater or lesser than quantum
            if rem[i] > 0:
                done = False

                # check if burst is greater than quantum
                if rem[i] > quantum:
                    # if it is true, add quantum to our current time
                    time += quantum

                    # then update the burst time in the list by deducting quantum from it
                    rem[i] -= quantum
            
                # if burst time is lesser than quantum
                else:
                    # then we don't need to add quantum to current time instead add the burst time
                    time = time + rem[i]
                    # then we append the waiting time by deducting the burst time from the turnaround time
                    wt[i] = time - int(processes[i][2])
                    # since the process is complete, we make its remaining burst time 0
                    rem[i] = 0
        
        # if all processes are done, we break out of the while loop
        if done == True:
            break

# function to calculate the turnaround time
def turnAroundTime(processes, wt, tat):
    n = len(processes)

    for i in range(n):
        # the formula for finding turnaround time is burst time + waiting time
        tat[i] = int(processes[i][2]) + wt[i]


# function to collect all data
def allData(processes, quantum):
    n = len(processes)

    # defining the lists
    wt = [0] * n # list of waiting time for each process
    tat = [0] * n # list of turnaround time for each process

    waitingTime(processes, wt, quantum) # calling the function for waiting time 
    turnAroundTime(processes, wt, tat) #  calling the function for turnaround time

    tot_wt = 0
    tot_tat = 0

    for i in range(n):
        tot_wt = tot_wt + wt[i] # calculating the total waiting time
        tot_tat = tot_tat + tat[i] # calculating the total turnaround time

        # printing the waiting time and turnaround time for each process 
        print(f'{processes[i][0]} arrived at 0 with a waiting time of {wt[i]} and ran for {processes[i][2]}. It had a turn-around time of {tat[i]}')

    # printing the average waiting time and turnaround time
    print(f'The average turnaround time is {tot_tat / n}MS and average waiting time is {tot_wt / n}MS')





# REFERENCE
# GeeksforGeeks. 2022. Program for Round Robin scheduling | Set 1 - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/program-round-robin-scheduling-set-1/> [Accessed 31 March 2022].
