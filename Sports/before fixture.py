import pyodbc
from tkinter import *
import tkinter.messagebox as messagebox

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-SMC51SMG;'
                      'Database=league;'
                      'Trusted_Connection=yes;')
root1 =  Tk()
root1.title("MINI PROJECT")
root1.geometry('400x250')

def register():

    def teamexit():
        messagebox.showinfo("Thank YOU", "BYEEEE")
        root2.destroy()

    def teamregister():

        a = team_id.get()
        b = password.get()
        c = team_name.get()
        cur2_1 = conn.cursor()
        ins2 = "select * from team where t_id= %d or t_name='%s'" %(a,c)
        cur2_1.execute(ins2)
        count=0
        for i in cur2_1:
            count+=1
        if count>0:
            messagebox.showinfo("Unsuccesfull", "Team id or Team Name already exists! Try again")
            root2.destroy()
            return
        else:
            cur2=conn.cursor()
            ins="insert into team(t_id,password,t_name) values(%d,'%s','%s')" %(a,b,c)
            cur2.execute(ins)
            conn.commit()
            team_id.set("")
            password.set("")
            team_name.set("")

    root2 = Tk()
    root2.geometry('400x300')

    team_id = IntVar(root2)
    password = StringVar(root2)
    team_name = StringVar(root2)

    head2 = Label(root2,text="===NEW REGISTRATION===").place(x=110,y=50)
    head2_1 = Label(root2,text=" Team ID ").place(x=70,y=100)
    head2_2 = Label(root2,text=" Password ").place(x=70,y=150)
    head2_3 = Label(root2,text=" Team Name ").place(x=70,y=200)

    entry2_1 = Entry(root2,textvariable = team_id).place(x=175,y=100)
    entry2_2 = Entry(root2,textvariable = password,show='*').place(x=175,y=150)
    entry2_3 = Entry(root2,textvariable = team_name).place(x=175,y=200)

    b2_1 = Button(root2,text="Register",borderwidth = 4, command = teamregister)
    b2_1.place(x=100,y=250)

    b2_2 = Button(root2,text="Exit",borderwidth = 4, command = teamexit)
    b2_2.place(x=200, y=250)

    root2.mainloop()

def login():
    root3 = Tk()
    root3.geometry('400x250')

    head3 = Label(root3, text="===Team login===").place(x=120, y=50)
    head3_1 = Label(root3, text="Team ID").place(x=75, y=100)
    head3_2 = Label(root3, text="Password").place(x=75, y=150)

    def logininto():
        team_id = t_id.get()
        p_word = pass_word.get()
        t_id.set("")
        pass_word.set("")
        cur3_1=conn.cursor()
        ins1="select t_name from team where t_id=%d and password='%s'" %(team_id,p_word)
        cur3_1.execute(ins1)
        c=0
        for i in cur3_1:
            ans=list(i)
            c+=1
        if c==1:
            messagebox.showinfo("Team login", "successfully logged In")
            root3.destroy()
            root4 = Tk()
            root4.geometry('400x250')

            head4 = Label(root4, text="===Team Details===").place(x=120, y=40)
            head4_1 = Label(root4, text=team_id).place(x=175, y=80)
            head4_2 = Label(root4, text=ans[0]).place(x=75, y=80)
            head4_3 = Label(root4, text="Player Name").place(x=75, y=120)
            head4_4 = Label(root4, text="Player ID").place(x=75, y=160)

            def enroll():
                pid = p_id.get()
                pname = p_name.get()
                cur4_1=conn.cursor()
                cur4_2=conn.cursor()
                ins4_1="select * from player where p_id=%d"%pid
                cur4_1.execute(ins4_1)
                count1 = 0
                for i in cur4_1:
                    count1 += 1
                ins4_2="select * from player where t_id=%d"%team_id
                cur4_2.execute(ins4_2)
                count2=0
                for j in cur4_2:
                    count2+=1
                if count1>=1:
                    messagebox.showinfo("Team Registration", "Player id already present")
                elif count2>=15:
                    messagebox.showinfo("Team Registration", "Team has 15 members!")
                else:
                    cur4_3=conn.cursor()
                    ins4_3="insert into player values(%d,'%s',%d,0,0)"%(pid,pname,team_id)
                    cur4_3.execute(ins4_3)
                    conn.commit()
                    messagebox.showinfo("Team Details", "successfully Enrolled")
                p_id.set("")
                p_name.set("")

            def close():
                messagebox.showinfo("Team Details", "THANK YOU!!!")
                root4.destroy()

            p_name = StringVar(root4)
            p_id = IntVar(root4)

            entry4_1 = Entry(root4, textvariable=p_name).place(x=175, y=120)
            entry4_2 = Entry(root4, textvariable=p_id).place(x=175, y=160)

            b3_1 = Button(root4, text="  ENROLL PLAYER  ", borderwidth=4, command=enroll)
            b3_1.place(x=75, y=200)
            b3_2 = Button(root4, text="  EXIT  ", borderwidth=4, command=close)
            b3_2.place(x=250, y=200)

            root4.mainloop()
        else:
            messagebox.showinfo("Team login", "Invalid credentials!")
            root3.destroy()

    def loginexit():
        messagebox.showinfo("Team login", "THANK YOU!!!")
        root3.destroy()

    t_id = IntVar(root3)
    pass_word = StringVar(root3)

    entry3_1 = Entry(root3, textvariable=t_id).place(x=175, y=100)
    entry3_2 = Entry(root3, textvariable=pass_word, show='*').place(x=175, y=150)

    b3_1 = Button(root3, text="  LOGIN  ", borderwidth=4, command=logininto)
    b3_1.place(x=75, y=200)
    b3_2 = Button(root3, text="  EXIT  ", borderwidth=4, command=loginexit)
    b3_2.place(x=175, y=200)

    root3.mainloop()

def fixtures():
    print("Fix")


head1 = Label(root1,text="===FOOTBALL LEAGUE===").place(x=125,y=50)

b1_1=Button(root1,text="Team Registration",borderwidth=4,command=register)
b1_1.place(x=25,y=120)

b1_2=Button(root1,text="Team Login",borderwidth=4,command=login)
b1_2.place(x=175,y=120)

b1_3=Button(root1,text="Fixtures",borderwidth=4,command=fixtures)
b1_3.place(x=300,y=120)


root1.mainloop()
