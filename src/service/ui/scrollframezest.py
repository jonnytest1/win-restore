from tkinter import Tk, ttk
from scrollableframe import ScrollableFrame


root =Tk()

frame = ScrollableFrame(root)

for i in range(500):
    ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

frame.pack()
root.mainloop()