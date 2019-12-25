# import tkinter
from tkinter import *

def init_window(master):
    # initialize the window size
    master.geometry('{}x{}'.format(200, 150))
    master.minsize(width=200, height=150)

    # window title
    master.title("Tkinter GUI: Pack")

    w = Label(master, text="Fill=NONE", bg="red", fg="white")
    w.pack()
    w = Label(master, text="Fill=X", bg="green", fg="black")
    w.pack(fill=X)
    w = Label(master, text="Fill=Y", bg="blue", fg="white")
    w.pack(side='right', fill=Y)

def main():
    # initialize window
    root = Tk()
    # called init_window() to initialize window properties
    init_window(root)
    # However, the window won’t appear until we’ve entered the Tkinter event loop.
    # The program will stay in the event loop until we close the window.
    root.mainloop()

if __name__ == ('__main__'):
    main()
