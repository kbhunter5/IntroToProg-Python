# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Kellen Hunter, 08/10/20 ,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strRemoveTask = "" # Remove a task
strTask = "" # Adding a new task
strPriority = "" # Priority of a task

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# List to File

objFile = open(strFile, "w")
dicRow = {"task": "Vaccum", "priority": "1"}
objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
dicRow = {"task": "Clean Kitchen", "priority": "2"}
objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
dicRow = {"task": "Homework", "priority": "3"}
objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
dicRow = {"task": "Laundry", "priority": "4"}
objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
dicRow = {"task": "Shower", "priority": "5"}
objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        #Show current Data
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"task":lstRow[0], "priority": lstRow[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter a task: ")
        strPriority = input("Enter an priority: ")
        dicRow = {"task": strTask, "priority": strPriority.strip()}
        lstTable.append(dicRow)
        #for objRow in lstTable:
        print(lstTable)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        print(lstTable)
        strRemoveTask = str(input("Which task would you like to remove from your list?"))
        for dicRow in lstTable:
            if dicRow["task"] == strRemoveTask:
                lstTable.remove(dicRow)
                print("The Selected task has been removed from your list")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", 'w')
        for dicRow in lstTable:
            objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
        objFile.close()
        print("Data has been saved to ToDoList.txt")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Program has ben exited")
        break  # and Exit the program