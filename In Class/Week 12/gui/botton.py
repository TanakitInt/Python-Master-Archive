# import tkinter
from tkinter import *

def init_window(master):
    # initialize the window size
    master.geometry('{}x{}'.format(400, 300))
    # fixed size window
    master.resizable(width=False, height=False)
    # window title
    master.title("Tkinter GUI: Button")

def init_button(master):
    hello_button = Button(master, text='Click Me!', command = lambda: print_message(master))
    hello_button.pack()

def print_message(master):
    tmp = Label(master, text='Hi! This is the welcome message.').pack()

def main():
    # initialize window
    root = Tk()
    # initialize window
    init_window(root)
    # initialize buttons
    init_button(root)
    # Tkinter event loop:
    # The program will stay in the event loop until we close the window.
    root.mainloop()

if __name__ == ('__main__'):
    main()
