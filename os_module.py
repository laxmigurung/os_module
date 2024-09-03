"""
Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input). 
The script should display the total number of items (both files and directories) present in the specified directory. 
Bonus Modify your script to count the number of files and directories separately. Hint: use the os module"""


import os
# get the current working directory
cwd = os.getcwd() 
print(f"Your current working directory is {cwd}")

change_dir = input("Is the file you are looking for is in this directory? (yes/no): ")

while True:
    if change_dir == "yes":
        lst = os.listdir(cwd)
        print(f"the total number of files and directories under {cwd} is {len(lst)}.")
        break
    elif change_dir == "no":
        # navigate to root dir
        dir = '/home/ubuntu'
        user_input_file = input("Enter the file/dir path you wish to get the count of: ")
        # os.path.join(path,<filename>)
        new_path = os.path.join(dir,user_input_file)
        lst = os.listdir(new_path)
        print(f"the total number of files and directories under {new_path} is {len(lst)}.")
        break

    else:
        change_dir = input("Please enter yes or no only!!! Is the file you are looking for is in this directory? (yes/no): ")

