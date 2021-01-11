#Exercise 19.1

'''from tkinter import messagebox
import tkinter as tk
class Window1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Press Me', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)


 #Creates Window2 with button2 that displays a "Nice Job" message
class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button2 = tk.Button(self.frame, text = 'Now Press Me', width = 25, command = self.new_window)
        self.button2.pack()
        self.frame.pack()
    def new_window(self):
        msg=messagebox.showinfo(message="Nice Job!")
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()'''


#Exercise 19.2

'''from tkinter import *
from tkinter import Canvas

top = Tk()
top.geometry("300x250")
def circleWindow():
    C = Canvas(top,bg='blue', height=250, width=300)
    oval = C.create_oval(70, 30, 200, 200, fill="Red")
    C.pack()
b = Button(top, text= "Click me for Graph", command = circleWindow)
b.place(x=90,y=100)
top.mainloop()'''


#Exercise 19.3

'''from swampy.Gui import *

g = Gui()
g.title('circle demo')
canvas = g.ca(width=500, height=500, bg='white')
circle = None


def callback1():
    """called when the user presses 'Create circle' """
    global circle
    circle = canvas.circle([0, 0], 100)


def callback2():
    """called when the user presses 'Change color' """

    # if the circle hasn't been created yet, do nothing
    if circle == None:
        return

    # get the text from the entry and try to change the circle's color
    color = entry.get()
    try:
        circle.config(fill=color)
    except TclError, message:
        # probably an unknown color name
        print message


# create the widgets
g.bu(text='Create circle', command=callback1)
entry = g.en()
g.bu(text='Change color', command=callback2)

g.mainloop()'''




#Exercise 19.4

'''import os, sys
from Gui import *
import Image as PIL      # to avoid name conflict with Tkinter
import ImageTk

class ImageBrowser(Gui):
    """An image browser that scans the files in a given directory and
    displays any images that can be read by PIL.
    """
    def __init__(self):
        Gui.__init__(self)

        # clicking on the image breaks out of mainloop
        self.button = self.bu(command=self.quit, relief=FLAT)

    def image_loop(self, dirname='.'):
        """loop through the files in (dirname), displaying
        images and skipping files PIL can't read.
        """
        files = os.listdir(dirname)
        for file in files:
            try:
                self.show_image(file)
                print file
                self.mainloop()
            except IOError:
                continue
            except:
                break

    def show_image(self, filename):
        """Use PIL to read the file and ImageTk to convert
        to a PhotoImage, which Tk can display.
        """
        image = PIL.open(filename)
        self.tkpi = ImageTk.PhotoImage(image)
        self.button.config(image=self.tkpi)

def main(script, dirname='.'):
    g = ImageBrowser()
    g.image_loop(dirname)

if __name__ == '__main__':
    main(*sys.argv)
'''





