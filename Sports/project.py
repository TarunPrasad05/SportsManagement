import pyodbc
import tkinter as tk
import tkinter.font as tkFont


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-SMC51SMG;'
                      'Database=league;'
                      'Trusted_Connection=yes;')
cursor=conn.cursor()


class App:
    def __init__(self, root):
        #setting title
        root.title("MINI PROJECT")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_836=tk.Button(root)
        GButton_836["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_836["font"] = ft
        GButton_836["fg"] = "#000000"
        GButton_836["justify"] = "center"
        GButton_836["text"] = "Team Registration"
        GButton_836.place(x=90,y=190,width=103,height=70)
        GButton_836["command"] = self.GButton_836_command

        GLabel_221=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_221["font"] = ft
        GLabel_221["fg"] = "#333333"
        GLabel_221["justify"] = "center"
        GLabel_221["text"] = "===FOOTBALL LEAGUE==="
        GLabel_221.place(x=180,y=80,width=230,height=50)

        GButton_328=tk.Button(root)
        GButton_328["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_328["font"] = ft
        GButton_328["fg"] = "#000000"
        GButton_328["justify"] = "center"
        GButton_328["text"] = "Team Login"
        GButton_328.place(x=250,y=190,width=97,height=72)
        GButton_328["command"] = self.GButton_328_command

        GButton_964=tk.Button(root)
        GButton_964["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_964["font"] = ft
        GButton_964["fg"] = "#000000"
        GButton_964["justify"] = "center"
        GButton_964["text"] = "Fixtures"
        GButton_964.place(x=410,y=190,width=102,height=74)
        GButton_964["command"] = self.GButton_964_command

    def GButton_836_command(self):
        class App2:
            def __init__(self, root1):
                # setting title
                root.title("undefined")
                # setting window size
                width = 501
                height = 375
                screenwidth = root.winfo_screenwidth()
                screenheight = root.winfo_screenheight()
                alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                root.geometry(alignstr)
                root.resizable(width=False, height=False)

                GLabel_816 = tk.Label(root)
                ft = tkFont.Font(family='Times', size=10)
                GLabel_816["font"] = ft
                GLabel_816["fg"] = "#333333"
                GLabel_816["justify"] = "center"
                GLabel_816["text"] = "REGISTRATION"
                GLabel_816.place(x=150, y=40, width=176, height=50)

                GLabel_33 = tk.Label(root)
                ft = tkFont.Font(family='Times', size=10)
                GLabel_33["font"] = ft
                GLabel_33["fg"] = "#333333"
                GLabel_33["justify"] = "center"
                GLabel_33["text"] = "Team ID"
                GLabel_33.place(x=100, y=100, width=107, height=53)

                GLabel_260 = tk.Label(root)
                ft = tkFont.Font(family='Times', size=10)
                GLabel_260["font"] = ft
                GLabel_260["fg"] = "#333333"
                GLabel_260["justify"] = "center"
                GLabel_260["text"] = "Password"
                GLabel_260.place(x=110, y=150, width=86, height=61)

                GLabel_750 = tk.Label(root)
                ft = tkFont.Font(family='Times', size=10)
                GLabel_750["font"] = ft
                GLabel_750["fg"] = "#333333"
                GLabel_750["justify"] = "center"
                GLabel_750["text"] = "Team Name"
                GLabel_750.place(x=100, y=220, width=120, height=38)

                GLineEdit_520 = tk.Entry(root)
                GLineEdit_520["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times', size=10)
                GLineEdit_520["font"] = ft
                GLineEdit_520["fg"] = "#333333"
                GLineEdit_520["justify"] = "center"
                GLineEdit_520["text"] = "t_id"
                GLineEdit_520.place(x=230, y=120, width=103, height=30)

                GLineEdit_110 = tk.Entry(root)
                GLineEdit_110["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times', size=10)
                GLineEdit_110["font"] = ft
                GLineEdit_110["fg"] = "#333333"
                GLineEdit_110["justify"] = "center"
                GLineEdit_110["text"] = "password"
                GLineEdit_110.place(x=230, y=170, width=104, height=30)

                GLineEdit_732 = tk.Entry(root)
                GLineEdit_732["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times', size=10)
                GLineEdit_732["font"] = ft
                GLineEdit_732["fg"] = "#333333"
                GLineEdit_732["justify"] = "center"
                GLineEdit_732["text"] = "name"
                GLineEdit_732.place(x=230, y=220, width=99, height=30)

                GButton_82 = tk.Button(root)
                GButton_82["bg"] = "#efefef"
                ft = tkFont.Font(family='Times', size=10)
                GButton_82["font"] = ft
                GButton_82["fg"] = "#000000"
                GButton_82["justify"] = "center"
                GButton_82["text"] = "REGISTER"
                GButton_82.place(x=190, y=280, width=117, height=41)
                GButton_82["command"] = self.GButton_82_command

            def GButton_82_command(self):
                a = GLineEdit_520.get()
                print(a)




        if __name__ == "__main__":
            root1 = tk.Tk()
            app2 = App2(root1)
            root1.mainloop()

    def GButton_328_command(self):
        print("command")


    def GButton_964_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

