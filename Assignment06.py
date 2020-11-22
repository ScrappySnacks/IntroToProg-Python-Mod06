# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# TWard,11.24.2020, Went back in time to modify code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "C:\\Users\\ld693a\\Desktop\\_PythonClass\\Mod06\\ToDoList.txt"  # Please see notes in assignment document for issues I am having with relative file location via command window.
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def ReadDataFromFile(strFileName, lstTable):   ### T. Ward conversion to snake case
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param lstTable: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        lstTable.clear() # clear current data
        file = open(strFileName, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            lstTable.append(row)
        file.close()
        return lstTable, 'Success'

    @staticmethod ### T. Ward modified to append lstTable given user input
    def AddDataToList(task, priority, lstTable):
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        return lstTable, 'Success'

    @staticmethod
    def RemoveDataFromlist(delTask, lstTable):  ### T. Ward modified to remove task
        i = 0  # Declare and initialize variable.  This will used a flag for telling the user the item does not exist.
        for row in lstTable:
            if delTask.strip() in row["Task"]:
                print("Now deleting forever and ever: " + delTask)
                lstTable.remove(row)
                i = i + 1  # If true, the script makes this a non-zero value.
        if i == 0: print("Task is not listed. Try again.")  # If i == 0, then the item was not found.  Tell the user.

    @staticmethod
    def WriteDataToFile(strFileName, lstTable):
        objFile = open(strFileName, "w")
        for row in lstTable:  ### T. Ward modified to save lstTable contents ################
            objFile.write(row["Task"] + ", " + row["Priority"] + "\n")
        objFile.close()
        return lstTable, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def PrintMenuTasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def PrintCurrentTasksInList(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def InputYesNoChoice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def InputPressToContinue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod ### T. Ward modified to take task and priority input from user for use later
    def InputNewTaskAndPriority():
        strTask = None
        strPriority = None
        strTask = str(input('Please enter a new task: ')).lower()
        strPriority = str(input('Please enter the priority: ')).lower()
        return strTask, strPriority

    @staticmethod
    def InputTaskToRemove():  ### T. Ward modified to take input from user on task to delete
        delTask = str(input('Please enter the task to delete: '))
        delTask = delTask.lower()
        return delTask


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.ReadDataFromFile(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.PrintCurrentTasksInList(lstTable)  # Show current data in the list/table
    IO.PrintMenuTasks()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  ### T. Ward modified to add tasks to existing lstTable
        task, priority = IO.InputNewTaskAndPriority()
        Processor.AddDataToList(task, priority, lstTable)
        # print(lstTable)  ### uncomment to perform check of input
        IO.InputPressToContinue(strStatus)
        continue  # to show the menu

    elif strChoice.strip() == '2':  ### T. Ward modified to remove an existing Task
        #print(lstTable)  ### uncomment to perform check of input
        task = IO.InputTaskToRemove()
        Processor.RemoveDataFromlist(task, lstTable)
        #print(lstTable)  ### uncomment to perform check of input
        IO.InputPressToContinue(strStatus)
        continue  # to show the menu

    elif strChoice.strip() == '3':  # Save Data to File
        strChoice = IO.InputYesNoChoice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.WriteDataToFile(strFileName,lstTable)
            IO.InputPressToContinue(strStatus)
        else:
            IO.InputPressToContinue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice.strip() == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.InputYesNoChoice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.ReadDataFromFile(strFileName, lstTable)  ### T. Ward modified to add Processor task
            IO.InputPressToContinue(strStatus)
        else:
            IO.InputPressToContinue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
