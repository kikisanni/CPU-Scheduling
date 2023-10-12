import string

# function to check if the length of a process is 3
# each process has to include the process name, priority, and burst
def task_length(processes):

    error = 0  # we set error to 0 by default

    for task in processes:
        if len(task) != 3: # checking if the length of the process is 3
            error += 1 # if length is not 3, we add one to error

    
    # if error is 0, it means length is 3 otherwise length is not 3
    if error != 0:
       return 1  # return 1 if there is an erro
    
    else:
        return 0 # else return 0


# function to check if priority is a number
def priority_isNum(processes):

    error = 0 # set error to 0

    for task in processes:
        #using try and except block to capture any error
        try:
            priority = task[1]

            if not priority.isnumeric(): # if prirority is not numeric, we  add 1 to error
                error += 1
        
        # this except block is used to capture IndexError particularly
        # in the case where priority is a punctuation e.g "?", it produces an IndexError
        # so instead of the program throwing an error, we capture it, and make it add 1 to error
        except:
            error += 1 
    
    
    # if error is not 0, it means priority is not numeric
    if error != 0:
        return 1
        
    else:
        return 0



# function to check if burst is a number
def burst_isNum(processes):

    error = 0 # set error to 0

    for task in processes:
        try:
            burst = task[2]
            
            if not burst.isnumeric():
                error += 1
        
        # this except block is used to capture IndexError particularly
        # in the case where priority is a punctuation e.g "?", it produces an IndexError
        # so instead of the program throwing an error, we capture it, and make it add 1 to error
        except:
            error += 1
        
    
    # if error is not 0, ot means burst is not a number
    if error != 0:
        return 1
        
    else:
        return 0
    

#function to check if the process name is a string
def name_isStr(processes):

    error = 0 # set error to 0 by default

    for task in processes:
        try:
            name = task[0]
        
            if not isinstance(name, str):
                error += 1
        
        # this except block is used to capture IndexError particularly
        # in the case where priority is a punctuation e.g "?", it produces an IndexError
        # so instead of the program throwing an error, we capture it, and make it add 1 to error
        except:
            error += 1

    #if error is not 0, it means name is not a string
    if error != 0:
        return 1
        
    else:
        return 0
    

# function to collect all the results and add the number of errors we have   
def data(processes):
    total_error = 0

    total_error = task_length(processes) + priority_isNum(processes) + burst_isNum(processes) + name_isStr(processes)
    
    return total_error
