import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from service.scan import scan_dir
from service.ui.checkentry import create_entry
from service.ui.collapseablepanel import CollapsablePanel
from service.ui.scrollableframe import ScrollableFrame

# create the root window
root = tk.Tk()
root.title('windows restoration')
#root.resizable(False, False)
#root.geometry('300x150')



is_image=False

frame=ttk.Frame(root)
frame.grid()

selection = ttk.Label(
    frame,
    text='C:\\',
    
)
selection.grid(column=2,row=0)




def select_file():
    global is_image
    filetypes = (
        ('disk image files', '*.img'),
        ('ISO file', '*.iso'),
    )

    filename = fd.askopenfilename(
        title='Open Source File',
        initialdir='/',
        filetypes=filetypes,)
    
    is_image=True
    selection.configure(text=filename)
    print(filename)

def select_dir():
    global is_image

    dirpath = fd.askdirectory(
        title='Open Source File',
        initialdir='/'
        )
    is_image=False

    selection.configure(text=dirpath)
    print(dirpath)

# open button
open_button = ttk.Button(
    frame,
    text='Open Source Image File',
    command=select_file
)
#open_button.pack(expand=True)
open_button.grid(column=0,row=0)
open_button_dir = ttk.Button(
    frame,
    text='Select Source Directory',
    command=select_dir
)
open_button_dir.grid(column=1,row=0)
#open_button_dir.pack(expand=True)

def scan():
    path=selection.cget("text")
    if is_image:
        raise "not implemented yet"
    
    entries= scan_dir(path)



    scan_result = tk.Tk()
    scan_result.title('windows restoration - scan result')
    
    sframe=ScrollableFrame(scan_result)

    CollapsablePanel(sframe.scrollable_frame,name="programs",entries=[create_entry(entry,sframe.scrollable_frame) for entry in entries])

    #scan_result.pack()
    sframe.pack(anchor="w",expand=True)
    #ttk.Scrollbar(sframe, orient='vertical')

    #frame.pack(expand=True)
    scan_result.geometry("400x650")

    root.quit()
    scan_result.mainloop()


scanButton = ttk.Button(
    frame,
    text='Scan',
    command=scan
)
scanButton.grid(column=0,row=1,sticky="w")


# run the application
root.mainloop()