import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def open_file_dialog(prompt):
    folder = filedialog.askdirectory(title=prompt)
    if folder:
        return str(Path(folder))
    return None


def backup_files():
    while True:
        # Initialize the Tkinter window
        root = tk.Tk()
        root.withdraw()

        # Get source directory
        source_dir = open_file_dialog("Select the folder you want to backup")
        if not source_dir:
            print("No source directory selected. Exiting...")
            break

        # Get destination directory
        save_dir = open_file_dialog("Select the destination for the backup")
        if not save_dir:
            print("No destination directory selected. Exiting...")
            break

        print(f"Backing up from: {source_dir} to {save_dir}...")

        # Perform the backup using shutil.copytree
        try:
            shutil.copytree(source_dir, save_dir, dirs_exist_ok=True)
            print("Backup completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask the user if they want to backup again
        yn = input("Do you want to backup again? (Y/N): ").lower()
        if yn != "y":
            print("Exiting the script.")
            break


if __name__ == "__main__":
    backup_files()