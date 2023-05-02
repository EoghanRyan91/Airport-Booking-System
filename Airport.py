import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
   
   
class AirportBookingSystem:
   
       def __init__(self, master):
          self.master = master
          self.master.title("Airport Booking System")
  
          # Create departure airport combo box
          dep_airports_label = ttk.Label(self.master, text="Departure Airport:")
          dep_airports_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
          self.dep_airports_var = tk.StringVar()
          self.dep_airports_combobox = ttk.Combobox(self.master, textvariable=self.dep_airports_var, state="readonly")
          self.dep_airports_combobox.grid(row=0, column=1, padx=5, pady=5)
  
          # Create destination airport combo box
          dest_airports_label = ttk.Label(self.master, text="Destination Airport:")
          dest_airports_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
          self.dest_airports_var = tk.StringVar()
          self.dest_airports_combobox = ttk.Combobox(self.master, textvariable=self.dest_airports_var, state="readonly")
          self.dest_airports_combobox.grid(row=1, column=1, padx=5, pady=5)
  
          # Create seat type combo box
          seat_types_label = ttk.Label(self.master, text="Seat Type:")
          seat_types_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
          self.seat_types = ["Economy", "Business", "First Class"]
          self.seat_types_var = tk.StringVar()
          self.seat_types_combobox = ttk.Combobox(self.master, textvariable=self.seat_types_var, values=self.seat_types,
                                                   state="readonly")
          self.seat_types_combobox.current(0)
          self.seat_types_combobox.grid(row=2, column=1, padx=5, pady=5)
  
          # Create direction radio buttons
          direction_label = ttk.Label(self.master, text="Direction:")
          direction_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
          self.direction_var = tk.StringVar(value="one-way")
          self.one_way_radio = ttk.Radiobutton(self.master, text="One Way", variable=self.direction_var, value="one-way")
          self.one_way_radio.grid(row=3, column=1, padx=5, pady=5, sticky="w")
          self.return_radio = ttk.Radiobutton(self.master, text="Return", variable=self.direction_var, value="return")
          self.return_radio.grid(row=3, column=1, padx=5, pady=5, sticky="e")
  
          # Create second leg check button
          second_leg_label = ttk.Label(self.master, text="Second Leg:")
          second_leg_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
          self.second_leg_var = tk.BooleanVar()
          self.second_leg_checkbutton = ttk.Checkbutton(self.master, variable=self.second_leg_var)
          self.second_leg_checkbutton.grid(row=4, column=1, padx=5, pady=5, sticky="w")
  
          # Create passenger name entry
          passenger_name_label = ttk.Label(self.master, text="Passenger Name:")
          passenger_name_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
          self.passenger_name_var = tk.StringVar()
          self.passenger_name_entry = ttk.Entry(self.master, textvariable=self.passenger_name_var)
          self.passenger_name_entry.grid(row=5, column=1, padx=5, pady=5)
  
          # Create book button
          book_button = ttk.Button(self.master, text="Book", command=self.book_flight)
          book_button.grid(row=6, column=1, padx=5, pady=5, sticky="e")
  
          # Create departure and destination airports list
          self.airports = ["Paris (CDG)", "London (LHR)", "Frankfurt (FRA)", "Amsterdam (AMS)",
                            "Madrid (MAD)", "Barcelona (BCN)", "Rome (FCO)", "Athens (ATH)"]
          self.dep_airports_combobox["values"] = sorted(self.airports)
          self.dest_airports_combobox["values"] = sorted(self.airports)
  
       def book_flight(self):
          dep_airport = self.dep_airports_var.get()
          dest_airport = self.dest_airports_var.get()
          seat_type = self.seat_types_var.get()
          direction = self.direction_var.get()
          second_leg = self.second_leg_var.get()
          passenger_name = self.passenger_name_var.get()
  
          if dep_airport == dest_airport:
              mb.showerror("Error", "Departure and destination airports cannot be the same.")
          else:
              if direction == "one-way":
                  message = f"You have booked a {seat_type} seat from {dep_airport} to {dest_airport}. "
                  message += f"Your booking reference is AB123."
                  mb.showinfo("Booking Confirmed", message)
              else:
                  if second_leg:
                      message = f"You have booked a {seat_type} seat from {dep_airport} to {dest_airport} with a second leg. "
                      message += f"Your booking reference is AB123."
                      mb.showinfo("Booking Confirmed", message)
                  else:
                      message = f"You have booked a {seat_type} seat from {dep_airport} to {dest_airport} with a return. "
                      message += f"Your booking reference is AB123."
                      mb.showinfo("Booking Confirmed", message)
  
  
if __name__ == "__main__":
      root = tk.Tk()
      app = AirportBookingSystem(root)
      root.mainloop()
