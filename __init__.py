import tkinter


class Window (tkinter.Tk):
    def __init__ (self, title: str="Window", geometry: str="800x450"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

    def show (self):
        self.mainloop()
