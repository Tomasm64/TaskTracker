# Task Tracker

## Description
A CLI program for keeping track of tasks. Based on these instructions: https://roadmap.sh/projects/task-tracker

### Languages
* Python
* JSON

### Required Software
* Python 3.10 or later

## Installation
"taskTracker.py" can be downloaded on its own, or you can clone the whole repository to your machine.

## Usage
These instructions assume the user has knowledge running python applications from the command line.

There are six possible functions when using this program. The examples shown use Windows git bash for execution.

### add
This adds a task to the file "tasks.json". If the file does not exist, it will be created. It generates a unique ID number that increments from the ID of the last task on the list.

````py taskTracker.py add "Wash Dishes"````