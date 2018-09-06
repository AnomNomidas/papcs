# http://www.effbot.org/tkinterbook/tkinter-dialog-windows.htm

from tkinter import *
import os
from card import Card
from container import DragDropWidget, CardContainer

class Dialog(Toplevel):

    def __init__(self, parent, title = None):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override

class DialogCreateCard(Dialog):
    def body(self, master):
        self.tkvar_suit = StringVar()
        self.tkvar_value = StringVar()
        self.tkvar_facing = StringVar()

        self.options_suit = {"Diamonds": Card.Suit.Diamonds, "Clubs": Card.Suit.Clubs, "Hearts": Card.Suit.Hearts, "Spades": Card.Suit.Spades}
        self.tkvar_suit.set("Spades")

        self.options_value = {"Ace": 1, "King": 13, "Queen": 12, "Jack": 11}
        for x in range(2, 11):
            self.options_value[str(x)] = x
        self.tkvar_value.set("Ace")

        self.options_facing = {"up": True, "down": False}
        self.tkvar_facing.set("up")
        
        Label(master, text="Create a(n) ").grid(column=0, row=0)
        OptionMenu(master, self.tkvar_value, *self.options_value).grid(column=1, row=0)
        Label(master, text=" of ").grid(column=2, row=0)
        OptionMenu(master, self.tkvar_suit, *self.options_suit).grid(column=3, row=0)
        Label(master, text=" facing ").grid(column=4, row=0)
        OptionMenu(master, self.tkvar_facing, *self.options_facing).grid(column=5, row=0)

    def apply(self):
        card = Card(self.options_value[self.tkvar_value.get()], self.options_suit[self.tkvar_suit.get()], self.options_facing[self.tkvar_facing.get()])
        photo = card.card_image

        card_image = CardContainer(self.nametowidget(self.winfo_parent()), image=photo, borderwidth=1, highlightthickness=0)
        card_image.image = photo
        card_image.card = card
        self.nametowidget(self.winfo_parent()).create_window(500, 500, window=card_image)
        
