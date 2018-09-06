import tkinter as tk
from ctypes import windll
from tkinter import Button, Frame, Label, Menu, Tk, Canvas, Widget

from card import Card
from dialog import Dialog, DialogCreateCard

# DPI scaling fix
windll.shcore.SetProcessDpiAwareness(1)

class PrettyAccuratePlayingCardsSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Pretty Accurate Playing Cards Simulator")

        self.main_canvas = Canvas(self.master, bg="green")
        self.main_canvas.bind("<Button-3>", self.show_context_menu)
        self.main_canvas.pack(fill="both", expand=1)

        self.context_menu = Menu(self.main_canvas, tearoff=0)
        self.context_menu.add_command(label="Create a card...", command=lambda: self.create_card(self.main_canvas))

        self.b = Button(self.main_canvas, text="Quit", command=root.destroy)
        self.b.pack()

    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def create_card(self, canvas):
        DialogCreateCard(canvas)

root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))
gui = PrettyAccuratePlayingCardsSimulator(root)
root.mainloop()
