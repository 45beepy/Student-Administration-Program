#Frontend

from tkinter import*
import tkinter.messagebox
import backend

class Student:

    def __init__(self, root):
        self.root =root
        self.root.title("Teacher Assistant Program")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#5EE6E2")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dateofbirth = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
        PM1 = StringVar()
        Mid1 = StringVar()
        POM1 = StringVar()

        #Functons
        def iExit():
            iExit = tkinter.messagebox.askyesno("Teacher Assistant Program", "Do you want to Exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtfname.delete(0, END)
            self.txtlname.delete(0, END)
            self.txtdob.delete(0, END)
            self.txtsex.delete(0, END)
            self.txtno.delete(0, END)
            self.txtut1.delete(0, END)
            self.txtmid1.delete(0, END)
            self.txtpo1.delete(0, END)

        def addData():
            if(len(StdID.get() )!=0):
                backend.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dateofbirth.get(), Gender.get(), Mobile.get(), PM1.get(), Mid1.get(), POM1.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dateofbirth.get(), Gender.get(), Mobile.get(), PM1.get(), Mid1.get(), POM1.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in backend.viewData():
             studentlist.insert(END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd=studentlist.curselection()[0]
            sd=studentlist.get(searchStd )

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtfname.delete(0, END)
            self.txtfname.insert(END, sd[2])
            self.txtlname.delete(0, END)
            self.txtlname.insert(END, sd[3])
            self.txtdob.delete(0, END)
            self.txtdob.insert(END, sd[4])
            self.txtsex.delete(0, END)
            self.txtsex.insert(END, sd[5])
            self.txtno.delete(0, END)
            self.txtno.insert(END, sd[6])
            self.txtut1.delete(0, END)
            self.txtut1.insert(END, sd[7])
            self.txtmid1.delete(0, END)
            self.txtmid1.insert(END, sd[8])
            self.txtpo1.delete(0, END)
            self.txtpo1.insert(END, sd[9])

        def DeleteData():
            if(len(StdID.get()) !=0):
                backend.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in backend.searchData(StdID.get(), Firstname.get(), Lastname.get(), Dateofbirth.get(), Gender.get(), Mobile.get(), PM1.get(), Mid1.get(), POM1.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if(len(StdID.get()) !=0):
                backend.deleteRec(sd[0])
            if(len(StdID.get()) !=0):
                backend.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dateofbirth.get(), Gender.get(), Mobile.get(), PM1.get(), Mid1.get(), POM1.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dateofbirth.get(), Gender.get(), Mobile.get(), PM1.get(), Mid1.get(), POM1.get()) )

        #Frames
        MainFrame = Frame(self.root, bg="#5EE6E2")
        MainFrame.grid()

        TitFrame = Frame(MainFrame,  bd=2, padx=54,pady=8, bg="#FFFFFF", relief=RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame ,font=('arial', 47,'bold'),text="Teacher Assistant Program",bg="#FFFFFF")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=1350, height=70, bd=2, padx=18,pady=10, bg="#FFFFFF", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,  bd=2, width=1300, height=400, padx=20,pady=20, bg="#5EE6E2", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame,  bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="#FFFFFF", font=('arial', 20,'bold'), text="Student Info\n" )
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame,  bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="#FFFFFF", font=('arial', 20,'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #Labels and Entry Widgents
        self.lblStdID = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Student ID:", padx=2, pady=2, bg="#FFFFFF")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfname = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Firstname:", padx=2, pady=2, bg="#FFFFFF")
        self.lblfname.grid(row=1, column=0, sticky=W)
        self.txtfname = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=Firstname, width=39)
        self.txtfname.grid(row=1, column=1)

        self.lbllname = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Lastname:", padx=2, pady=2, bg="#FFFFFF")
        self.lbllname.grid(row=2, column=0, sticky=W)
        self.txtlname = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=Lastname, width=39)
        self.txtlname.grid(row=2, column=1)

        self.lbldob = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Date of Birth:", padx=2, pady=2, bg="#FFFFFF")
        self.lbldob.grid(row=3, column=0, sticky=W)
        self.txtdob = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=Dateofbirth, width=39)
        self.txtdob.grid(row=3, column=1)

        self.lblsex = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Gender:", padx=2, pady=2, bg="#FFFFFF")
        self.lblsex.grid(row=4, column=0, sticky=W)
        self.txtsex = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=Gender, width=39)
        self.txtsex.grid(row=4, column=1)

        self.lblno = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Contact No:", padx=2, pady=2, bg="#FFFFFF")
        self.lblno.grid(row=5, column=0, sticky=W)
        self.txtno = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=Mobile, width=39)
        self.txtno.grid(row=5, column=1)

        self.lblut1 = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Premid Term:", padx=2, pady=2, bg="#FFFFFF")
        self.lblut1.grid(row=6, column=0, sticky=W)
        self.txtut1 = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=PM1, width=39)
        self.txtut1.grid(row=6, column=1)

        self.lblmid1 = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="Mid Term:", padx=2, pady=2, bg="#FFFFFF")
        self.lblmid1.grid(row=7, column=0, sticky=W)
        self.txtmid1 = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=Mid1, width=39)
        self.txtmid1.grid(row=7, column=1)

        self.lblpo1 = Label(DataFrameLEFT , font=('arial', 20,'bold'),text="PostMid Term:", padx=2, pady=2, bg="#FFFFFF")
        self.lblpo1.grid(row=8, column=0, sticky=W)
        self.txtpo1 = Entry(DataFrameLEFT , font=('arial', 20,'bold'),textvariable=POM1, width=39)
        self.txtpo1.grid(row=8, column=1)

        #Listbox & scroll bar
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)

        #Button Widgets
        self.btnAddData = Button(ButtonFrame, text="Add New",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit",font=('arial', 20,'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)












  











        
    
if __name__=="__main__":
    root = Tk()
    application = Student(root)
    root.mainloop()
