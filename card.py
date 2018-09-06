from enum import Enum
import tkinter as tk

class Card :
    class Suit(Enum) :
        Diamonds = 'D'
        Clubs = 'C'
        Hearts = 'H'
        Spades = 'S'

    def __init__(self, card_number=0, card_suit=None, isFaceUp=True):
        if card_number not in range(1, 14) or card_suit not in Card.Suit:
            self.card_number = 0
            self.card_suit = None
        else:
            self.card_number = card_number
            self.card_suit = card_suit
            self.isFaceUp = isFaceUp
    
    @property
    def card_name(self):
        face_cards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

        if self.card_number not in range(1, 14) or self.card_suit not in Card.Suit:
            self._card_name = "Undefined card"
        else:
            self._card_name = str(self.card_number) + " of " + self.card_suit.name if self.card_number not in face_cards else face_cards[self.card_number] + " of " + self.card_suit.name
        
        return self._card_name

    @property
    def card_id(self):
        face_id = {1: "A", 11: "J", 12: "Q", 13: "K"}
        
        if self.card_number not in range(1, 14) or self.card_suit not in Card.Suit:
            self._card_id = "0x"
        else:
            self._card_id = str(self.card_number) +  self.card_suit.value if self.card_number not in face_id else face_id[self.card_number] + self.card_suit.value
        
        return self._card_id
    
    @property
    def card_image(self):
        return tk.PhotoImage(file="images/" + self.card_id + ".png") if self.isFaceUp else tk.PhotoImage(file="images/blue_back.png")