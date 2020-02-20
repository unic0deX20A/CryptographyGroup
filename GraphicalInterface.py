from tkinter import filedialog
from tkinter import *
from tkinter import messagebox


def saveAs():
    filedialog.asksaveasfilename()


def openfile():
    myFile = filedialog.askopenfilename()
    selection = Label(root, text=myFile).pack()
    return


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Open", command=openfile)
        fileMenu.add_command(label="Save As", command=saveAs)
        fileMenu.add_command(label="Create File")
        fileMenu.add_command(label="Exit", command=quitApp)
        menu.add_cascade(label="File", menu=fileMenu)

        actionMenu = Menu(menu)
        actionMenu.add_command(label="Decrypt")
        actionMenu.add_command(label="Encrypt")
        actionMenu.add_command(label="Generate key")
        menu.add_cascade(label="Action", menu=actionMenu)

        displayArea = Label(self.master, text="DISPLAY", justify=LEFT)
        displayArea.pack()


def quitApp():
    if messagebox.askokcancel("Confirm Exit", "Do you really wish to quit?"):
        root.destroy()


root = Tk()
crypto_app = Window(root)
root.wm_title("Cryptographer1.0")
root.geometry("650x350")
root.protocol("WM_DELETE_WINDOW", quitApp)
root.mainloop()
