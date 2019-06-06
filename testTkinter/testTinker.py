import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os
from tkinter import colorchooser

def main():
    window = tk.Tk()
    window.title('test')
    window.geometry("400x400")

    my_label = ttk.Label(window, text="Hello World!")
    my_label.place(x=50,y=50)
    #my_label.grid(row=1, column=1)

    window.mainloop()

def getMessages():
    messagebox.showinfo("Information","Informative message")
    messagebox.showerror("Error", "Error message")
    messagebox.showwarning("Warning","Warning message")

def getQuestions():
    answer = messagebox.askokcancel("Question","Do you want to open this file?")
    answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
    answer = messagebox.askyesno("Question","Do you like Python?")
    answer = messagebox.askyesnocancel("Question", "Continue playing?")


def getSimpleDialog():
    application_window = tk.Tk()
    answer = simpledialog.askstring("Input","What is you first name?",parent=application_window)
    if answer:
        print("Your first name is ",answer)
    else:
        print("You don't have a first name?")


def getFileDialog():
    application_window = tk.Tk()

    my_filetypes = [('all files','.*'),('text files','.txt')]

    answer = filedialog.askdirectory(parent=application_window,initialdir=os.getcwd(),title="Please select a folder:")

    answer = filedialog.askopenfilename(parent=application_window,initialdir=os.getcwd(),title="Please select a file:",filetypes=my_filetypes)

    answer = filedialog.askopenfilenames(parent=application_window,initialdir=os.getcwd(),title="Please select one or more files:",filetypes=my_filetypes)

    answer = filedialog.asksaveasfilename(parent=application_window,initialdir=os.getcwd(),title="Please select a file name for saving:",filetypes=my_filetypes)

def getColorChooser():
    application_window = tk.Tk()
    rgb_color, web_color = colorchooser.askcolor(parent=application_window,initialcolor=(255, 0, 0))
    print(rgb_color,web_color)

#getColorChooser()
#getFileDialog()
    
main()
