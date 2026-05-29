import os
folders = ["Projects", "Notes", "Assignments", "Python", "MATLAB"]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(folder, "created")
    else:
        print(folder, "already exists")