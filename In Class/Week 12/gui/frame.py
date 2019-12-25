# import tkinter
from tkinter import *

def init_window(master):
    img_path = 'D:\Documents\KMITL\\06026104_computer_programming\scripts\gui\\'

    # fixed size window
    master.resizable(width=False, height=False)
    # window title
    master.title("Tkinter GUI: Frame")

    # Bottom frame
    bottomFrame = Frame(master, height=50)
    bottomFrame.pack(side='bottom')
    output_label = Label(bottomFrame, text='Selected season: ')
    output_label.pack()

    # Top frame
    topFrame = Frame(master)
    topFrame.pack()

    spring_img = PhotoImage(file=img_path+'images\spring.gif')
    spring_label = Button(topFrame, image=spring_img, command=lambda: output_label.config(text='Spring'))
    spring_label.image = spring_img
    spring_label.pack(side='left')

    summer_img = PhotoImage(file=img_path+'images\summer.gif')
    summer_label = Button(topFrame, image=summer_img, command=lambda: output_label.config(text='Summer'))
    summer_label.image = summer_img
    summer_label.pack(side='right')

    # Middle frame
    middleFrame = Frame(master)
    middleFrame.pack()

    fall_img = PhotoImage(file=img_path+'images/fall.gif')
    fall_label = Button(middleFrame, image=fall_img, command=lambda: output_label.config(text='Fall'))
    fall_label.image = fall_img
    fall_label.pack(side='left')

    winter_img = PhotoImage(file=img_path+'images/winter.gif')
    winter_label = Button(middleFrame, image=winter_img, command=lambda: output_label.config(text='Winter'))
    winter_label.image = winter_img
    winter_label.pack(side='right')

def main():
    # initialize window
    root = Tk()
    # initialize window
    init_window(root)
    # Tkinter event loop:
    # The program will stay in the event loop until we close the window.
    root.mainloop()

if __name__ == ('__main__'):
    main()
