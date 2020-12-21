import random
from tkinter import *

root = Tk()
root.title("Password Generator")
root.geometry("600x600")

def submit():
    global password

    password = Label(root, text="")
    password.config(font=("Courier", 24))
    password.grid(row=3, column=0, pady=40)
    characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                  'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'E', 'R', 'T',
                  'Y', 'U', 'I',
                  'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    x = int(characters_want.get())
    results = random.choices(characters, k=x)
    if x <= 8:
        password = Label(root, text=" password too short")
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)


    if x == 9:
        password = Label(root, text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] + results[6] + results[7] +results[8])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)

    if x == 10:
        password = Label(root, text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] + results[6] + results[7] +
              results[8] + results[9])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 11:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] + results[6] + results[7] +
              results[8] + results[9] + results[10])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 12:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[9] + results[10] + results[11] )
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 13:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
                              results[6] + results[7] + results[8] + results[9] + results[10] + results[11]+ results[12])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 14:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
                              results[6] + results[7] + results[8] + results[9] + results[10] + results[11] + results[
                                  12] + results[13])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 15:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[9] + results[10] + results[11] + results[12] + results[
                  13] + results[14])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)

    if x == 16:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[12] + results[13] + results[14] + results[15] +
              results[9] + results[10] + results[11])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 17:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[12] + results[13] + results[14] + results[15] + results[
                  16] +
              results[9] + results[10] + results[11])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    if x == 18:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[12] + results[13] + results[14] + results[15] + results[
                  16] +
              results[9] + results[10] + results[11] + results[17])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)

    if x == 19:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[12] + results[13] + results[14] + results[15] + results[
                  16] +
              results[9] + results[10] + results[11] + results[17] + results[18])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)

    if x == 20:
        password = Label(root,
                         text=results[0] + results[1] + results[2] + results[3] + results[4] + results[5] +
              results[6] + results[7] + results[8] + results[12] + results[13] + results[14] + results[15] + results[
                  16] +
              results[9] + results[10] + results[11] + results[17] + results[18] + results[19])
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)


    if x >= 21:
        password = Label(root, text=" password too long")
        password.config(font=("Courier", 24))
        password.grid(row=3, column=0, pady=40)
    characters_want.delete(0, END)


#text box for asking how many characters they want
characters_want = Entry(root, width=55)
characters_want.grid(row=1, column=0, padx=20, pady=20)




#label for password
characters_want_label = Label(root, text=" how many characters do you " + "\n" "want for your password?")
characters_want_label.config(font=("Courier", 24))
characters_want_label.grid(row=0, column=0,  pady=40)

#Enter button
enter_btn = Button(root, text="Create Password", command=submit)
enter_btn.config(font=("Courier", 24))
enter_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=90, ipady=13 )

def clear_widget(widget):
    widget.destroy()
#clear button
clear = Button(root, text="Clear", command=lambda: clear_widget(password))
clear.config(font=("Courier", 24))
clear.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=90, ipady=13 )
root.mainloop()










