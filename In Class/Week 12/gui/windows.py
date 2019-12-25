# import tkinter
from tkinter import *

def init_window(master):
    # initialize the window size
    master.geometry('{}x{}'.format(500, 200))
    # # fixed size window
    # master.resizable(width=False, height=False)
    # define maximum-minimum size of window
    master.maxsize(width=800, height=600)
    master.minsize(width=200, height=150)

    # window title
    master.title("First GUI program")

    # create a Label widget as a child to the master window:
    # A Label widget can display either text or an icon or other image.
    text_content = """At present, only GIF and PPM/PGM
    formats are supported, but an interface
    exists to allow additional image file
    formats to be added easily."""
    tmp1 = Label(master, text=text_content, font=("Helvetica", 14))
    # packed the widget into the master window
    tmp1.pack(side="left")
    # define image path
    logo = PhotoImage(file="images\python_logo.gif")
    tmp2 = Label(master, image=logo)
    tmp2.image = logo
    tmp2.pack(side="right")

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
