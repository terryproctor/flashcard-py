from tkinter import *
import pandas as pd 
import random


BACKGROUND_COLOR = "#B1DDC6"
# read csv
df = pd.read_csv("./data/french_words.csv")
#orient allows to go through each row and get both the 'French' and 'English' (keys) for a random row
to_learn = df.to_dict(orient='records')
language = "French"
current_card = {}


#---------------------------------------------------------------------------
#change word on buttons
def change_word():
    global current_card, flip_timer

    #Reset card
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")

    #get word
    dict_len = len(df['French'])
    rand_int = random.randint(0, dict_len-1)
    current_card = to_learn[rand_int]
    french_word = current_card['French']
    canvas.itemconfig(card_word, text=french_word)
    
    #flip card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)

#--------------------------------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

#---------------------------------------------------------------------------------
# UI
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)
#Canvas for card 800 x 526
word = "word"

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text=f"{language}", font="Ariel 40 italic")
card_word = canvas.create_text(400, 263, text=f"{word}", font="Ariel 60 bold")
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image = cross_image, highlightthickness = 0, command=change_word)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image = tick_image, highlightthickness = 0, command=change_word)
tick_button.grid(row=1, column=2)

window.mainloop()