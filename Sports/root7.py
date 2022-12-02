import pyodbc
from tkinter import *
import tkinter.messagebox as messagebox

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-SMC51SMG;'
                      'Database=league;'
                      'Trusted_Connection=yes;')
root1 = Tk()
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
        ins2 = "select * from team where t_id= %d or t_name='%s'" % (a, c)
        cur2_1.execute(ins2)
        count = 0
        for i in cur2_1:
            count += 1
        if count > 0:
            messagebox.showinfo("Unsuccesfull", "Team id or Team Name already exists! Try again")
            root2.destroy()
            return
        else:
            cur2 = conn.cursor()
            ins = "insert into team(t_id,password,t_name) values(%d,'%s','%s')" % (a, b, c)
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

    head2 = Label(root2, text="===NEW REGISTRATION===").place(x=110, y=50)
    head2_1 = Label(root2, text=" Team ID ").place(x=70, y=100)
    head2_2 = Label(root2, text=" Password ").place(x=70, y=150)
    head2_3 = Label(root2, text=" Team Name ").place(x=70, y=200)

    entry2_1 = Entry(root2, textvariable=team_id).place(x=175, y=100)
    entry2_2 = Entry(root2, textvariable=password, show='*').place(x=175, y=150)
    entry2_3 = Entry(root2, textvariable=team_name).place(x=175, y=200)

    b2_1 = Button(root2, text="Register", borderwidth=4, command=teamregister)
    b2_1.place(x=100, y=250)

    b2_2 = Button(root2, text="Exit", borderwidth=4, command=teamexit)
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
        cur3_1 = conn.cursor()
        ins1 = "select t_name from team where t_id=%d and password='%s'" % (team_id, p_word)
        cur3_1.execute(ins1)
        c = 0
        for i in cur3_1:
            ans = list(i)
            c += 1
        if c == 1:
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
                cur4_1 = conn.cursor()
                cur4_2 = conn.cursor()
                ins4_1 = "select * from player where p_id=%d and t_id=%d" % (pid, team_id)
                cur4_1.execute(ins4_1)
                count1 = 0
                for i in cur4_1:
                    count1 += 1
                ins4_2 = "select * from player where t_id=%d" % team_id
                cur4_2.execute(ins4_2)
                count2 = 0
                for j in cur4_2:
                    count2 += 1
                if count1 >= 1:
                    messagebox.showinfo("Team Registration", "Player id already present")
                elif count2 >= 15:
                    messagebox.showinfo("Team Registration", "Team has 15 members!")
                else:
                    cur4_3 = conn.cursor()
                    ins4_3 = "insert into player values(%d,'%s',%d,0,0)" % (pid, pname, team_id)
                    cur4_3.execute(ins4_3)
                    conn.commit()
                    messagebox.showinfo("Team Details", "successfully Enrolled")
                p_id.set("")
                p_name.set("")

            def close():
                messagebox.showinfo("Team Details", "THANK YOU!!!")
                root4.destroy()

            def disp():
                '''root10= Tk()
                root10.geometry('400x600')'''
                cur10_1 = conn.cursor()
                ins10_1 = "select * from team where t_id=%d" % team_id
                cur10_1.execute(ins10_1)
                for i in cur10_1:
                    i = list(i)
                    print(
                        "ID: " + str(i[0]) + "  Name: " + i[2] + "  Match played: " + str(i[3]) + "  Match won: " + str(
                            i[4]))
                cur10_1.close()
                cur10_2 = conn.cursor()
                ins10_2 = "select * from player where t_id=%d" % team_id
                cur10_2.execute(ins10_2)
                count = 0
                ans = []
                for j in cur10_2:
                    j = list(j)
                    print(
                        "ID: " + str(j[0]) + "  Name: " + j[1] + "  Match played: " + str(j[3]) + "  Match won: " + str(
                            j[4]))
                cur10_2.close()
                # l1= Label(root10,text="ID: "+str(i[0])+"  Name: "+i[2]+"  Match played: "+str(i[3])+"  Match won: "+str(i[4])).place(x=50,y=50)
                # root10.mainloop()

            p_name = StringVar(root4)
            p_id = IntVar(root4)

            entry4_1 = Entry(root4, textvariable=p_name).place(x=175, y=120)
            entry4_2 = Entry(root4, textvariable=p_id).place(x=175, y=160)

            b3_1 = Button(root4, text="  ENROLL PLAYER  ", borderwidth=4, command=enroll)
            b3_1.place(x=75, y=200)
            b3_2 = Button(root4, text="  EXIT  ", borderwidth=4, command=close)
            b3_2.place(x=220, y=200)
            b3_3 = Button(root4, text=" Display ", borderwidth=4, command=disp)
            b3_3.place(x=300, y=200)

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
    cur5_1 = conn.cursor()
    ins5_1 = "select * from team"
    cur5_1.execute(ins5_1)
    count = 0
    for i in cur5_1:
        count += 1
    if count < 8:
        messagebox.showinfo("Teams Left", "Teams need to register!")
    elif count > 8:
        messagebox.showinfo("Team overflow", "Only 8 teams can participate")
    else:
        cur5_2 = conn.cursor()
        ins5_2 = "select t_id from team"
        cur5_2.execute(ins5_2)
        n = []
        for i in cur5_2:
            t = list(i)
            n.append(t[0])
        cur5_3 = conn.cursor()
        for j in range(4):
            ins5_3 = "insert into fixture(g_no,t1_id,t2_id) values(%d,%d,%d)" % (j + 1, n[j * 2 + 0], n[j * 2 + 1])
            cur5_3.execute(ins5_3)
            conn.commit()

        root5 = Tk()
        root5.geometry('500x750')

        head5 = Label(root5, text="===FIXTURES===").place(x=175, y=50)
        head5_1 = Label(root5, text="===Knockouts===").place(x=175, y=100)
        head5_2 = Label(root5, text="Team1 ID").place(x=75, y=150)
        head5_3 = Label(root5, text="  vs").place(x=200, y=150)
        head5_4 = Label(root5, text="Team2 ID").place(x=250, y=150)
        head5_5 = Label(root5, text="===SEMIS===").place(x=175, y=400)
        head5_6 = Label(root5, text="===FINAL===").place(x=175, y=550)
        head5_7 = Label(root5, text="   vs  ").place(x=200, y=200)
        head5_14 = Label(root5, text=n[0]).place(x=75, y=200)
        head5_15 = Label(root5, text=n[1]).place(x=250, y=200)
        head5_8 = Label(root5, text="   vs  ").place(x=200, y=250)
        head5_16 = Label(root5, text=n[2]).place(x=75, y=250)
        head5_17 = Label(root5, text=n[3]).place(x=250, y=250)
        head5_9 = Label(root5, text="   vs  ").place(x=200, y=300)
        head5_18 = Label(root5, text=n[4]).place(x=75, y=300)
        head5_19 = Label(root5, text=n[5]).place(x=250, y=300)
        head5_10 = Label(root5, text="  vs ").place(x=200, y=350)
        head5_20 = Label(root5, text=n[6]).place(x=75, y=350)
        head5_21 = Label(root5, text=n[7]).place(x=250, y=350)

        head5_11 = Label(root5, text="  vs ").place(x=200, y=450)
        head5_22 = Label(root5, text="  SFT1  ").place(x=75, y=450)
        head5_23 = Label(root5, text="  SFT2  ").place(x=250, y=450)
        head5_12 = Label(root5, text="  vs ").place(x=200, y=500)
        head5_24 = Label(root5, text="  SFT3  ").place(x=75, y=500)
        head5_25 = Label(root5, text="  SFT4  ").place(x=250, y=500)
        head5_13 = Label(root5, text="  vs ").place(x=200, y=600)
        head5_26 = Label(root5, text="  FT1  ").place(x=75, y=600)
        head5_27 = Label(root5, text="  FT2  ").place(x=250, y=600)

        def play():

            cur6_1 = conn.cursor()
            ins6_1 = "select * from fixture"
            cur6_1.execute(ins6_1)
            for x in cur6_1:
                n = (list(x))
                if n[3] == None:
                    break
            cur6_1.close()

            cur6_2 = conn.cursor()
            ins6_2 = "select p_id from player where t_id = %d " % n[1]
            cur6_2.execute(ins6_2)
            c1 = 0
            for y in cur6_2:
                c1 += 1
            cur6_2.close()
            cur6_3 = conn.cursor()
            ins6_3 = "select p_id from player where t_id = %d " % n[2]
            cur6_3.execute(ins6_3)
            c2 = 0
            for z in cur6_3:
                c2 += 1
            cur6_3.close()

            if c1 < 11 or c2 < 11:
                messagebox.showinfo("CANT PLAY", "Team members are insufficient")

            else:
                root6 = Tk()
                root6.geometry('750x1000')

                head6 = Label(root6, text="===MATCH===").place(x=175, y=50)
                head6_1 = Label(root6, text=n[1]).place(x=75, y=100)
                head6_2 = Label(root6, text=n[2]).place(x=250, y=100)
                head6_3 = Label(root6, text="  vs").place(x=200, y=100)
                head6_4 = Label(root6, text="WINNER").place(x=75, y=700)

                def over():
                    t1 = []
                    t1.append(t1p1_id.get())
                    t1.append(t1p2_id.get())
                    t1.append(t1p3_id.get())
                    t1.append(t1p4_id.get())
                    t1.append(t1p5_id.get())
                    t1.append(t1p6_id.get())
                    t1.append(t1p7_id.get())
                    t1.append(t1p8_id.get())
                    t1.append(t1p9_id.get())
                    t1.append(t1p10_id.get())
                    t1.append(t1p11_id.get())

                    t2 = []
                    t2.append(t2p1_id.get())
                    t2.append(t2p2_id.get())
                    t2.append(t2p3_id.get())
                    t2.append(t2p4_id.get())
                    t2.append(t2p5_id.get())
                    t2.append(t2p6_id.get())
                    t2.append(t2p7_id.get())
                    t2.append(t2p8_id.get())
                    t2.append(t2p9_id.get())
                    t2.append(t2p10_id.get())
                    t2.append(t2p11_id.get())

                    if len(t1) != len(set(t1)) or len(t2) != len(set(t2)):
                        messagebox.showinfo("CANT PLAY", "Duplicate Players")
                        t1p1_id.set("")
                        t1p2_id.set("")
                        t1p3_id.set("")
                        t1p4_id.set("")
                        t1p5_id.set("")
                        t1p6_id.set("")
                        t1p7_id.set("")
                        t1p8_id.set("")
                        t1p9_id.set("")
                        t1p10_id.set("")
                        t1p11_id.set("")

                        t2p1_id.set("")
                        t2p2_id.set("")
                        t2p3_id.set("")
                        t2p4_id.set("")
                        t2p5_id.set("")
                        t2p6_id.set("")
                        t2p7_id.set("")
                        t2p8_id.set("")
                        t2p9_id.set("")
                        t2p10_id.set("")
                        t2p11_id.set("")
                    else:
                        win_ner = winner.get()
                        cur6_4 = conn.cursor()
                        ins6_4 = "update team set m_played=1 where t_id=%d" % n[1]
                        cur6_4.execute(ins6_4)
                        conn.commit()
                        cur6_4.close()
                        cur6_5 = conn.cursor()
                        ins6_5 = "update team set m_played=1 where t_id=%d" % n[2]
                        cur6_5.execute(ins6_5)
                        conn.commit()
                        cur6_5.close()
                        cur6_6 = conn.cursor()
                        ins6_6 = "update player set g_played=1 where t_id=%d " % n[1]
                        cur6_6.execute(ins6_6)
                        conn.commit()
                        cur6_6.close()
                        cur6_7 = conn.cursor()
                        ins6_7 = "update player set g_played=1 where t_id=%d " % n[2]
                        cur6_7.execute(ins6_7)
                        conn.commit()
                        cur6_7.close()
                        cur6_8 = conn.cursor()
                        ins6_8 = "update fixture set win_id=%d where g_no=%d " % (win_ner, n[0])
                        cur6_8.execute(ins6_8)
                        conn.commit()
                        cur6_8.close()
                        cur6_9 = conn.cursor()
                        ins6_9 = "update team set m_won=1 where t_id=%d " % win_ner
                        cur6_9.execute(ins6_9)
                        conn.commit()
                        cur6_9.close()
                        cur6_10 = conn.cursor()
                        ins6_10 = "update player set g_won=1 where t_id=%d " % win_ner
                        cur6_10.execute(ins6_10)
                        conn.commit()
                        cur6_10.close()
                        t1p1_id.set("")
                        t1p2_id.set("")
                        t1p3_id.set("")
                        t1p4_id.set("")
                        t1p5_id.set("")
                        t1p6_id.set("")
                        t1p7_id.set("")
                        t1p8_id.set("")
                        t1p9_id.set("")
                        t1p10_id.set("")
                        t1p11_id.set("")
                        t2p1_id.set("")
                        t2p2_id.set("")
                        t2p3_id.set("")
                        t2p4_id.set("")
                        t2p5_id.set("")
                        t2p6_id.set("")
                        t2p7_id.set("")
                        t2p8_id.set("")
                        t2p9_id.set("")
                        t2p10_id.set("")
                        t2p11_id.set("")
                        winner.set("")

                        if n[0] == 1:
                            cur6_11 = conn.cursor()
                            ins6_11 = "insert into fixture(g_no,t1_id) values(5,%d)" % win_ner
                            cur6_11.execute(ins6_11)
                            cur6_11.commit()
                            cur6_11.close()
                            # root5.head5_22.config(text=win_ner)
                            # root5.head5_22.update()
                        elif n[0] == 2:
                            cur6_12 = conn.cursor()
                            ins6_12 = "update fixture set t2_id=%d where g_no=5" % win_ner
                            cur6_12.execute(ins6_12)
                            cur6_12.commit()
                            cur6_12.close()
                            # head5_23.config(text=win_ner)
                        elif n[0] == 3:
                            cur6_13 = conn.cursor()
                            ins6_13 = "insert into fixture(g_no,t1_id) values(6,%d)" % win_ner
                            cur6_13.execute(ins6_13)
                            cur6_13.commit()
                            cur6_13.close()
                            # head5_24.config(text=win_ner)

                        elif n[0] == 4:
                            cur6_14 = conn.cursor()
                            ins6_14 = "update fixture set t2_id=%d where g_no=6" % win_ner
                            cur6_14.execute(ins6_14)
                            cur6_14.commit()
                            cur6_14.close()
                            # head5_25.config(text=win_ner)

                        messagebox.showinfo("MATCH DAY", "MATCH OVER")

                def close():
                    messagebox.showinfo(" MATCH ", "THANK YOU!!!")
                    root6.destroy()

                t1p1_id = IntVar(root6)
                t1p2_id = IntVar(root6)
                t1p3_id = IntVar(root6)
                t1p4_id = IntVar(root6)
                t1p5_id = IntVar(root6)
                t1p6_id = IntVar(root6)
                t1p7_id = IntVar(root6)
                t1p8_id = IntVar(root6)
                t1p9_id = IntVar(root6)
                t1p10_id = IntVar(root6)
                t1p11_id = IntVar(root6)

                t2p1_id = IntVar(root6)
                t2p2_id = IntVar(root6)
                t2p3_id = IntVar(root6)
                t2p4_id = IntVar(root6)
                t2p5_id = IntVar(root6)
                t2p6_id = IntVar(root6)
                t2p7_id = IntVar(root6)
                t2p8_id = IntVar(root6)
                t2p9_id = IntVar(root6)
                t2p10_id = IntVar(root6)
                t2p11_id = IntVar(root6)

                winner = IntVar(root6)

                entry6_1 = Entry(root6, textvariable=t1p1_id).place(x=75, y=150)
                entry6_5 = Entry(root6, textvariable=t1p2_id).place(x=75, y=200)
                entry6_2 = Entry(root6, textvariable=t1p3_id).place(x=75, y=250)
                entry6_3 = Entry(root6, textvariable=t1p4_id).place(x=75, y=300)
                entry6_4 = Entry(root6, textvariable=t1p5_id).place(x=75, y=350)
                entry6_6 = Entry(root6, textvariable=t1p6_id).place(x=75, y=400)
                entry6_7 = Entry(root6, textvariable=t1p7_id).place(x=75, y=450)
                entry6_8 = Entry(root6, textvariable=t1p8_id).place(x=75, y=500)
                entry6_9 = Entry(root6, textvariable=t1p9_id).place(x=75, y=550)
                entry6_10 = Entry(root6, textvariable=t1p10_id).place(x=75, y=600)
                entry6_11 = Entry(root6, textvariable=t1p11_id).place(x=75, y=650)

                entry6_12 = Entry(root6, textvariable=t2p1_id).place(x=250, y=150)
                entry6_13 = Entry(root6, textvariable=t2p2_id).place(x=250, y=200)
                entry6_14 = Entry(root6, textvariable=t2p3_id).place(x=250, y=250)
                entry6_15 = Entry(root6, textvariable=t2p4_id).place(x=250, y=300)
                entry6_16 = Entry(root6, textvariable=t2p5_id).place(x=250, y=350)
                entry6_17 = Entry(root6, textvariable=t2p6_id).place(x=250, y=400)
                entry6_18 = Entry(root6, textvariable=t2p7_id).place(x=250, y=450)
                entry6_19 = Entry(root6, textvariable=t2p8_id).place(x=250, y=500)
                entry6_20 = Entry(root6, textvariable=t2p9_id).place(x=250, y=550)
                entry6_21 = Entry(root6, textvariable=t2p10_id).place(x=250, y=600)
                entry6_22 = Entry(root6, textvariable=t2p11_id).place(x=250, y=650)

                entry6_24 = Entry(root6, textvariable=winner).place(x=150, y=700)

                b6_1 = Button(root6, text="  ||OVER|| ", borderwidth=4, command=over)
                b6_1.place(x=175, y=750)

                root6.mainloop()

        """def play1():
            messagebox.showinfo("FIXTURES", "PLAY1 STARTED")

        def play2():
            messagebox.showinfo("FIXTURES", "PLAY2 STARTED")

        def play3():
            messagebox.showinfo("FIXTURES", "PLAY3 STARTED")

        def play4():
            messagebox.showinfo("FIXTURES", "PLAY4 STARTED")

        def play5():
            messagebox.showinfo("FIXTURES", "PLAY5 STARTED")

        def play6():
            messagebox.showinfo("FIXTURES", "PLAY6 STARTED")

        def play7():
            messagebox.showinfo("FIXTURES", "FINAL STARTED")"""

        def play22():
            cur7_1 = conn.cursor()
            ins7_1 = "select * from fixture"
            cur7_1.execute(ins7_1)
            for x in cur7_1:
                n = (list(x))
                if n[3] == None:
                    break
            cur7_1.close()

            root7 = Tk()
            root7.geometry('750x1000')

            head7 = Label(root7, text="===MATCH===").place(x=175, y=50)
            head7_1 = Label(root7, text=n[1]).place(x=75, y=100)
            head7_2 = Label(root7, text=n[2]).place(x=250, y=100)
            head7_3 = Label(root7, text="  vs").place(x=200, y=100)
            head7_4 = Label(root7, text="WINNER").place(x=75, y=700)

            def over():
                t1 = []
                t1.append(t1p1_id.get())
                t1.append(t1p2_id.get())
                t1.append(t1p3_id.get())
                t1.append(t1p4_id.get())
                t1.append(t1p5_id.get())
                t1.append(t1p6_id.get())
                t1.append(t1p7_id.get())
                t1.append(t1p8_id.get())
                t1.append(t1p9_id.get())
                t1.append(t1p10_id.get())
                t1.append(t1p11_id.get())

                t2 = []
                t2.append(t2p1_id.get())
                t2.append(t2p2_id.get())
                t2.append(t2p3_id.get())
                t2.append(t2p4_id.get())
                t2.append(t2p5_id.get())
                t2.append(t2p6_id.get())
                t2.append(t2p7_id.get())
                t2.append(t2p8_id.get())
                t2.append(t2p9_id.get())
                t2.append(t2p10_id.get())
                t2.append(t2p11_id.get())

                win_ner = winner.get()
                cur7_4 = conn.cursor()
                ins7_4 = "update team set m_played=2 where t_id in (%d,%d)" % (n[1], n[2])
                cur7_4.execute(ins7_4)
                conn.commit()
                cur7_4.close()
                cur7_6 = conn.cursor()
                ins7_6 = "update player set g_played=2 where t_id in (%d,%d) " % (n[1], n[2])
                cur7_6.execute(ins7_6)
                conn.commit()
                cur7_6.close()
                cur7_8 = conn.cursor()
                ins7_8 = "update fixture set win_id=%d where g_no=%d " % (win_ner, n[0])
                cur7_8.execute(ins7_8)
                conn.commit()
                cur7_8.close()
                cur7_9 = conn.cursor()
                ins7_9 = "update team set m_won=2 where t_id=%d " % win_ner
                cur7_9.execute(ins7_9)
                conn.commit()
                cur7_9.close()
                cur7_10 = conn.cursor()
                ins7_10 = "update player set g_won=2 where t_id=%d " % win_ner
                cur7_10.execute(ins7_10)
                conn.commit()
                cur7_10.close()
                t1p1_id.set("")
                t1p2_id.set("")
                t1p3_id.set("")
                t1p4_id.set("")
                t1p5_id.set("")
                t1p6_id.set("")
                t1p7_id.set("")
                t1p8_id.set("")
                t1p9_id.set("")
                t1p10_id.set("")
                t1p11_id.set("")
                t2p1_id.set("")
                t2p2_id.set("")
                t2p3_id.set("")
                t2p4_id.set("")
                t2p5_id.set("")
                t2p6_id.set("")
                t2p7_id.set("")
                t2p8_id.set("")
                t2p9_id.set("")
                t2p10_id.set("")
                t2p11_id.set("")
                winner.set("")

                if n[0] == 5:
                    cur7_11 = conn.cursor()
                    ins7_11 = "insert into fixture(g_no,t1_id) values(7,%d)" % win_ner
                    cur7_11.execute(ins7_11)
                    cur7_11.commit()
                    cur7_11.close()
                elif n[0] == 6:
                    cur7_12 = conn.cursor()
                    ins7_12 = "update fixture set t2_id=%d where g_no=7" % win_ner
                    cur7_12.execute(ins7_12)
                    cur7_12.commit()
                    cur7_12.close()

                messagebox.showinfo("MATCH DAY", "MATCH OVER")

            def close():
                messagebox.showinfo(" MATCH ", "THANK YOU!!!")
                root7.destroy()

            t1p1_id = IntVar(root7)
            t1p2_id = IntVar(root7)
            t1p3_id = IntVar(root7)
            t1p4_id = IntVar(root7)
            t1p5_id = IntVar(root7)
            t1p6_id = IntVar(root7)
            t1p7_id = IntVar(root7)
            t1p8_id = IntVar(root7)
            t1p9_id = IntVar(root7)
            t1p10_id = IntVar(root7)
            t1p11_id = IntVar(root7)

            t2p1_id = IntVar(root7)
            t2p2_id = IntVar(root7)
            t2p3_id = IntVar(root7)
            t2p4_id = IntVar(root7)
            t2p5_id = IntVar(root7)
            t2p6_id = IntVar(root7)
            t2p7_id = IntVar(root7)
            t2p8_id = IntVar(root7)
            t2p9_id = IntVar(root7)
            t2p10_id = IntVar(root7)
            t2p11_id = IntVar(root7)

            winner = IntVar(root7)

            entry6_1 = Entry(root7, textvariable=t1p1_id).place(x=75, y=150)
            entry6_5 = Entry(root7, textvariable=t1p2_id).place(x=75, y=200)
            entry6_2 = Entry(root7, textvariable=t1p3_id).place(x=75, y=250)
            entry6_3 = Entry(root7, textvariable=t1p4_id).place(x=75, y=300)
            entry6_4 = Entry(root7, textvariable=t1p5_id).place(x=75, y=350)
            entry6_6 = Entry(root7, textvariable=t1p6_id).place(x=75, y=400)
            entry6_7 = Entry(root7, textvariable=t1p7_id).place(x=75, y=450)
            entry6_8 = Entry(root7, textvariable=t1p8_id).place(x=75, y=500)
            entry6_9 = Entry(root7, textvariable=t1p9_id).place(x=75, y=550)
            entry6_10 = Entry(root7, textvariable=t1p10_id).place(x=75, y=600)
            entry6_11 = Entry(root7, textvariable=t1p11_id).place(x=75, y=650)

            entry6_12 = Entry(root7, textvariable=t2p1_id).place(x=250, y=150)
            entry6_13 = Entry(root7, textvariable=t2p2_id).place(x=250, y=200)
            entry6_14 = Entry(root7, textvariable=t2p3_id).place(x=250, y=250)
            entry6_15 = Entry(root7, textvariable=t2p4_id).place(x=250, y=300)
            entry6_16 = Entry(root7, textvariable=t2p5_id).place(x=250, y=350)
            entry6_17 = Entry(root7, textvariable=t2p6_id).place(x=250, y=400)
            entry6_18 = Entry(root7, textvariable=t2p7_id).place(x=250, y=450)
            entry6_19 = Entry(root7, textvariable=t2p8_id).place(x=250, y=500)
            entry6_20 = Entry(root7, textvariable=t2p9_id).place(x=250, y=550)
            entry6_21 = Entry(root7, textvariable=t2p10_id).place(x=250, y=600)
            entry6_22 = Entry(root7, textvariable=t2p11_id).place(x=250, y=650)

            entry6_24 = Entry(root7, textvariable=winner).place(x=150, y=700)

            b6_1 = Button(root7, text="  ||OVER|| ", borderwidth=4, command=over)
            b6_1.place(x=175, y=750)

            root7.mainloop()

        def play33():
            cur8_1 = conn.cursor()
            ins8_1 = "select * from fixture"
            cur8_1.execute(ins8_1)
            for x in cur8_1:
                n = (list(x))
                if n[3] == None:
                    break
            cur8_1.close()

            root7 = Tk()
            root7.geometry('750x1000')

            head7 = Label(root8, text="===MATCH===").place(x=175, y=50)
            head7_1 = Label(root8, text=n[1]).place(x=75, y=100)
            head7_2 = Label(root8, text=n[2]).place(x=250, y=100)
            head7_3 = Label(root8, text="  vs").place(x=200, y=100)
            head7_4 = Label(root8, text="WINNER").place(x=75, y=700)

            def over():
                t1 = []
                t1.append(t1p1_id.get())
                t1.append(t1p2_id.get())
                t1.append(t1p3_id.get())
                t1.append(t1p4_id.get())
                t1.append(t1p5_id.get())
                t1.append(t1p6_id.get())
                t1.append(t1p7_id.get())
                t1.append(t1p8_id.get())
                t1.append(t1p9_id.get())
                t1.append(t1p10_id.get())
                t1.append(t1p11_id.get())

                t2 = []
                t2.append(t2p1_id.get())
                t2.append(t2p2_id.get())
                t2.append(t2p3_id.get())
                t2.append(t2p4_id.get())
                t2.append(t2p5_id.get())
                t2.append(t2p6_id.get())
                t2.append(t2p7_id.get())
                t2.append(t2p8_id.get())
                t2.append(t2p9_id.get())
                t2.append(t2p10_id.get())
                t2.append(t2p11_id.get())

                win_ner = winner.get()
                cur8_4 = conn.cursor()
                ins8_4 = "update team set m_played=3 where t_id in (%d,%d)" % (n[1], n[2])
                cur8_4.execute(ins8_4)
                conn.commit()
                cur8_4.close()
                cur8_6 = conn.cursor()
                ins8_6 = "update player set g_played=3 where t_id in (%d,%d) " % (n[1], n[2])
                cur8_6.execute(ins8_6)
                conn.commit()
                cur8_6.close()
                cur8_8 = conn.cursor()
                ins8_8 = "update fixture set win_id=%d where g_no=%d " % (win_ner, n[0])
                cur8_8.execute(ins8_8)
                conn.commit()
                cur8_8.close()
                cur8_9 = conn.cursor()
                ins8_9 = "update team set m_won=3 where t_id=%d " % win_ner
                cur8_9.execute(ins8_9)
                conn.commit()
                cur8_9.close()
                cur8_10 = conn.cursor()
                ins8_10 = "update player set g_won=3 where t_id=%d " % win_ner
                cur8_10.execute(ins8_10)
                conn.commit()
                cur8_10.close()
                t1p1_id.set("")
                t1p2_id.set("")
                t1p3_id.set("")
                t1p4_id.set("")
                t1p5_id.set("")
                t1p6_id.set("")
                t1p7_id.set("")
                t1p8_id.set("")
                t1p9_id.set("")
                t1p10_id.set("")
                t1p11_id.set("")
                t2p1_id.set("")
                t2p2_id.set("")
                t2p3_id.set("")
                t2p4_id.set("")
                t2p5_id.set("")
                t2p6_id.set("")
                t2p7_id.set("")
                t2p8_id.set("")
                t2p9_id.set("")
                t2p10_id.set("")
                t2p11_id.set("")
                winner.set("")

                cur8_20 = conn.cursor()
                ins8_20 = "select t_name from team where t_id=%d" % win_ner
                cur8_20.execute(ins8_20)
                for i in cur8_20:
                    n = list(i)

                messagebox.showinfo("FINALS!", "MATCH OVER" + n[0] + "WON THE LEAGUE")

            def close():
                messagebox.showinfo(" FINAL ", "THANK YOU FOR THE LEAGUE")
                root8.destroy()

            t1p1_id = IntVar(root8)
            t1p2_id = IntVar(root8)
            t1p3_id = IntVar(root8)
            t1p4_id = IntVar(root8)
            t1p5_id = IntVar(root8)
            t1p6_id = IntVar(root8)
            t1p7_id = IntVar(root8)
            t1p8_id = IntVar(root8)
            t1p9_id = IntVar(root8)
            t1p10_id = IntVar(root8)
            t1p11_id = IntVar(root8)

            t2p1_id = IntVar(root8)
            t2p2_id = IntVar(root8)
            t2p3_id = IntVar(root8)
            t2p4_id = IntVar(root8)
            t2p5_id = IntVar(root8)
            t2p6_id = IntVar(root8)
            t2p7_id = IntVar(root8)
            t2p8_id = IntVar(root8)
            t2p9_id = IntVar(root8)
            t2p10_id = IntVar(root8)
            t2p11_id = IntVar(root8)

            winner = IntVar(root8)

            entry6_1 = Entry(root8, textvariable=t1p1_id).place(x=75, y=150)
            entry6_5 = Entry(root8, textvariable=t1p2_id).place(x=75, y=200)
            entry6_2 = Entry(root8, textvariable=t1p3_id).place(x=75, y=250)
            entry6_3 = Entry(root8, textvariable=t1p4_id).place(x=75, y=300)
            entry6_4 = Entry(root8, textvariable=t1p5_id).place(x=75, y=350)
            entry6_6 = Entry(root8, textvariable=t1p6_id).place(x=75, y=400)
            entry6_7 = Entry(root8, textvariable=t1p7_id).place(x=75, y=450)
            entry6_8 = Entry(root8, textvariable=t1p8_id).place(x=75, y=500)
            entry6_9 = Entry(root8, textvariable=t1p9_id).place(x=75, y=550)
            entry6_10 = Entry(root8, textvariable=t1p10_id).place(x=75, y=600)
            entry6_11 = Entry(root8, textvariable=t1p11_id).place(x=75, y=650)

            entry6_12 = Entry(root8, textvariable=t2p1_id).place(x=250, y=150)
            entry6_13 = Entry(root8, textvariable=t2p2_id).place(x=250, y=200)
            entry6_14 = Entry(root8, textvariable=t2p3_id).place(x=250, y=250)
            entry6_15 = Entry(root8, textvariable=t2p4_id).place(x=250, y=300)
            entry6_16 = Entry(root8, textvariable=t2p5_id).place(x=250, y=350)
            entry6_17 = Entry(root8, textvariable=t2p6_id).place(x=250, y=400)
            entry6_18 = Entry(root8, textvariable=t2p7_id).place(x=250, y=450)
            entry6_19 = Entry(root8, textvariable=t2p8_id).place(x=250, y=500)
            entry6_20 = Entry(root8, textvariable=t2p9_id).place(x=250, y=550)
            entry6_21 = Entry(root8, textvariable=t2p10_id).place(x=250, y=600)
            entry6_22 = Entry(root8, textvariable=t2p11_id).place(x=250, y=650)

            entry6_24 = Entry(root8, textvariable=winner).place(x=150, y=700)

            b6_1 = Button(root8, text="  ||OVER|| ", borderwidth=4, command=over)
            b6_1.place(x=175, y=750)

            root8.mainloop()

        def close():
            messagebox.showinfo("FIXTURES", "THANK YOU!!!")
            root5.destroy()

        b5_1 = Button(root5, text="  PLAY1  ", borderwidth=4, command=play)
        b5_1.place(x=400, y=200)
        b5_2 = Button(root5, text="  PLAY2  ", borderwidth=4, command=play)
        b5_2.place(x=400, y=250)
        b5_3 = Button(root5, text="  PLAY3  ", borderwidth=4, command=play)
        b5_3.place(x=400, y=300)
        b5_4 = Button(root5, text="  PLAY4  ", borderwidth=4, command=play)
        b5_4.place(x=400, y=350)
        b5_5 = Button(root5, text="  PLAY5  ", borderwidth=4, command=play22)
        b5_5.place(x=400, y=450)
        b5_6 = Button(root5, text="  PLAY6  ", borderwidth=4, command=play22)
        b5_6.place(x=400, y=500)
        b5_7 = Button(root5, text="  PLAY7  ", borderwidth=4, command=play33)
        b5_7.place(x=400, y=600)

        b5_8 = Button(root5, text="  EXIT  ", borderwidth=4, command=close)
        b5_8.place(x=175, y=650)

        root5.mainloop()


head1 = Label(root1, text="===FOOTBALL LEAGUE===").place(x=125, y=50)

b1_1 = Button(root1, text="Team Registration", borderwidth=4, command=register)
b1_1.place(x=25, y=120)

b1_2 = Button(root1, text="Team Login", borderwidth=4, command=login)
b1_2.place(x=175, y=120)

b1_3 = Button(root1, text="Fixtures", borderwidth=4, command=fixtures)
b1_3.place(x=300, y=120)

root1.mainloop()