from tkinter import LEFT, Widget, ttk,ACTIVE
from service.scan import CopyEntry
from service.ui.collapseablepanel import CollapsablePanel



def create_entry(p:CopyEntry,container:Widget):

    entry_frame=ttk.Frame(container)
    #entry_frame.setvar("displaymode","grid")
    btn = ttk.Checkbutton(entry_frame,text="")
    btn.config(state=ACTIVE)
    btn.state(["active","selected","!alternate","!focus"])
    btn.grid(column=0,row=0,sticky="n")


    if p.with_registry:
        sub_frame=ttk.Frame(entry_frame)
        sub_frame.grid(column=1,row=0)
        lbl=ttk.Label(sub_frame,text="also has registry entries")
        CollapsablePanel(sub_frame,f"ℹ️ {p.path}",[lbl],as_label=True)
    else:
        ttk.Label(entry_frame,text=p.path).grid(column=1,row=0)
    
    #entry_frame.pack(side=LEFT,anchor="s")

    return entry_frame

