import tkinter


class Window (tkinter.Tk):
    def __init__ (self, title: str="Window", geometry: str="960x540"):
        super().__init__()
        self.title(title)
        self.figure_canvas = tkinter.Canvas(master=self, highlightthickness=0, border=0)
        self.figure_canvas.pack(fill="both", expand=True)
        self.geometry(geometry)

    def show (self):
        self.mainloop()
