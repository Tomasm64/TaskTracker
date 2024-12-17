#modules
import sys
import json
import datetime
import os

#open task file
#with open('tasks.json','r') as file:
    #data = json.load(file)

argLen = len(sys.argv)
# Decide what to do based on number of arguments

# No arguments
if(argLen == 1):
    print("Please provide an argument")

# 1 argument
elif(argLen == 2):
    # Listing all tasks
    if(sys.argv[1] == "list"):
        if(not os.path.isfile("tasks.json")):
            print("No task file found")
        else:
            with open("tasks.json",'r') as file:
                data = json.load(file)
                taskList = data["tasks"]
                for t in taskList:
                    print(f"{t["id"]}: {t["description"]}")
                    print(f"Status: {t["status"]}")
                    print(f"Created: {t["createdAt"]}")
                    print(f"Updated: {t["updatedAt"]}")
                    print("-------------------------------------")
                
# 2 arguments
elif(argLen == 3):
    # Adding a task
    if(sys.argv[1] == "add"):
        taskDesc = sys.argv[2]
        taskID = 1
        taskStatus = "todo"
        taskCreated = str(datetime.datetime.now())
        taskUpdated = str(datetime.datetime.now())
        
        #Defining task list
        tasks = {
            "tasks": []
        }
        if(os.path.isfile("tasks.json")):
            with open("tasks.json","r") as file:
                tasks = json.load(file)
                #generate new id based on id of last entry
                taskID = 1 + tasks["tasks"][-1]["id"]

        #Creating JSON object
        newTask = {
            "id": taskID,
            "description": taskDesc,
            "status": taskStatus,
            "createdAt": taskCreated,
            "updatedAt": taskUpdated
        }
        tasks["tasks"].append(newTask)
        #Write to JSON file
        with open("tasks.json",'w') as file:
            json.dump(tasks,file,indent=4)

        print(f"Task added successfuly (ID: {taskID})")

    # Deleting a task
    elif(sys.argv[1] == "delete"):
        taskID = sys.argv[2]
        taskFound = False
        if(not os.path.isfile("tasks.json")):
            print("No task file found")
        else:
            with open("tasks.json",'r') as file:
                data = json.load(file)
                taskList = data["tasks"]
                for i in range(0,len(taskList)):
                    if str(taskList[i]["id"]) == str(taskID):
                        taskFound = True
                        break
            
            if not taskFound:
                print("Task ID not found")
            else:
                confirm = input(f"Are you sure you want to delete task {taskID}: {taskList[i]["description"]}? (y/n)\n")
                if(confirm == 'y' or confirm == 'Y'):
                    taskList.pop(i)
                    updatedTasks = {
                        "tasks": taskList
                    }
                    with open("tasks.json",'w') as file:
                        json.dump(updatedTasks,file,indent=4)
                    print(f"Task ID {taskID} deleted successfully")

# 3 arguments
elif(argLen == 4):
    # Updating the name of a task
    if(sys.argv[1] == "update"):
        taskID = sys.argv[2]
        newDesc = sys.argv[3]
        taskFound = False
        if(not os.path.isfile("tasks.json")):
            print("No task file found")
        else:
            with open("tasks.json",'r') as file:
                data = json.load(file)
                taskList = data["tasks"]
                for i in range(0,len(taskList)):
                    if str(taskList[i]["id"]) == str(taskID):
                        taskList[i]["description"] = newDesc
                        taskList[i]["updatedAt"] = str(datetime.datetime.now())
                        taskFound = True
                        break
            if not taskFound:
                print("Task ID not found")
            else:
                updatedTasks = {
                    "tasks": taskList
                }
                with open("tasks.json",'w') as file:
                    json.dump(updatedTasks,file,indent=4)
                print(f"Task ID {taskID} updated successfully")
                