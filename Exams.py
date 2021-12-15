from tkinter import*
from tkinter import messagebox
from PIL import  ImageTk,Image
import  pyodbc

# BLUEPRINT OBJECT

class JUSTLOGIN:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.config(bg='#fff')
        self.root.title('MyJust Login')
        self.root.iconbitmap(r'C:\Users\PC\PycharmProjects\RoomProjects\GUIs Projects\PROJECT\JUSTEXAM_CENTER\images\JAM.ico')

        # img
        self.img_bg=Image.open('images/bg.PNG')
        self.img=ImageTk.PhotoImage(self.img_bg)
        Label(self.root,image=self.img,bg='white',bd=0).place(x=1,y=1)

        # left icon
        self.img_icon = Image.open('images/JUST.png')
        self.resize=self.img_icon.resize((120,120),Image.ANTIALIAS)
        self.new=ImageTk.PhotoImage(self.resize)
        Label(self.root,image=self.new,bg='white',bd=0).place(x=1020,y=120)
        Label(self.root, text="JAMHUURIYA UNIVERSITY", bg='white',
              fg='#019',font=('Verdana',19,'bold'),bd=0).place(x=1140, y=150)
        Label(self.root, text="OF SCIENCE AND TECHNOLOGY (JUST)", bg='white',
              fg='#017', font=('Verdana', 12, 'bold'), bd=0).place(x=1160, y=190)

        Label(self.root, text="MyJust Login", bg='white',
              fg='green', font=('Verdana', 22, 'bold'), bd=0).place(x=1150, y=310)


        self.text_box = Image.open('images/text.png')

        self.res=self.text_box.resize((350,110),Image.ANTIALIAS)
        self.img_=ImageTk.PhotoImage(self.res)
        Label(self.root,image=self.img_,bg='white',bd=0).place(x=1120,y=400)
        Label(self.root,text='Username',bg='white',fg='#014',
        font=('Verdana',13,'bold'),bd=0).place(x=1150,y=380)
        self.userID = Entry(self.root, bg='white', fg='#011', font=('Verdana', 14, 'bold'),
                            bd=0,justify=CENTER, relief='flat')
        self.userID.place(x=1150, y=435, height=30)

        # 2
        self.text_box2 = Image.open('images/text.png')
        self.res2 = self.text_box2.resize((350, 110), Image.ANTIALIAS)
        self.img_2 = ImageTk.PhotoImage(self.res2)
        Label(self.root, image=self.img_2, bg='white', bd=0).place(x=1120, y=530)
        Label(self.root, text='Password', bg='white', fg='#014',
              font=('Verdana', 13, 'bold'), bd=0).place(x=1150, y=510)

        self.userPas = Entry(self.root, bg='white', fg='#011', font=('Verdana', 14, 'bold'),
                            bd=0, justify=CENTER, relief='flat',show='*')
        self.userPas.place(x=1150, y=565, height=30)

        # sign in
        self.signin = Image.open('images/login.png')
        self.res3 = self.signin.resize((320, 95), Image.ANTIALIAS)
        self.img_3 = ImageTk.PhotoImage(self.res3)
        self.SignIn=Button(self.root, command=self.signIn,image=self.img_3,cursor='hand2', bg='white', bd=0,activebackground='white')
        self.SignIn.place(x=1140, y=630)

        self.Register = Button(self.root, text='Register?', cursor='hand2', bg='white',fg='red',
                               font=('Serif',13,'bold'),bd=0,
                             activebackground='white',command=self.register)
        self.Register.place(x=1340, y=610)

        self.fb = Image.open('images/fb.png')
        self.res4 = self.fb.resize((30, 30), Image.ANTIALIAS)
        self.img_4 = ImageTk.PhotoImage(self.res4)
        self.fb_ = Button(self.root, image=self.img_4, cursor='hand2', bg='white', bd=0, activebackground='white')
        self.fb_.place(x=1260, y=730)

        self.insta = Image.open('images/insta.png')
        self.res5= self.insta.resize((30, 30), Image.ANTIALIAS)
        self.img_5 = ImageTk.PhotoImage(self.res5)
        self.inst_ = Button(self.root, image=self.img_5, cursor='hand2', bg='white', bd=0, activebackground='white')
        self.inst_.place(x=1310, y=730)

        Label(self.root, text='AllRight Reserved @2021', bg='white', fg='#014',
              font=('Verdana', 8), bd=0).place(x=1240, y=780)


    # functions
    def signIn(self):
        if self.userID.get()=='' or self.userPas.get()=='':
            messagebox.showerror('Error','Input Required')
        else:
            try:
                db=pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=ExamCenter;"
                    "Trusted_Connection=yes;"
                )
                cursor=db.cursor()
                cursor.execute('SELECT *FROM students where sid=? and password=?',
                               (self.userID.get(),self.userPas.get()))
                row=cursor.fetchone()
                if row==None:
                    messagebox.showerror('ERR','This ID is Not exist')
                    self.userID.delete(0,END)
                    self.userPas.delete(0,END)
                else:
                    messagebox.showinfo('ADMIN',f'Successful Login With {row[1]}')
                    self.userID.delete(0, END)
                    self.userPas.delete(0, END)
            except Exception as err:
                messagebox.showerror('ERR',f'Error Occurred Due To \n{err}')

    def register(self):
        self.window=Toplevel()
        # self.window.geometry("600x300")
        self.window.title('Register New Student')
        self.window.focus()
        self.window.state('zoomed')
        self.window.resizable(0,0)
        self.window.config(bg='#fff')

        #frame
        self.student=LabelFrame(self.window,text='Student Registration',
        font=('Verdana',17,'bold'),fg='#445',width=740,height=600,bd=4,relief='groove'
                                ,bg='#f4f4f4')
        self.student.place(x=40,y=100)

        Label(self.student,text='StudentID',bg='#f4f4f4',fg='#019',
              font=('Verdana',16,'bold')).place(x=30,y=50)
        self.stdID=Entry(self.student,fg='#019',bg='#f4f4f4',font=('Verdana',15,'bold'),
                         bd=6,relief='groove')
        self.stdID.place(x=30,y=100,width=170)
        #2
        Label(self.student, text='Student-Name', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=340, y=50)
        self.stdname = Entry(self.student, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                           bd=6, relief='groove')
        self.stdname.place(x=340, y=100, width=320)

        #3
        Label(self.student, text='Gender', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=30, y=180)
        self.text=StringVar()
        self.male=Radiobutton(self.student,text='Male',bg='#f4f4f4',fg='#010',
                              font=('Verdana',16,'bold'),value='Male',variable=self.text)
        self.male.place(x=140,y=180)

        self.Female = Radiobutton(self.student, text='Female',variable=self.text, bg='#f4f4f4', fg='#010',
                                font=('Verdana', 16, 'bold'), value='Female')
        self.Female.place(x=250, y=180)

        #4
        Label(self.student, text='Class', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=30, y=250)
        self.Class = Entry(self.student, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                             bd=6, relief='groove')
        self.Class.place(x=30, y=300, width=190)

        Label(self.student, text='Password', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=380, y=250)
        self.pascode = Entry(self.student, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                           bd=6, relief='groove',show='*')
        self.pascode.place(x=380, y=300, width=190)


        # save
        self.Submit=Button(self.student,text='Submit',bg='#018',fg='#fff',
                           font=('Sans Serif',19,'bold'),width=20,bd=4,relief='sunken',
                           command=self.submit)
        self.Submit.place(x=140,y=390)


        # marks frame
        self.marks = LabelFrame(self.window, text='Student Marks',
                                  font=('Verdana', 17, 'bold'), fg='#445', width=740, height=600, bd=4, relief='groove'
                                  , bg='#f4f4f4')
        self.marks.place(x=790, y=100)

        Label(self.marks, text='StudentID', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=30, y=50)
        self.fk_student = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                           bd=6, relief='groove')
        self.fk_student.place(x=30, y=100, width=170)
        # 2
        #vars
        self.db_var=IntVar()
        self.js_var=IntVar()
        self.nw_var=IntVar()
        self.en_var=IntVar()
        self.desc_var=IntVar()
        self.acc_var=IntVar()
        self.toatl_var=IntVar()
        self.av_var=IntVar()
        self.grade_var=StringVar()
        Label(self.marks, text='Database', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=340, y=50)
        self.database = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                             bd=6, relief='groove',textvariable=self.db_var)
        self.database.place(x=340, y=100, width=180)
        # 4
        Label(self.marks, text='JavaScript', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=30, y=160)
        self.js = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                           bd=6, relief='groove',textvariable=self.js_var)
        self.js.place(x=30, y=210, width=190)

        Label(self.marks, text='Networking', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=340, y=160)
        self.net = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                             bd=6, relief='groove',textvariable=self.nw_var)
        self.net.place(x=340, y=210, width=190)

        #6

        Label(self.marks, text='English', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=30, y=280)
        self.eng = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                           bd=6, relief='groove',textvariable=self.en_var)
        self.eng.place(x=30, y=330, width=190)
        #
        Label(self.marks, text='Discrete', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=340, y=280)
        self.des = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                         bd=6, relief='groove',textvariable=self.desc_var)
        self.des.place(x=340, y=330, width=190)

        #
        Label(self.marks, text='Account', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=30, y=390)
        self.acc = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                         bd=6, relief='groove',textvariable=self.acc_var)
        self.acc.place(x=30, y=435, width=190)

        Label(self.marks, text='Total', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=330, y=390)
        self.ttl = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                         bd=6, relief='groove',textvariable=self.toatl_var)
        self.ttl.config(state=NORMAL)
        self.ttl.place(x=330, y=435, width=110)

        Label(self.marks, text='Average', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=450, y=390)
        self.av = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                         bd=6, relief='groove',textvariable=self.av_var)
        self.av.config(state=NORMAL)
        self.av.place(x=450, y=435, width=110)

        Label(self.marks, text='Grade', bg='#f4f4f4', fg='#019',
              font=('Verdana', 16, 'bold')).place(x=580, y=390)
        self.grade = Entry(self.marks, fg='#019', bg='#f4f4f4', font=('Verdana', 15, 'bold'),
                        bd=6, relief='groove',textvariable=self.grade_var)
        self.grade.config(state=NORMAL)
        self.grade.place(x=580, y=435, width=110)

        # save
        self.sve = Button(self.marks, text='Submit', bg='#000', fg='#fff',command=self.save,
                             font=('Sans Serif', 15, 'bold'), width=10, bd=4, relief='sunken',
                             )
        self.sve.config(state=DISABLED)
        self.sve.place(x=130, y=490)

        self.cal = Button(self.marks, text='Calculate', bg='#000', fg='#fff', command=self.calc,
                          font=('Sans Serif', 15, 'bold'), width=10, bd=4, relief='sunken',
                          )
        self.cal.place(x=350, y=490)



    def submit(self):
        if self.stdID.get()=='' or self.stdname.get()=='' or self.Class.get()=='' or self.pascode.get()=='':
            messagebox.showerror('ERROR','Required Student info',parent=self.student)
        else:
            try:
                conn=pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=ExamCenter;"
                    "Trusted_Connection=yes;"
                )
                cursor=conn.cursor()
                try:
                    cursor.execute("INSERT into students values(?,?,?,?,?)",
                                   (self.stdID.get(),self.stdname.get(),self.text.get(),self.Class.get(),self.pascode.get()))
                    conn.commit()
                    messagebox.showinfo('JUST',f'Successful Added With {self.stdname.get()}',parent=self.student)
                    self.clear_box()
                except Exception as err:
                    messagebox.showerror('ERR',f'this '
                                               f'{err}ID Already Exist',parent=self.student)
                    self.clear_box()




            except Exception as err:
                messagebox.showerror('ER',f'error Due To {err}',parent=self.student)

    def calc(self):
        self.ttl.delete(0,END)
        self.grade.delete(0,END)
        self.av.delete(0,END)
        self.total_marks = int(self.database.get()) + int(self.js.get()) + int(self.net.get()) + int(self.eng.get()) + int(self.des.get()) + int(self.acc.get())
        self.average=self.total_marks//6
        self.ttl.insert(0, self.total_marks)
        self.av.insert(0,self.average)
        if self.average>=90 and self.average<=100:
            self.grade.insert(0,'A')
        elif self.average>=80 and self.average<=89:
            self.grade.insert(0,'B')

        elif self.average >= 70 and self.average <= 79:
            self.grade.insert(0, 'C')
        elif self.average >= 60 and self.average <= 69:
            self.grade.insert(0, 'D')
        elif self.average >= 50 and self.average <= 59:
            self.grade.insert(0, 'E')
        else:
            self.grade.insert(0,'Fail')
        self.sve.config(state=NORMAL)



    def save(self):
        if self.fk_student.get() == '' or self.database.get() == 0 or self.js.get() == 0 or self.net.get() == 0 or self.eng.get() == 0 or self.des.get() == 0 or self.acc.get() == 0:
            messagebox.showerror('ER', 'All Fields Are required', parent=self.marks)
        else:
            try:
                conn =pyodbc.connect(
                            "Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                            "Database=ExamCenter;"
                            "Trusted_Connection=yes;"
                        )
                cursor = conn.cursor()
                cursor.execute('INSERT INTO marks values(?,?,?,?,?,?,?,?,?,?)',
                               (self.fk_student.get(),self.database.get(),self.js.get(),self.net.get(),self.eng.get(),self.des.get(),self.acc.get(),self.ttl.get(),self.av.get(),self.grade.get()))
                conn.commit()
                messagebox.showinfo('ADMIN',f'You Assigned Marks With StudentID {self.fk_student.get()}',
                                    parent=self.marks)
                self.clear_marks()
            except pyodbc.IntegrityError:
                messagebox.showerror('ERR','This ID is not exist\nIn The Database',parent=self.marks)




    def clear_box(self):
        self.stdID.delete(0, END)
        self.stdname.delete(0, END)
        self.text.set('')
        self.Class.delete(0, END)
        self.pascode.delete(0, END)

    def clear_marks(self):
        self.fk_student.delete(0,END)
        self.database.delete(0,END)
        self.js.delete(0,END)
        self.net.delete(0,END)
        self.eng.delete(0,END)
        self.des.delete(0,END)
        self.acc.delete(0,END)
        self.ttl.delete(0,END)
        self.av.delete(0,END)
        self.grade.delete(0,END)
if __name__=='__main__':
    root=Tk()

    apk=JUSTLOGIN(root)
    root.mainloop()
