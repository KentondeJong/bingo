
from tkinter import *
from tkinter import messagebox
import random

bingo = []
bingo.append(list(range(1,16)))
bingo.append(list(range(16,31)))
bingo.append(list(range(31,46)))
bingo.append(list(range(46,61)))
bingo.append(list(range(61,76)))
buttons = []
command = ""

master = Tk()
master.title('BINGO')
window_height = 500
window_width = 900
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

column = 0
row = 1

for letters in bingo:
    if column == 0 : text = 'B'
    if column == 1 : text = 'I'
    if column == 2 : text = 'N'
    if column == 3 : text = 'G'
    if column == 4 : text = 'O'
    Label(master, text=text).grid(row=0, column=column)

    master.columnconfigure(column, weight=1)

    for nums in letters:
        master.rowconfigure(row, weight=1)
        button = Checkbutton(master, text=nums, variable=nums, state=DISABLED)
        button.grid(row=row, column=column)
        buttons.append(button)
        row = 1 if row == len(letters) else row +1
    column += 1

def roll():
   #shuffle letters and numbers
    random.shuffle(bingo)
    random.shuffle(bingo[0])
    num = bingo[0][0]

    #what letter is it?
    str = ''
    if num >= 1 and num <= 15:
        str = 'B'
    elif num >= 16 and num <= 30:
        str = 'I'
    elif num >= 31 and num <= 45:
        str = 'N'
    elif num >= 46 and num <= 60:
        str = 'G'
    elif num >= 61 and num <= 75:
        str = 'O'

    #print the letters and number
    messagebox.showinfo( "You rolled...", (str, bingo[0][0]))
    buttons[bingo[0][0]-1].select() #check the checkbox that we just rolled

    #remove number, if last number, remove letter
    bingo[0].pop(0)
    if len(bingo[0]) == 0:
        bingo.pop(0)

    #how many numbers are left?
    num = 0
    for letters in bingo:
        for nums in letters:
            num += 1

    #if no numbes are left
    if num == 0:
       x = messagebox.showinfo( "Game Over!", "Thanks for playing!")
       master.destroy()


Button(master, text ="Roll", command = roll).grid(row=17, column=0, columnspan=2, padx=10, pady=10)
Button(master, text ="Close", command=master.destroy).grid(row=17, column=3, columnspan=2, padx=10, pady=10)

mainloop()

