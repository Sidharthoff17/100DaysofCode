import time
from tkinter import *

class Card:
    def __init__(self, french_word, english_word):

        self.french_word = french_word
        self.english_word = english_word
        self.img = None

    def display_french(self, canvas: Canvas, image):

        try:
            self.img = PhotoImage(file=image)
            # Place the image in the center of the canvas
            canvas.create_image(410, 275, image=self.img, anchor="center")
        except Exception as e:
            print("Couldn't load image:", e)
            canvas.create_text(250, 200, text="Image not found", fill="red", font=("Arial", 20, "bold"))

        canvas.create_text(400, 150, text="French", font=("Arial", 24, "italic"), fill="black")
        canvas.create_text(400, 300, text=f"{self.french_word}", font=("Arial", 40, "bold"), fill="black")

    def display_english(self, canvas: Canvas, image):
        #
        try:
            self.img = PhotoImage(file = image)
            # Place the image in the center of the canvas
            canvas.create_image(410, 275, image=self.img, anchor="center")
        except Exception as e:
            print("Couldn't load image:", e)
            canvas.create_text(250, 200, text="Image not found", fill="red", font=("Arial", 20, "bold"))

        canvas.create_text(400, 150, text="English", font=("Arial", 24, "italic"), fill="white")
        canvas.create_text(400, 300, text=f"{self.english_word}", font=("Arial", 40, "bold"), fill="white")

    def flip(self,canvas: Canvas, french_image, english_image, delay_ms=3000):

        self.display_french(canvas, french_image)
        # Schedule the flip to English
        canvas.after(delay_ms, lambda: self.display_english(canvas, english_image))