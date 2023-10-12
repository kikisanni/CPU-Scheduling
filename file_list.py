mport string


#function to read a file, and get the list of processes
def read_file(file):

   taskList = []

   # open and read the file containing the processes
   with open(file, "r") as fin:

      # read each line of the file and put them into a list
      fin = fin.readlines()

      for task in fin:
         #remove the punctuations that exst within each task in the list
         task = task.translate(str.maketrans("", "", string.punctuation))


         #split each task in the list on whitespace in order to have the process name, priority, and burst
         task = task.strip().split()

         #then append each task to a new list
         taskList.append(task)


   return taskList # we return a list of lists

