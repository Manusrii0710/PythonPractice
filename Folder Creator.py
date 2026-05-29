import os
folder_name = input("Enter the name of the folder you want to create: ")
folders=folder_name.split(",")
for folder in folders:
    folder = folder.strip()
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"'{folder}' created successfully.")
    else:
        print(f"'{folder}' already exists.")