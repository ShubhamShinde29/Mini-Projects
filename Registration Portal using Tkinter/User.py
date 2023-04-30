from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import pymysql
from tabulate import tabulate
import os

def trial(u):
    userroot=Tk()   
    userroot.title("User Page")
    sw = userroot.winfo_screenwidth()
    sh = userroot.winfo_screenheight()
    userroot.geometry("%dx%d" % (sw, sh))
    userroot.wm_iconbitmap("appicon.ico")

    con=pymysql.connect(host='localhost',user='root',password='shubham@29',database='activity')
    cur=con.cursor()
    try:
        cur.execute("select * from stud where uname=%s",u)
    except:
        pass
    finally:
        con.close()

    # === Bg Image ====#
    bg = ImageTk.PhotoImage(file="img/bgf.jpg")
    bgimage = Label(userroot, image=bg).place(
    x=0, y=0, relwidth=1, relheight=1)

    namelabel=Label(userroot,text="Presented by Shubham Shinde",font=("times new roman",15,"italic","bold"),bg="cyan",fg="black").place(x=1250,y=790)


    # === Register Frame ===#
    frame1 = Frame(userroot, bg="pink",highlightbackground="black",highlightthickness=3)
    frame1.place(x=230, y=120, width=1150, height=550)

    # === Frame component ===#
    title = Label(frame1, text=("Welcome  User !!"), font=("times new roman", 30, "italic","bold" ), bg="pink", fg="black").place(x=50, y=30)
    game_frame = Frame(frame1,bg="pink",highlightbackground="black",highlightthickness=3)
    game_frame.place(x=120,y=100,width=900,height=250)

    #scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(game_frame,orient='horizontal')
    game_scroll.pack(side= BOTTOM,fill=X)

    my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    #define our column
    
    my_game['columns'] = ('ID', 'FirstName', 'LastName','Mobile','Email','UserName','Password','Security Question','Answer')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("ID",anchor=CENTER, width=80)
    my_game.column("FirstName",anchor=CENTER,width=80)
    my_game.column("LastName",anchor=CENTER,width=80)
    my_game.column("Mobile",anchor=CENTER, width=80)
    my_game.column("Email",anchor=CENTER,width=80)
    my_game.column("UserName",anchor=CENTER,width=80)
    my_game.column("Password",anchor=CENTER, width=80)
    my_game.column("Security Question",anchor=CENTER,width=80)
    my_game.column("Answer",anchor=CENTER,width=80)


    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("ID",text="ID",anchor=CENTER)
    my_game.heading("FirstName",text="FirstName",anchor=CENTER)
    my_game.heading("LastName",text="LastName",anchor=CENTER)
    my_game.heading("Mobile",text="Mobile",anchor=CENTER)
    my_game.heading("Email",text="Email",anchor=CENTER)
    my_game.heading("UserName",text="UserName",anchor=CENTER)
    my_game.heading("Password",text="Password",anchor=CENTER)
    my_game.heading("Security Question",text="Security Question",anchor=CENTER)
    my_game.heading("Answer",text="Answer",anchor=CENTER)

    # fetch data
    count=0
    for i in cur:
        count+=1
        my_game.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

    frame = Frame(frame1,bg="pink",highlightbackground="black",highlightthickness=3)
    frame.place(x=5,y=400,width=1130,height=50)

    #labels
    p1= Label(frame,text = "ID")
    p1.grid(row=0,column=0 )

    p2 = Label(frame,text="FirstName")
    p2.grid(row=0,column=1)

    p3 = Label(frame,text="LastName")
    p3.grid(row=0,column=2)

    p4 = Label(frame,text="Mobile")
    p4.grid(row=0,column=3)

    p5 = Label(frame,text="Email")
    p5.grid(row=0,column=4)

    p6 = Label(frame,text="UserName")
    p6.grid(row=0,column=5)

    p7 = Label(frame,text="Password")
    p7.grid(row=0,column=6)

    p8 = Label(frame,text="S_Question")
    p8.grid(row=0,column=7)

    p9 = Label(frame,text="Answer")
    p9.grid(row=0,column=8)

    #Entry boxes
    p1_entry= Entry(frame)
    p1_entry.grid(row= 1,column=0)

    p2_entry = Entry(frame)
    p2_entry.grid(row=1,column=1)

    p3_entry = Entry(frame)
    p3_entry.grid(row=1,column=2)

    p4_entry = Entry(frame)
    p4_entry.grid(row=1,column=3)

    p5_entry = Entry(frame)
    p5_entry.grid(row=1,column=4)

    p6_entry = Entry(frame)
    p6_entry.grid(row=1,column=5)

    p7_entry = Entry(frame)
    p7_entry.grid(row=1,column=6)

    p8_entry = Entry(frame)
    p8_entry.grid(row=1,column=7)

    p9_entry = Entry(frame)
    p9_entry.grid(row=1,column=8)

    #Select Record
    def select_record():
        #clear entry boxes
        p1_entry.delete(0,END)
        p2_entry.delete(0,END)
        p3_entry.delete(0,END)
        p4_entry.delete(0,END)
        p5_entry.delete(0,END)
        p6_entry.delete(0,END)
        p7_entry.delete(0,END)
        p8_entry.delete(0,END)
        p9_entry.delete(0,END)
        
        #grab record
        selected=my_game.focus()
        #grab record values
        values = my_game.item(selected,'values')

        #output to entry boxes
        p1_entry.insert(0,values[0])
        p1_entry.configure(state=DISABLED)
        p2_entry.insert(0,values[1])
        p3_entry.insert(0,values[2])
        p4_entry.insert(0,values[3])
        p5_entry.insert(0,values[4])
        p6_entry.insert(0,values[5])
        p6_entry.configure(state=DISABLED)
        p7_entry.insert(0,values[6])
        p8_entry.insert(0,values[7])
        p8_entry.configure(state=DISABLED)
        p9_entry.insert(0,values[8])

    #save Record
    def update_record():
        selected=my_game.focus()
        # mysql connection
        con=pymysql.connect(host='localhost',user='root',password='shubham@29',database='activity')
        cur1=con.cursor()

        try:
            my_game.item(selected,text="",values=(p1_entry.get(),p2_entry.get(),p3_entry.get(),p4_entry.get(),p5_entry.get(),p6_entry.get(),p7_entry.get(),p8_entry.get(),p9_entry.get()))
            p6_entry.configure(state=NORMAL)
            p8_entry.configure(state=NORMAL)
            p1_entry.configure(state=NORMAL)
            cur1.execute("update stud set id=%s,fname=%s,lname=%s,Mob=%s,email=%s,uname=%s,pass=%s,que=%s,ans=%s where uname=%s",(p1_entry.get(),p2_entry.get(),p3_entry.get(),p4_entry.get(),p5_entry.get(),p6_entry.get(),p7_entry.get(),p8_entry.get(),p9_entry.get(),u))
            con.commit()
        except:
            pass

    #clear entry boxes
        p1_entry.delete(0,END)
        p2_entry.delete(0,END)
        p3_entry.delete(0,END)
        p4_entry.delete(0,END)
        p5_entry.delete(0,END)
        p6_entry.delete(0,END)
        p7_entry.delete(0,END)
        p8_entry.delete(0,END)
        p9_entry.delete(0,END)

    def login():
        userroot.destroy()
        os.system('python Get_Registered.py')

    #Buttons
    select_button = Button(frame1,text="Select Record",bg="black",fg="white",font=("Comic Sans MS",13,"italic"),cursor="hand2",command=select_record).place(x=300,y=480,width=150,height=40)
    refresh_button = Button(frame1,text="Update Record",bg="black",fg="white",font=("Comic Sans MS",13,"italic"),cursor="hand2",command=update_record).place(x=480,y=480,width=150,height=40)
    signout = Button(frame1,text="Sign Out",bg="black",fg="white",font=("Comic Sans MS",13,"italic"),cursor="hand2",command=login).place(x=660,y=480,width=150,height=40)

    userroot.state('zoomed')
    userroot.resizable(False,False)
    userroot.mainloop()

