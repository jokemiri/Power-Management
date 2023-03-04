import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Create an instance of tkinter frame or window
root=Tk()
# Set the size of the tkinter window
root.geometry("300x300")
root.title("Power Options")#give title to the window
head=Label(root, text="PC Power Options", font=('Calibri 15'), bg='white', fg='#1e81b0')# a label
head.place(x=50, y=10)
root.resizable(0, 0)
root.configure(bg="white")

#window_icon
window_icon = PhotoImage(file="icon.png")
root.iconphoto(False, window_icon)


# Label(root, width=120, height=10, bg="#52bbd8").pack()

#frame
# frame = Frame(root, width=750, height=420, bg='#d6e9ee')
# frame.place(x=25, y=10)

logo = PhotoImage(file='logo.png')
Label(root, image=logo, bg='white').place(x=10, y=10)

# Label(frame, text='Power Options', font='Calibri 18 bold', bg='#d6e9ee').place(x=100, y=20)

#color1
# colors=Canvas(frame, bg='#1e81b0', width=150, height=265, bd=0)
# colors.place(x=20, y=140)

def Shutdown():#function to shutdown
    os.system("shutdown /s /t 0")

def Restart():#function to restart
    os.system("shutdown /r /t 0")

def logout():#function to logout
    os.system("shutdown /l /t 0")

shutdown_button = PhotoImage(file="shutdown.png")
restart_button = PhotoImage(file="restart.png")
logout_button = PhotoImage(file="logout.png")


#buttons
Button(root,text='Shutdown',command=Shutdown, font=('normal',11), bg='white', image=shutdown_button).place(x= 20, y=100)
Button(root,text='Restart',command=Restart,font=('normal',11), bg='white', image=restart_button).place(x= 220, y=100)
Button(root,text='Logout',command=logout,font=('normal',11), bg='white', image=logout_button).place(x= 120, y=100)

root.mainloop()