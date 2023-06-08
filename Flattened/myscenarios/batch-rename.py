import os
import sys


dir_path = "Flattened\myscenarios"
counter = 1
for filename in os.listdir(dir_path):
    if filename != "batch-rename.py":
        print("Renaming: " + filename + "...")
        #size = len(os.path.splitext(filename)[0])
        #new_filename = os.path.splitext(filename)[0][:size-4] + ".json"
        new_filename = os.path.splitext(filename)[0] + ".json"
        oldFileName = os.path.join(dir_path, filename)
        newFileName = os.path.join(dir_path, new_filename)
        os.rename(oldFileName, newFileName)

