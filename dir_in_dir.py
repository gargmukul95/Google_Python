# The new_directory function creates a new directory inside the current working directory,
# then creates a new empty file inside the new directory,
# and returns the list of files in that directory.
# Complete the function to create a file "script.py" in the directory "PythonPrograms".


import os
import csv


def new_directory(directory, filename):
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print("Dir already exists")
    # Before creating a new directory, check to see if it already exists
    # Create the new file inside of the new directory
    with open(os.path.join(directory, filename), "w") as file:
    # Return the list of files in the new directory
     return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

