from tkinter import *
from tkinter import filedialog 
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb

root=Tk()

root.title("Steganography - Hide a Screte Text Message in an Image")
root.geometry("700x500+150+180")

root.resizable(False,False)
root.configure(bg='#2f4155')

#icon
image_icon=PhotoImage(file='logo.jpg')
root.iconphoto(False,image_icon)

root.mainloop()