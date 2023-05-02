import tkinter as tk
from tkinter import ttk
import sqlite3

class AdminWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x300")
        self.window.title("Admin Window")

        self.label = tk.Label(self.window, text="This is the Admin Window")
        

        db_button = ttk.Button(self.window, text="Display DB Contents")
        db_button.grid(row=1, column=1, padx=5, pady=5)
      

        self.window.mainloop()

if __name__ == "__main__":
    admin_window = AdminWindow()

