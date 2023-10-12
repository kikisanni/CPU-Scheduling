
import sys
from file_list import read_file
from schedule import schedule
from error_checking import data



def main():

   #tasks = []

   file = sys.argv[1]

   processes = read_file(file)

   error = data(processes)


   # checking to see if there is an error
   if error != 0:
      print("Error: Invalid Input") # we print a statement to show that there is an error
      exit() # and we terminate the whole process by exiting
   
   else:
      schedule(processes) # if ther is no error, we execute the tasks

   

if __name__ == "__main__":
   main()
