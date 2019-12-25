# import tkinter
from tkinter import *

def init_window(master):
    img_path = 'D:\Documents\KMITL\\06026104_computer_programming\scripts\gui\\'

    # fixed size window
    master.resizable(width=False, height=False)
    # window title
    master.title("Tkinter GUI: Grid")

    # display selected season: row 2, column 0
    output_label = Label(master, text='Selected season: ')
    output_label.grid(row=2, column=0, columnspan=2)

    # Spring: row 0, column 0
    spring_img = PhotoImage(file=img_path+'images\spring.gif')
    spring_label = Button(master, image=spring_img, command=lambda: output_label.config(text='Spring'))
    spring_label.image = spring_img
    spring_label.grid(row=0, column=0)

    # Summer: row 0, column 1
    summer_img = PhotoImage(file=img_path+'images\summer.gif')
    summer_label = Button(master, image=summer_img, command=lambda: output_label.config(text='Summer'))
    summer_label.image = summer_img
    summer_label.grid(row=0, column=1)

    # Fall: row 1, column 0
    fall_img = PhotoImage(file=img_path+'images/fall.gif')
    fall_label = Button(master, image=fall_img, command=lambda: output_label.config(text='Fall'))
    fall_label.image = fall_img
    fall_label.grid(row=1, column=0)

    # Winter: row 1, column 1
    winter_img = PhotoImage(file=img_path+'images/winter.gif')
    winter_label = Button(master, image=winter_img, command=lambda: output_label.config(text='Winter'))
    winter_label.image = winter_img
    winter_label.grid(row=1, column=1)

def main():
    # initialize window
    root = Tk()
    # initialize window
    init_window(root)
    # Tkinter event loop.
    root.mainloop()

if __name__ == ('__main__'):
    main()
