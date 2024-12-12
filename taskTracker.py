#modules
import sys
import json
import datetime

#open task file
#with open('tasks.json','r') as file:
    #data = json.load(file)

argLen = len(sys.argv)
if(argLen == 3):
    # User wants to add a task
    if(sys.argv[1] == "add"):
        taskDesc = sys.argv[2]
        taskID = 1
        taskStatus = "todo"
        taskCreated = str(datetime.datetime.now())
        taskUpdated = str(datetime.datetime.now())
        
        #Creating JSON object
        newTask = {
            "id": taskID,
            "description": taskDesc,
            "status": taskStatus,
            "createdAt": taskCreated,
            "updatedAt": taskUpdated
        }

        #Write to JSON file
        with open('tasks.json','w') as file:
            json.dump(newTask,file,indent=4)
        
        print(f"Task added successfuly (ID: {taskID})")

'''
argLen = len(sys.argv)
print("Number of Arguments: ", argLen)

for i in sys.argv:
    print(i)
'''