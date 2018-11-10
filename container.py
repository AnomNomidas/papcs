import tkinter as tk
from tkinter import Menu

# drag-and-drop functionality from https://stackoverflow.com/questions/37280004/drag-and-drop-widgets-tkinter

class DragDropWidget:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.drag_start_x = 0
        self.drag_start_y = 0
        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)

    def drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def drag_motion(self, event):
        x = self.winfo_x() - self.drag_start_x + event.x
        y = self.winfo_y() - self.drag_start_y + event.y
        self.place(x=x, y=y)

class CardContainer(DragDropWidget, tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-3>", self.toggle_facing)
        self.bind("<Button-2>", self.lift_card)
        self.bind("<Double-Button-1>", self.card_context_menu)
        
        self.context_menu = Menu(self, tearoff=0)
        self.context_menu.add_command(label="Delete card", command=lambda: self.destroy())

    def toggle_facing(self, event):
        self.card.isFaceUp = not self.card.isFaceUp
        new_photo = self.card.card_image

        self.config(image=new_photo)
        self.image = new_photo
    
    def lift_card(self, event):
        self.lift()

    def card_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
        