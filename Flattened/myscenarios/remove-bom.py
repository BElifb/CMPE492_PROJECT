import os
import sys


dir_path = "Flattened\myscenarios"
counter = 1
for filename in os.listdir(dir_path):
    if filename != "batch-rename.py":
        print("Removing BOM: " + filename + "...")
        #size = len(os.path.splitext(filename)[0])
        #new_filename = os.path.splitext(filename)[0][:size-4] + ".json"
        filename = oldFileName = os.path.join(dir_path, filename)
        # fp = open(filename,'r')
        # s = fp.read()
        # u = s.decode('utf-8-sig')
        # s = u.encode('utf-8')
        # print(fp.encoding)  
        # fp.close()
        # fp.open(filename, 'w')
        # fp.write(s)
        s = open(filename, mode='r', encoding='utf-8-sig').read()
        open(filename, mode='w', encoding='utf-8').write(s)
