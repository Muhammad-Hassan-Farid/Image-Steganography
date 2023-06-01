from tkinter import *
from tkinter import filedialog 
from PIL import Image,ImageTk
import os
from stegano import lsb

root=Tk()

root.title("Steganography - Hide a Screte Text Message in an Image")
root.geometry("700x500+400+180")
root.resizable(False,False)
root.configure(bg='skyblue')

# open image function
def showimage():
    global filename
    filename=filedialog.askopenfilename(initialfile=os.getcwd(),
                                        title="Select Image File",
                                        filetype=(("PNG File","*.png"),
                                                  ("JPG File","*.jpg"),
                                                  ("All file","*.text")
                                        ))
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=250,height=250)
    lb1.image=img
    
# Hide Text function  
def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename), message)
   
# Show image function
def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END, clear_message)
   
# Save image fuction 
def save():
    secret.save("hidden.png")

#icon
image_icon=PhotoImage(file='icon.png')
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="Logo2.png")
Label(root,image=logo,bg="skyblue").place(x=10,y=13)

Label(root,text="Image Steganography",bg="skyblue",fg="black",font="arial 25 bold").place(x=70,y=20)

#first Frame
f = Frame(root,bd=3,bg="black",width="340",height=280,relief=GROOVE)
f.place(x=10,y=80)

lb1 = Label(f,bg="black")
lb1.place(x=40,y=10)

#second frame
frame2 = Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20", bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=280)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg="skyblue",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="arail 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arail 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="skyblue",fg='black').place(x=20,y=5)

#Fourth Frame
frame4=Frame(root,bd=3,bg="skyblue",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Image",width=10,height=2,font="arail 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Image",width=10,height=2,font="arail 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="skyblue",fg='black').place(x=20,y=5)


root.mainloop()