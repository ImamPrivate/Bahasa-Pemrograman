from tkinter import *
from tkinter import ttk
layar = Tk()
layar.configure(bg="blue")
layar.geometry("300x200")
layar.title("GUI")

frame = ttk.Frame(layar)
frame.pack(padx=10,pady=10,fill="x",expand=True)

teks=ttk.Label(frame, text="Hello everyone")
teks.pack(padx=10,pady=10,fill="x",expand=True)

layar.mainloop()
