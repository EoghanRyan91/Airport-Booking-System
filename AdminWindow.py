import tkinter as tk
from tkinter import ttk
import sqlite3

class AdminWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1200x500")
        self.window.title("Admin Window")
        self.label = tk.Label(self.window, text="This is the Admin Window")
        
        # Display DB Button
        db_button = ttk.Button(self.window, text="Display DB Contents", command=self.display_db_contents)
        db_button.grid(row=1, column=0, padx=5, pady=5)


      # DB Table Code

        self.table = ttk.Treeview(self.window)
        self.table.grid(row=3, column=0, padx=5, pady=5)

        self.window.mainloop()

  
      # Function to show DB Contents
    def display_db_contents(self):
        self.load_db_contents()

    def load_db_contents(self):
        connection = sqlite3.connect('flight_database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flights")
        rows = cursor.fetchall()
        self.table.delete(*self.table.get_children())
        self.table["columns"] = ("1", "2", "3", "4")
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("1", width=100, anchor=tk.CENTER)
        self.table.column("2", width=100, anchor=tk.CENTER)
        self.table.column("3", width=100, anchor=tk.CENTER)
        self.table.column("4", width=100, anchor=tk.CENTER)
        self.table.heading("1", text="Passenger Name")
        self.table.heading("2", text="Departure Airport")
        self.table.heading("3", text="Destination Airport")
        self.table.heading("4", text="Seat Type")
        for row in rows:
            self.table.insert("", tk.END, text="", values=row)
        connection.close()

        
    

if __name__ == "__main__":
    admin_window = AdminWindow()

