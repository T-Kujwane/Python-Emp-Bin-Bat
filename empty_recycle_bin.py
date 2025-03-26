# Set echo off
import logging
logging.disable(logging.CRITICAL)

# Empty Windows Recycle Bin on execution
import subprocess, sys;

# Importing Required Libraries
try:
    import winshell
except ImportError:
    print("The 'winshell' module is not installed. Please install it using 'pip install winshell'.")
    sys.exit(1);

# access recycle bin
recycle_bin = winshell.recycle_bin();

has_cleared_recycle_bin = False;

recycle_bin_items_count = len(list(recycle_bin));

if recycle_bin_items_count > 0:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False);
    has_cleared_recycle_bin = True;

# Importing libraries required to clean the D: drive
import os
import shutil

# Define the path to the D: drive
d_drive_path = 'D:/'

has_cleared_d_drive = False

# Count the number of items in the D: drive
d_drive_items_count = sum(len(files) for _, _, files in os.walk(d_drive_path))
d_drive_items_count -= 1  # Subtract 1 to exclude the root directory

# If the D: drive is not empty, clear it
if d_drive_items_count > 0:
    
    # Walk through all directories and files in the D: drive
    for root, dirs, files in os.walk(d_drive_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)  # Delete the file
            except Exception as e:
                print(f'Failed to delete {file_path}: {e}')
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                shutil.rmtree(dir_path)  # Delete the directory and its contents
            except Exception as e:
                print(f'Failed to delete directory {dir_path}: {e}')
    has_cleared_d_drive = True

output_message = ""
dialog_title = ""

if has_cleared_recycle_bin and has_cleared_d_drive:
    output_message = "Deleted " + str(recycle_bin_items_count) + " item(s) from Recycle Bin and " + str(d_drive_items_count) + " item(s) from D: Drive."
    dialog_title = "Recycle Bin and D: Drive Cleared Successfully!"
elif has_cleared_recycle_bin:
    output_message = "Deleted " + str(recycle_bin_items_count) + " item(s) from Recycle Bin."
    dialog_title = "Recycle Bin Cleared Successfully!"
elif has_cleared_d_drive:
    output_message = "Deleted " + str(d_drive_items_count) + " item(s) from D: Drive."
    dialog_title = "D: Drive Cleared Successfully!"
else:
    output_message = "Recycle Bin and D: Drive are already empty."
    dialog_title = "No Items to Delete"

# tkinter is already bundled with the executable.
import tkinter as tk
from tkinter import messagebox as mbox

def self_destruct():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()  # Hide the main window
root.after(10000, self_destruct)
mbox.showinfo(dialog_title, output_message, parent=root)
root.mainloop()