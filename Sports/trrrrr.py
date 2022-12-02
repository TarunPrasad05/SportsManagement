from tkinter import *
import tkinter.messagebox as messagebox

def teamexit():
    messagebox.showinfo("Thank YOU", "BYEEEE")
    root2.destroy()


def teamregister():
    id = team_id.get()
    passwo = password.get()
    nam = team_name.get()
    print("HELLO" + passwo)
    # print(a)

    team_id.set("")
    password.set("")
    team_name.set("")


root2 = Tk()
root2.geometry('400x300')

team_id = StringVar()
password = StringVar()
team_name = StringVar()

head2 = Label(root2, text="===NEW REGISTRATION===").place(x=110, y=50)
head2_1 = Label(root2, text=" Team ID ").place(x=70, y=100)
head2_2 = Label(root2, text=" Password ").place(x=70, y=150)
head2_3 = Label(root2, text=" Team Name ").place(x=70, y=200)

entry2_1 = Entry(root2, textvariable=team_id).place(x=175, y=100)
entry2_2 = Entry(root2, textvariable=password).place(x=175, y=150)
entry2_3 = Entry(root2, textvariable=team_name).place(x=175, y=200)

b2_1 = Button(root2, text="Register", borderwidth=4, command=teamregister)
b2_1.place(x=100, y=250)

b2_2 = Button(root2, text="Exit", borderwidth=4, command=teamexit)
b2_2.place(x=200, y=250)

root2.mainloop()
