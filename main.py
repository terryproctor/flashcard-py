from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#--------------------------------------------------------
# UI
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=40, pady=35)
window.title("Flashy")

#Canvas for card 800 x 526
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image = cross_image, highlightthickness = 0)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image = tick_image, highlightthickness = 0)
tick_button.grid(row=1, column=2)

window.mainloop()