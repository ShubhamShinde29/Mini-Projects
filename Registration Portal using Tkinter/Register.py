from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import os
import sys
import mysql.connector
import pymysql


class Register():
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Portal")
        self.root.geometry("%dx%d" % (sw, sh))
        self.root.wm_iconbitmap("appicon.ico")

        # === Bg Image ====#
        self.bg = ImageTk.PhotoImage(file="img/bgf.jpg")
        bgimage = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)
        
        namelabel=Label(self.root,text="Presented by Shubham Shinde",font=("times new roman",15,"italic","bold"),bg="cyan",fg="black").place(x=1250,y=790)

        # === Register Frame ===#
        frame1 = Frame(self.root, bg="orange",highlightbackground="black",highlightthickness=3)
        frame1.place(x=350, y=100, width=800, height=550)

        # === Frame component ===#
        title = Label(frame1, text="REGISTER HERE !!", font=(
            "times new roman", 30, "italic", "bold"), bg="orange", fg="black").place(x=50, y=30)

        # === 1st row ==#
        fname = Label(frame1, text="First Name ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=50, y=100)
        self.fname_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.fname_txt.place(x=50, y=130, width=250)

        lname = Label(frame1, text="Last Name ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=400, y=100)
        self.lname_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.lname_txt.place(x=400, y=130, width=250)

        # === 2nd Row ===#
        Mob = Label(frame1, text="Contact No ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=50, y=170)
        self.mob_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.mob_txt.place(x=50, y=200, width=250)

        mail = Label(frame1, text="Email ID ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=400, y=170)
        self.mail_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.mail_txt.place(x=400, y=200, width=250)

        # === 3rd Row ===#
        username = Label(frame1, text="Username ", font=("Comic Sans MS",
                    13, "bold"), bg="orange", fg="black").place(x=50, y=250)
        self.username_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.username_txt.place(x=50, y=280, width=250)

        password = Label(frame1, text="Password ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=400, y=250)
        self.password_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.password_txt.place(x=400, y=280, width=250)

        # === 4th Row ===#
        S_que = Label(frame1, text="Security Question ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=50, y=330)
        self.S_que_cmb = ttk.Combobox(frame1, font=(
            "Comic Sans MS", 13), state="readonly", justify=CENTER)
        self.S_que_cmb['value'] = ('Select', 'Your Birth Date',
                            'Your first School', 'Your pet name')
        self.S_que_cmb.place(x=50, y=360, width=250)
        self.S_que_cmb.current(0)

        ans = Label(frame1, text="Answer ", font=(
            "Comic Sans MS", 13, "bold"), bg="orange", fg="black").place(x=400, y=330)
        self.ans_txt = Entry(frame1, font=("Comic Sans MS", 13, "italic"),
                        bg="white", fg="black")
        self.ans_txt.place(x=400, y=360, width=250)

        # === Terms & conditions
        self.chbtn=IntVar()
        ch = Checkbutton(frame1, text="Agree to Terms & conditions",
                        bg="orange",variable=self.chbtn, onvalue=1, offvalue=0).place(x=50, y=420)

        # == Submit button ===#
        submit_btn = Button(frame1, text="Register Now",bg="black",fg="white",font=("Comic Sans MS",13,"italic"), bd=1, cursor="hand2",command=self.insert_data).place(
            x=360, y=470, width=150, height=40)

        # === Login In ===#
        sign_btn = Button(frame1, text="Login",bg="black",fg="white",font=("Comic Sans MS",13,"italic"), cursor="hand2",command=callLogin).place(
            x=180, y=470, width=150, height=40)

    def insert_data(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.mob_txt.get()=="" or self.mail_txt.get()=="" or self.username_txt.get()=="" or self.password_txt.get()=="" or self.S_que_cmb.get()=="" or self.ans_txt.get()=="":
            messagebox.showerror("Error","All fields are required ......",parent=self.root)
        elif self.chbtn.get()==0:
            messagebox.showerror("Error","Please agree terms and conditions",parent=self.root)
        else:
            con=pymysql.connect(host='localhost',user='root',password='shubham@29',database='activity')
            cur=con.cursor()
            try:
                firstname=self.fname_txt.get()
                lastname=self.lname_txt.get()
                mobile=self.mob_txt.get()
                email=self.mail_txt.get()
                username=self.username_txt.get()
                password=self.password_txt.get()
                que=self.S_que_cmb.get()
                ans=self.ans_txt.get()
                record=(firstname,lastname,mobile,email,username,password,que,ans)
                
            #   checking for existing user
                cur.execute("select uname from stud where uname=%s",self.username_txt.get())
                row=cur.fetchone()

                cur.execute("select admin_username from admin where admin_username=%s",self.username_txt.get())
                row1=cur.fetchone()
                if row!=None:
                        messagebox.showerror("Error","Sorry Username already exists.....",parent=self.root)
                elif row1!=None:
                        messagebox.showerror("Error","Sorry Username already exists.....",parent=self.root)
                else:
                    insert_query="""insert into stud(fname,lname,Mob,email,uname,pass,que,ans)values(%s, %s, %s, %s, %s, %s, %s, %s)"""
                    cur.execute(insert_query,record)
                    con.commit()
                    messagebox.showinfo("Success","Registration Successfull..!!!!",parent=self.root)
                    callRegister()
            finally:
                con.close()

root = Tk()
def callLogin():
      root.destroy()
      os.system('python Get_Registered.py')

def callRegister():
     root.destroy() 
     os.system('python Register.py')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
obj = Register(root)
root.state('zoomed')
root.resizable(False,False)
root.mainloop()
