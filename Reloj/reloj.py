import tkinter as tk
import time

def update_clock():
    current_hour = time.strftime("%H:%M:%S")
    ceas.config(text=current_hour)
    ceas.after(1000, update_clock)

app = tk.Tk()
app.title("Reloj pyton")

ceas = tk.Label(app, text="", font=("helvetica", 48))
ceas.pack()

update_clock()
app.mainloop()