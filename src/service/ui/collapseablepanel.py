from tkinter import Widget, ttk


class CollapsablePanel(ttk.Frame):

    hidden=True

    def __init__(self,container:Widget,name:str,entries:list[Widget],as_label=False, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.entries=entries
        self.name=name
        self.cnt=container

        if as_label:
            self.toggle_button=ttk.Label(container,text=name)
            self.toggle_button.bind('<Button-1>', self.toggle)
        else:
            self.toggle_button=ttk.Button(container,text=name,command= self.toggle)
        self.toggle_button.pack(anchor="w",)

        #for entry in entries:
           # entry._setup(self,{})  #pack(in_=container)


        self.hide()
        self.pack()


    def toggle(self,*args):
        if self.hidden:
            self.show()
        else:
            self.hide()

    def hide(self):
        for entry in self.entries:
            entry.pack_forget()
        self.hidden=True
        self.toggle_button.configure(text=f"▶️ {self.name}")


    def show(self):
        for entry in self.entries:
            entry.pack(anchor="w",padx=10) #,in_=self.cnt
        self.hidden=False
        self.toggle_button.configure(text=f"🔽 {self.name}")