from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def check_winner():
    if (button1['text'] == button2['text'] == button3['text'] == '0' or
        button4['text'] == button5['text'] == button6['text'] == '0' or
        button7['text'] == button8['text'] == button9['text'] == '0' or 
        button1['text'] == button4['text'] == button7['text'] == '0' or
        button2['text'] == button5['text'] == button8['text'] == '0' or
        button3['text'] == button6['text'] == button9['text'] == '0' or 
        button1['text'] == button5['text'] == button9['text'] == '0' or
        button3['text'] == button5['text'] == button7['text'] == '0'):
         messagebox.showinfo("Winner of game","Player 0 is the winner")

    elif(button1['text'] == button2['text'] == button3['text'] == 'X' or
        button4['text'] == button5['text'] == button6['text'] == 'X' or
        button7['text'] == button8['text'] == button9['text'] == 'X' or 
        button1['text'] == button4['text'] == button7['text'] == 'X' or
        button2['text'] == button5['text'] == button8['text'] == 'X' or
        button3['text'] == button6['text'] == button9['text'] == 'X' or 
        button1['text'] == button5['text'] == button9['text'] == 'X' or
        button3['text'] == button5['text'] == button7['text'] == 'X'):
        messagebox.showinfo("Winner of game","Player X is the winner")
    elif all(button['text'] != ' ' for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9]):
        messagebox.showinfo("Draw","No winner ")

root = Tk()
root.geometry('560x375')
button1 = ttk.Button(root, text=" ", command=lambda: buttonPressed(1))
button1.grid(row=0, column=0, ipadx=50, ipady=50)
button2 = ttk.Button(root, text=" ", command=lambda: buttonPressed(2))
button2.grid(row=0, column=1, ipadx=50, ipady=50)
button3 = ttk.Button(root, text=" ", command=lambda: buttonPressed(3))
button3.grid(row=0, column=2, ipadx=50, ipady=50)
button4 = ttk.Button(root, text=" ", command=lambda: buttonPressed(4))
button4.grid(row=1, column=0, ipadx=50, ipady=50)
button5 = ttk.Button(root, text=" ", command=lambda: buttonPressed(5))
button5.grid(row=1, column=1, ipadx=50, ipady=50)
button6 = ttk.Button(root, text=" ", command=lambda: buttonPressed(6))
button6.grid(row=1, column=2, ipadx=50, ipady=50)
button7 = ttk.Button(root, text=" ", command=lambda: buttonPressed(7))
button7.grid(row=2, column=0, ipadx=50, ipady=50)
button8 = ttk.Button(root, text=" ", command=lambda: buttonPressed(8))
button8.grid(row=2, column=1, ipadx=50, ipady=50)
button9 = ttk.Button(root, text=" ", command=lambda: buttonPressed(9))
button9.grid(row=2, column=2, ipadx=50, ipady=50)

player = 1

def buttonPressed(buttonNumber):
    global player
    if player == 1:
        text_value = 'X'
    else:
        text_value = '0'

    if buttonNumber == 1:
        button1.config(text=text_value)
    elif buttonNumber == 2:
        button2.config(text=text_value)
    elif buttonNumber == 3:
        button3.config(text=text_value)
    elif buttonNumber == 4:
        button4.config(text=text_value)
    elif buttonNumber == 5:
        button5.config(text=text_value)
    elif buttonNumber == 6:
        button6.config(text=text_value)
    elif buttonNumber == 7:
        button7.config(text=text_value)
    elif buttonNumber == 8:
        button8.config(text=text_value)
    elif buttonNumber == 9:
        button9.config(text=text_value)

    check_winner()
    player = 3 - player  # Toggle between player 1 and 2

root.mainloop()
