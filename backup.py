import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import customtkinter
from tkinter import messagebox
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def open_file_dialog(prompt):
    folder = filedialog.askdirectory(title=prompt)
    if folder:
        return str(Path(folder))
    return None


def backup_files():
    while True:
        # Get source directory
        source_dir = open_file_dialog("Select the folder you want to backup")
        if not source_dir:
            messagebox.showerror("No source directory selected. Exiting...")
            return

        # Get destination directory
        save_dir = open_file_dialog("Select the destination for the backup")
        if not save_dir:
            messagebox.showerror("No destination directory selected. Exiting...")
            return

        messagebox.showinfo("Backup in progress",f"Backing up from: {source_dir} to {save_dir}...")

        try:
            shutil.copytree(source_dir, save_dir, dirs_exist_ok=True)
            messagebox.showinfo("Success", "Backup completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        # Ask the user if they want to backup again
        yn = input("Do you want to backup again? (Y/N): ").lower()
        if yn != "y":
            print("Exiting the script.")
            break




root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Backup Util", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Backup Button", command=backup_files)
button.pack(pady=12, padx=10)

root.mainloop()
