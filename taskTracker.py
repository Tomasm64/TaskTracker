#modules
import sys
import json
import datetime
import os

#open task file
#with open('tasks.json','r') as file:
    #data = json.load(file)

argLen = len(sys.argv)
#Decide what to do based on number of arguments
if(argLen == 1):
    print("Please provide an argument")

elif(argLen == 2):
    # List all tasks
    if(sys.argv[1] == "list"):
        if(not os.path.isfile("tasks.json")):
            print("No task file found")
        else:
            with open("sampleTasks.json",'r') as file:
                data = json.load(file)
                taskList = data["tasks"]
                for t in taskList:
                    print(f"{t["id"]}: {t["description"]}")
                    print(f"Status: {t["status"]}")
                    print(f"Created: {t["createdAt"]}")
                    print(f"Updated: {t["updatedAt"]}")
                    print("-------------------------------------")
                

elif(argLen == 3):
    # User wants to add a task
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