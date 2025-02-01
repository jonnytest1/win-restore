from tkinter import ttk,Canvas,Widget

class ScrollableFrame(ttk.Frame):

    paddings_y=14
    paddings_x=26

    def __init__(self, container:Widget, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"), 
                yscrollcommand=scrollbar.set
            )
        )
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        container.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"), 
                yscrollcommand=scrollbar.set,
                height=container.winfo_height()-self.paddings_y,
                width=container.winfo_width()-self.paddings_x
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.update_idletasks()
        self.canvas.configure(yscrollcommand=scrollbar.set,scrollregion=self.canvas.bbox('all'))

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units") 