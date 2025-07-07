from tkinter import  *
import pandas as pd
from card import Card
import time


def flip_card(card_ex: Card):
    card_ex.display_english(canvas, "images/card_back.png")

BACKGROUND_COLOR = "#B1DDC6"
FRONT_IMAGE = "images/card_front.png"
BACK_IMAGE = "images/card_back.png"
cards = []

#read each set of words from the data set into card objects
langauge_data = pd.read_csv("data/french_words.csv")
for key, row in langauge_data.iterrows():
    #create card object
    card_object = Card(row["French"], row["English"])
    cards.append(card_object)

#create UI
window = Tk()
window.title("Flashy")
window.minsize(width=1000, height= 650)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

#
# Create the canvas widget
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR)
canvas.pack(pady=20)


current_index = 0  # Track current card index

def show_next_card():
    global current_index

    if len(cards) == 0:
        print("No more cards left — deck complete!")
        canvas.delete("all")
        canvas.create_text(400, 263, text="Great job!", fill="black", font=("Arial", 40, "bold"))
        return

    if current_index >= len(cards):
        current_index = 0  # wrap around if we reach the end

    card = cards[current_index]
    card.display_french(canvas, FRONT_IMAGE)

    # Schedule flip to English after 3 seconds
    window.after(3000, lambda c=card: c.display_english(canvas, BACK_IMAGE))

def mark_known():
    global current_index
    if cards:
        print(f"Known: {cards[current_index].french_word}")
        cards.pop(current_index)  # remove known card from list
    show_next_card()

def mark_unknown():
    global current_index
    if cards:
        print(f"Unknown: {cards[current_index].french_word}")
        current_index += 1
    show_next_card()


# Start by showing the first card

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Create buttons with image icons
right_button = Button(image=right_img, highlightthickness=0, command=mark_known)
right_button.pack(side="right", padx=50)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=mark_unknown)
wrong_button.pack(side="left", padx=50)

show_next_card()









window.mainloop()

