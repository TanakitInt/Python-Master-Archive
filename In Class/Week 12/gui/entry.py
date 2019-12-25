# import tkinter
from tkinter import *

def init_window(master):
    # initialize the window size
    master.geometry('{}x{}'.format(250, 140))
    # fixed size window
    master.resizable(width=False, height=False)
    # window title
    master.title("Tkinter GUI: Entry")

    xLabel = Label(master, text='Input x: ', font=("Helvetica", 14))
    xLabel.grid(row=0, column=0)
    inputX = Entry(master)
    inputX.grid(row=0, column=1)

    yLabel = Label(master, text='Input y: ', font=("Helvetica", 14))
    yLabel.grid(row=1, column=0)
    inputY = Entry(master)
    inputY.grid(row=1, column=1, padx=5)

    resultLabel = Label(master, text='x+y: ', font=("Helvetica", 14))
    resultLabel.grid(row=2, column=0)
    result = Entry(master, state='readonly')
    result.grid(row=2, column=1)

    errorLabel = Label(master, font=("Helvetica", 14))
    errorLabel.grid(row=4, column=0, columnspan=2)

    calButton = Button(master, text='Caluculate', command=lambda: cal_summation(inputX, inputY, result, errorLabel))
    calButton.grid(row=3, column=0, padx=20)

    cancelButton = Button(master, text='Cancel', command=lambda: clearEntries(inputX, inputY, result, errorLabel))
    cancelButton.grid(row=3, column=1)

def cal_summation(inputX, inputY, result, errorLabel):
    valid_x = False
    try:
        # get the current contents of the entry field as string
        num_x = eval(inputX.get())
        valid_x = True
    except:
        errorLabel.config(text='Invalid input X.')

    valid_y = False
    try:
        # get the current contents of the entry field as string
        num_y = eval(inputY.get())
        valid_y = True
    except:
        errorLabel.config(text='Invalid input Y.')

    if valid_x and valid_y:
        result.config(state='normal')
        result.delete(0, END)
        result.insert(0, num_x+num_y)
        result.config(state='readonly')
        errorLabel.config(text='')

def clearEntries(inputX, inputY, result, errorLabel):
    inputX.delete(0,END)
    inputY.delete(0, END)
    result.config(state='normal')
    result.delete(0, END)
    result.config(state='readonly')
    errorLabel.config(text='')

def main():
    # initialize window
    root = Tk()
    # initialize window
    init_window(root)
    #Tkinter event loop.
    root.mainloop()

if __name__ == ('__main__'):
    main()
