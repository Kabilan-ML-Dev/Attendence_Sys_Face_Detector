import tkinter as tk
from tkinter import Label, Button
import csv
import os
from datetime import datetime
import femod  # your face recognition module

# CSV file path
attd_file = "Attendance.csv"

# Function to initialize CSV file if not present
def initialize_csv():
    if not os.path.exists(attd_file):
        with open(attd_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time", "Status"])
        print("✅ CSV file initialized.")

# Function to mark attendance
def take_attendance():
    name = femod.predicted_label()  # This should return the predicted name (string)
    if not name:
        print("⚠️ No face recognized.")
        return
     today = datetime.now().strftime("%Y-%m-%d")

    # Step 1: Check if today's attendance for this name already exists
    already_marked = False
    if os.path.exists(attd_file):
        with open(attd_file, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Name"] == name and row["Date"] == today:
                    already_marked = True
                    break

    if already_marked:
        print(f"⚠️ Attendance already marked for {name} today.")
        return
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(attd_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, date, time, "Present"])
    
    print(f"✅ Attendance marked for {name} at {time}.")

# Initialize GUI
m = tk.Tk()
m.title("Attendance System")
m.geometry("500x600")

a = Label(m, text="RKAS Industries Pvt Ltd.", font=("Helvetica", 24))
a.pack()
b = Label(m, text="Attendance System", font=("Helvetica", 18))
b.pack()

c = Button(m, text="Take Attendance", height=5, width=50,
           command=take_attendance, bg='gold1', fg='black')
c.place(relw=0.8, relh=0.25, relx=0.104167, rely=0.265185)

d = Button(m, text="Quit", command=m.quit, bg='darkolivegreen1', fg='black')
d.place(relw=0.8, relh=0.25, relx=0.104167, rely=0.59)

initialize_csv()  
m.mainloop()
