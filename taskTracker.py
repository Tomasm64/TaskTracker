# modules
import sys
import json
import datetime
import os

try:
    # Decide what to do based on number of arguments
    argLen = len(sys.argv)

    # No arguments
    if(argLen == 1):
        print("Please provide one of the following commands:\n")
        print("list")
        print("add")
        print("update")
        print("delete")
        print("mark-in-progress")
        print("mark-done")

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

        else:
            print("invalid command")
                    
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
        
        #Marking task as "in-progress"
        elif(sys.argv[1] == "mark-in-progress"):
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
                    if(taskList[i]["status"] == "in-progress"):
                        print(f"Task {taskID} is already in progress")
                    else:
                        taskList[i]["status"] = "in-progress"
                        taskList[i]["updatedAt"] = str(datetime.datetime.now())
                        updatedTasks = {
                            "tasks": taskList
                        }
                        with open("tasks.json",'w') as file:
                            json.dump(updatedTasks,file,indent=4)
                        print(f"Task ID {taskID} is now in progress")

        #Marking task as "in-progress"
        elif(sys.argv[1] == "mark-done"):
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
                    if(taskList[i]["status"] == "done"):
                        print(f"Task {taskID} is already done")
                    else:
                        taskList[i]["status"] = "done"
                        taskList[i]["updatedAt"] = str(datetime.datetime.now())
                        updatedTasks = {
                            "tasks": taskList
                        }
                        with open("tasks.json",'w') as file:
                            json.dump(updatedTasks,file,indent=4)
                        print(f"Task ID {taskID} is now done")

        # Listing tasks by status
        elif(sys.argv[1] == "list"):
            if(not os.path.isfile("tasks.json")):
                print("No task file found")
            else:
                taskStatus = sys.argv[2]
                with open("tasks.json",'r') as file:
                    data = json.load(file)
                    taskList = data["tasks"]
                    for t in taskList:
                        if(t["status"] == taskStatus):
                            print(f"{t["id"]}: {t["description"]}")
                            print(f"Status: {t["status"]}")
                            print(f"Created: {t["createdAt"]}")
                            print(f"Updated: {t["updatedAt"]}")
                            print("-------------------------------------")
        else:
            print("invalid command")

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

        else:
            print("invalid command")

    else:
        print("invalid number of arguments")

except Exception as e:
    print("Exception has occured: ", e)
                