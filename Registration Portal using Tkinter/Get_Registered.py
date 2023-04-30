from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
import pymysql
from User import trial
from Admin import show

class Login():
    
    
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("%dx%d" % (sw,sh))
        self.root.wm_iconbitmap("appicon.ico")
        

        #=== Bg Image ====#
        self.bg=ImageTk.PhotoImage(file="img/bgf.jpg")
        lbgimage=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        namelabel=Label(self.root,text="Presented by Shubham Shinde",font=("times new roman",15,"italic","bold"),bg="cyan",fg="black").place(x=1250,y=790)


        #=== Login Frame ===#
        frame2=Frame(self.root,bg="orange")
        frame2.place(x=500,y=200,width=500,height=450)

        #=== Login Frame component ===#
        ltitle=Label(frame2,text="Login HERE !!",font=("times new roman",30,"italic","bold"),bg="orange",fg="black").place(x=50,y=30)

        #=== 1st row ==#
        u=Label(frame2,text="Username ",font=("Comic Sans MS",15,"bold"),bg="orange",fg="black").place(x=190,y=110)
        self.username_txt=Entry(frame2,font=("Comic Sans MS",13,"italic"),bg="white",fg="black")
        self.username_txt.place(x=120,y=150,width=250)

        p=Label(frame2,text="Password ",font=("Comic Sans MS",15,"bold"),bg="orange",fg="black").place(x=190,y=210)
        self.password_txt=Entry(frame2,font=("Comic Sans MS",13,"italic"),show="*",bg="white",fg="black")
        self.password_txt.place(x=120,y=250,width=250)

        #=== Sign In ===#
        login_btn=Button(frame2,text="Login",bg="black",fg="white",font=("Comic Sans MS",13,"italic"),cursor="hand2",command=self.login_data).place(x=250,y=330,width=150,height=40)

        # == Signup button ===#
        submit_btn = Button(frame2, text="Sign Up",bg="black",fg="white",font=("Comic Sans MS",13,"italic"), bd=1, cursor="hand2",command=callRegister).place(x=80, y=330, width=150, height=40)

        # Exit Button
        exit_btn=Button(frame2,text="Exit [->",bg="orange",fg="black",font=("Comic Sans MS",10,"italic"),bd=2,cursor="hand2",command=exit).place(x=410,y=420,width=70,height=25)

    def login_data(self):
        if self.username_txt.get()=="" or self.password_txt.get()=="" :
            messagebox.showerror("Error","All fields are required ......",parent=self.root)
        else:
            con=pymysql.connect(host='localhost',user='root',password='shubham@29',database='activity')
            cur=con.cursor()
            try:
                username=self.username_txt.get()
                password=self.password_txt.get()
                
            #   checking for existing user
                cur.execute("select uname from stud where uname=%s",self.username_txt.get())
                uname=cur.fetchone()

                cur.execute("select pass from stud where uname=%s",self.username_txt.get())
                upass=cur.fetchone()
                

                cur.execute("select admin_username from admin where admin_username=%s",self.username_txt.get())
                aname=cur.fetchone()

                cur.execute("select password from admin where admin_username=%s",self.username_txt.get())
                apass=cur.fetchone()
                

                if uname!=None or aname!=None:
                    if upass!=None:
                        if upass[0]==password:
                            messagebox.showinfo("Success","Welcome User.....",parent=self.root)
                            root.destroy()
                            trial(username)
                        else:
                            messagebox.showerror("Error","Wrong password....",parent=self.root)
                    elif apass!=None:
                        if apass[0]==password:
                            messagebox.showinfo("Success","Welcome Admin.....",parent=self.root)
                            root.destroy()
                            show()
                        else:
                            messagebox.showerror("Error","Wrong password....",parent=self.root)
                else:
                    messagebox.showerror("Error","Username not found....",parent=self.root)
        
            finally:
                con.close()


root=Tk()

def callRegister():
     root.destroy()
     os.system('python Register.py')

def exit():
    res=messagebox.askquestion('Exit Application', 'Do you really want to exit ?')
    if res == 'yes' :
        root.destroy()


sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
root.state('zoomed')
root.resizable(False,False)
objl=Login(root)
root.mainloop()