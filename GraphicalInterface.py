# ICS483 Group Project
# Authors: Kekeli D Akouete, Vang Uni A
# Implementing encryption in an application

from tkinter import filedialog
from tkinter import *
from tkinter import messagebox


def saveAs():
    filedialog.asksaveasfilename()


def openfile():
    myFile = filedialog.askopenfilename()
    Label(root, text=myFile).pack()


def showhelp():
    with open("help.txt", "r") as helper:
        msg = helper.read()
    messagebox.showinfo(title="About", message=msg)
    return


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=openfile)
        fileMenu.add_command(label="Save As", command=saveAs)
        fileMenu.add_command(label="Create File")
        fileMenu.add_command(label="Exit", command=quitApp)

        actionMenu = Menu(menu)
        menu.add_cascade(label="Action", menu=actionMenu)
        actionMenu.add_command(label="Decrypt")
        actionMenu.add_command(label="Encrypt")
        actionMenu.add_command(label="Generate key")

        helpMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About", command=showhelp)

        displayArea = Label(self.master, text="DISPLAY", justify=LEFT)
        displayArea.pack()

        status = Label(self.master, text="Cryptographer_1.0 \u00AE All rights reserved", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)


def quitApp():
    if messagebox.askokcancel("Confirm Exit", "Do you really wish to quit?"):
        root.destroy()


root = Tk()
crypto_app = Window(root)
root.wm_title("Cryptographer1.0")
root.geometry("650x350")
root.protocol("WM_DELETE_WINDOW", quitApp)
root.mainloop()