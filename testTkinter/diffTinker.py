import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os
from tkinter import colorchooser
import difflib
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.listName=["1","2"]
        self.mm=''

    def initWidgets(self):
        ttk.Button(self.master,
        text="文件1",
        command=lambda : self.selectFile(self.listName,0)).place(x=50,y=150)
        
        ttk.Button(self.master,
        text="文件2",
        command=lambda : self.selectFile(self.listName,1)).place(x=280,y=150)

        ttk.Button(self.master,
        text="文件比较",
        command=self.diffFile).place(x=160,y=260)


        self.e1 = tk.Entry(self.master,textvariable = self.mm)
        self.e1.place(x=50,y=50)
        self.e1.focus_set()
        self.mm="abc"


        # self.e2 = tk.Entry(self.master,textvariable = self.listName[1])
        # self.e2.place(x=260,y=50)

    def selectFile(self, file,tag):
        my_filetypes = [('all files','.*'),('text files','.txt')]
        file[tag] = filedialog.askopenfilename(parent=self.master,initialdir=os.getcwd(),title="Please select a file:",filetypes=my_filetypes)
        print(file)

    def diffFile(self):
        for file1 in self.listName:
            if not os.path.exists(file1):
                messagebox.showerror("Error", "请检查文件选择")

        d=difflib.HtmlDiff()
        file_obj = open("diff.html","w")
        with open(self.listName[0], 'r') as f1:
            with open(self.listName[1], 'r') as f2:
                file_obj.write(d.make_file(f1.readlines(),f2.readlines()))               
        file_obj.close()
        print("diff")
          


# def main():
#     window = tk.Tk()
#     window.title('test')
#     window.geometry("400x400")

#     my_label = ttk.Label(window, text="Hello World!")
#     my_label.place(x=50,y=50)
#     #my_label.grid(row=1, column=1)

#     window.mainloop()

def testdif():
    d=difflib.HtmlDiff()
    file_obj = open("diff.html","w")
    with open('text1.txt', 'r') as f1:
        with open('text2.txt', 'r') as f2:
            file_obj.write(d.make_file(f1.readlines(),f2.readlines()))
                
    file_obj.close()
        
def __main__():
    window = tk.Tk()
    window.title('test')
    window.geometry("500x300")
    App(window)
    window.mainloop()


    
__main__()
    