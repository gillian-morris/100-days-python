# Day 31 - Flash Card
# Review of tkinter, pandas, and other concepts covered so far.

from tkinter import *
import pandas as pd
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")
word = None
timer = None
# -------------------------Update UI---------------------#

def flip_card():
    global word
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(canvas_img,image=card_back_img)


def next_card():
    global word
    global timer
    window.after_cancel(timer)

    word = random.choice(to_learn)

    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    canvas.itemconfig(canvas_img,image=card_front_img)
    timer = window.after(3000, flip_card)


#--------------------------Right--------------------------#

def right_answer():
    global word
    try:
        to_learn.remove(word)
    except ValueError:
        messagebox.showinfo(
            title="Done", message="You have mastered all words items provided."
        )
    next_card()

#--------------------------Wrong--------------------------#

def wrong_answer():
    next_card()

#---------------------------UI----------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400,263,image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
word_text = canvas.create_text(
    400, 263, text="Word", font=(FONT, 60, "bold")
)
canvas.grid(row=0, column=0, columnspan=2)

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong_answer)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_img, highlightthickness=0, command=right_answer)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()

data = pd.DataFrame(to_learn)
data.to_csv("data/words_to_learn.csv", index=False)
