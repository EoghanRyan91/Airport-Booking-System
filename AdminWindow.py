import tkinter as tk

class AdminWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("Admin Window")

        self.label = tk.Label(self.window, text="This is the Admin Window")
        self.label.pack()

        self.window.mainloop()

if __name__ == "__main__":
    admin_window = AdminWindow()

