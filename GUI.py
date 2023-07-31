import tkinter as tk
from tkinter import ttk
from tkinter import *
import Database
import registration
import sign_in
import transaction

class login(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry("925x500+300+200")
        self.configure(bg="#fff")
        self.resizable(False,False)
        self.structure()
        self.entry_widgets()
        self.submit()


        
    


    def structure(self):
        self.img=PhotoImage(file='login.png')
        Label(self,image=self.img,bg='white').place(x=50,y=50)  
        self.frame=Frame(self,width=350,height=350,bg="white")
        self.frame.place(x=480,y=70)
        heading=Label(self.frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)
    def entry_widgets(self):
        def on_enter(event):
            self.user.delete(0,tk.END)
        def on_leave(event):
            if self.user.get()=='':
                self.user.insert(0,"Username")
        self.user=Entry(self.frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30,y=80)
        self.user.insert(0,'Username')
        self.user.bind('<FocusIn>',on_enter)
        self.user.bind('<FocusOut>',on_leave)
        Frame(self.frame,width=295,height=2,bg="black").place(x=25,y=107)
        def on_enter(event):
            self.code.delete(0,tk.END)
        def on_leave(event):
            if self.code.get()=='':
                self.code.insert(0,"Password")
        self.code=Entry(self.frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
        self.code.place(x=30,y=150)
        self.code.insert(0,'Password')
        self.code.bind('<FocusIn>',on_enter)
        self.code.bind('<FocusOut>',on_leave)
        Frame(self.frame,width=295,height=2,bg="black").place(x=25,y=177)
        
    def submit(self):
        def signin():
            username=self.user.get()
            password=self.code.get()
            accno=sign_in.sign(username,password)
            if accno:
                self.withdraw()
                switching=main_frame(accno)
                switching.show__window()
            else:
                Label(self.frame,text="Wrong Username or Password",bg="#fff",fg="red").place(x=30,y=180)
        def sign__up():
            self.withdraw()
            signup_window=signup()
            signup_window.previous_window = self
            signup_window.mainloop()

        self.button=Button(self.frame,text="Sign In",width=39,pady=7,bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
        label=Label(self.frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=75,y=270)
        self.sign_up=Button(self.frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign__up)
        self.sign_up.place(x=215,y=270)
class signup(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        self.title("SignUp")
        self.geometry('750x600+300+100')
        self.configure(bg='#fff')
        self.resizable(False,False)
        self.structure()
        self.entry_widgets()
        self.submit()


    def structure(self):
        self.img=PhotoImage(file="fun-cartoon-kid-with-rain-gear.png")
        Label(self,image=self.img,border=0,bg="white").place(x=30,y=150)

        self.frame2= Frame(self,width=325,height=500,bg='#fff')
        self.frame2.place(x=410,y=50)
    def entry_widgets(self):
        self.heading=Label(self.frame2,text="Register",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=100,y=5)
        #=====================================================
        def on_enter(event):
            if self.name.get()=='Enter Your Full Name':
                self.name.delete(0,tk.END)
        def on_leave(event):
            if self.name.get()=='':
                self.name.insert(0,"Enter Your Full Name")
        self.name=Entry(self.frame2,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
        self.name.place(x=30,y=80)
        self.name.insert(0,"Enter Your Full Name")
        self.name.bind("<FocusIn>",on_enter)
        self.name.bind("<FocusOut>",on_leave)
        Frame(self.frame2,width=295,height=2,bg='black').place(x=25,y=107)
    #======================================================================================
        def on_enter(event):
            if self.address.get()=='Enter Your Address':
                self.address.delete(0,tk.END)
        def on_leave(event):
            if self.address.get()=='':
                self.address.insert(0,"Enter Your Address")
        self.address=Entry(self.frame2,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
        self.address.place(x=30,y=150)
        self.address.insert(0,"Enter Your Address")
        self.address.bind("<FocusIn>",on_enter)
        self.address.bind("<FocusOut>",on_leave)
        Frame(self.frame2,width=295,height=2,bg='black').place(x=25,y=177)
#=================================================================================
        def on_enter(e):
            if self.phn_no.get()=='Enter Your Phone Number':
                self.phn_no.delete(0,tk.END)
        def on_leave(e):
            if self.phn_no.get()=='':
                self.phn_no.insert(0,"Enter Your Phone Number")
        self.phn_no=Entry(self.frame2,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
        self.phn_no.place(x=30,y=220)
        self.phn_no.insert(0,"Enter Your Phone Number")
        self.phn_no.bind("<FocusIn>",on_enter)
        self.phn_no.bind("<FocusOut>",on_leave)
        Frame(self.frame2,width=295,height=2,bg='black').place(x=25,y=247)
#===================================================================================
        def on_enter(e):
            if self.Email.get()=='Enter Your Email':
                self.Email.delete(0,tk.END)
        def on_leave(e):
            if self.Email.get()=='':
                self.Email.insert(0,"Enter Your Email")
        self.Email=Entry(self.frame2,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
        self.Email.place(x=30,y=290)
        self.Email.insert(0,"Enter Your Email")
        self.Email.bind("<FocusIn>",on_enter)
        self.Email.bind("<FocusOut>",on_leave)
        Frame(self.frame2,width=295,height=2,bg='black').place(x=25,y=317)
#=====================================================================================
        def on_enter(e):
            if self.Dob.get()=='Enter Your Date Of Birth':
                self.Dob.delete(0,tk.END)
        def on_leave(e):
            if self.Dob.get()=='':
                self.Dob.insert(0,"Enter Your Date Of Birth")
        self.Dob=Entry(self.frame2,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
        self.Dob.place(x=30,y=360)
        self.Dob.insert(0,"Enter Your Date Of Birth")
        self.Dob.bind("<FocusIn>",on_enter)
        self.Dob.bind("<FocusOut>",on_leave)
        Frame(self.frame2,width=295,height=2,bg='black').place(x=25,y=387)
    

    def submit(self):
        def generate(Acc_no):
            
            username,password=sign_in.generator(Acc_no)
            
            self.withdraw()
            credential_window=credential(username,password,Acc_no)
            credential_window.show_window()

            
        
        def sign_up():
            name=self.name.get()
            address=self.address.get()
            phn_no=self.phn_no.get()
            email=self.Email.get()
            DOB=self.Dob.get()
            user=registration.registration(name,address,phn_no,email,DOB)
            user.save_to_file()
            self.button.destroy()
            Acc_no=Database.account_no(name)
            self.gen=Button(self.frame2,text='Generate User Name Password',width=39,pady=7,bg='#8D28C4',fg='white',border=0,command=lambda: generate(Acc_no))
            self.gen.place(x=35, y=430)
            

        def signed_in():
            self.destroy()
            self.previous_window.deiconify()
        self.button = Button(self.frame2, text="Sign Up", width=39, pady=7, bg='#57a1f8', fg='white', border=0, command=sign_up)
        self.button.place(x=35, y=430)

        self.label=Label(self.frame2,text='I have an account!!',fg='black',bg='white',font=("Microsoft YaHei UI Light",9))
        self.label.place(x=90,y=470)

        self.signin=Button(self.frame2,width=6,text='sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signed_in)
        self.signin.place(x=200,y=470)
# import tkinter as tk
# from tkinter import ttk
# from tkinter import *
# import Database
# import registration
# import sign_in
# from PIL import ImageTk, Image
class credential(tk.Toplevel):
    def __init__(self,username,password,account):
        super().__init__()
        
        self.title("Credential")
        self.geometry("1200x725+300+200")
        self.configure(bg="#fff")
        self.resizable(False,False)
        self.user=username
        self.pass123=password
        self.acc=account
        self.create_canvas()
    def create_canvas(self):
        def switch(account_number):
            self.withdraw()
            switching=main_frame(account_number)
            switching.show__window()
        self.background=PhotoImage(file='kolkata_colour.png')
        self.mycanvas=Canvas(self,width=1387,height=750)
        self.mycanvas.pack(fill='both',expand=True)
        self.mycanvas.create_image(0,0,image=self.background,anchor='nw')
        textttt="USERNAME : "+str(self.user)+'\n'+"PASSWORD : "+str(self.pass123)+"\n"+"Acc. No. : "+str(self.acc)
        self.mycanvas.create_text(650,460,text=textttt,font=("Copperplate Gothic Bold",50,'bold'))
        imageee=PhotoImage(file="transparent.png")
        self.button=Button(self,text='Go To Workspace',fg="#59FBFF",bg="#505B77",font=("Franklin Gothic Medium Cond",14,'bold'),command=lambda: switch(self.acc))
        self.mycanvas.create_window(1000,32,window=self.button)
    def show_window(self):
        self.mainloop()
# credential("param123","1234","41566516165")
#=======================================================================================================================================================

class main_frame(tk.Toplevel):
    def __init__(self,account_number):
        super().__init__()
        
        self.title("Dashboard")
        self.geometry("1478x802+300+200")
        self.configure(bg="#fff")
        self.resizable(False,False)
        self.buttonframe=Frame(self,width=197,height=802,bg="#fff")
        self.buttonframe.place(x=0,y=0)
        self.ACC_no=account_number
        self.button()
        self.home()
    def show__window(self):
        self.mainloop()
    def home(self):
        self.totalframe=Frame(self,width=1281,height=802,bg="#fff")
        self.totalframe.place(x=197,y=0)
        self.frame4=Frame(self,width=1188,height=127,bg="#fff")
        self.frame4.place(x=234,y=39)
        self.menu=PhotoImage(file="menu.png")
        Label(self,image=self.menu,border=0,bg="#fff").place(x=1051,y=215)
        self.title=Label(self.frame4,text="WELCOME TO BANK MANAGEMENT SYSTEM",bg="#fff",fg="black",font=("Book Antiqua",24))
        self.title.place(x=234,y=39)
        self.frame5=Frame(self,width=244,height=355,bg="#fff")
        self.frame5.place(x=1100,y=272)
        self.theme=PhotoImage(file="cut-and-plant.png")
        Label(self,image=self.theme,border=0,bg="#fff").place(x=300,y=340)
        # getyouknow(table,inputval,input1,output1,output2,output3,output4,output5,output6,output7)
        name=transaction.getyouknow("users",self.ACC_no,"account_number","name","0","0","0","0","0","0")
        texttt = "Name = {}".format(name)
        self.namelabel = Label(self.frame5, text=texttt, bg="#fff", fg="#4472C4", font=("Bodoni MT", 12))
        self.namelabel.place(x=1150, y=280)

        



    def button(self):
        self.home_button=Button(self.buttonframe,text="Home",width=15,height=1,bg="#fff",fg="black",border=0,font=("Microsoft YaHei UI Light",15),command=self.home)
        self.home_button.place(x=10,y=82)
        self.deposit=Button(self.buttonframe,text="Deposit",width=15,height=1,bg="#fff",fg='black',border=0,font=("Microsoft YaHei UI Light",15),command=self.deposit)
        self.deposit.place(x=15,y=140)
        self.withdraw=Button(self.buttonframe,text="Withdraw",width=15,height=1,bg="#fff",fg='black',border=0,font=("Microsoft YaHei UI Light",15),command=self.withdraw)
        self.withdraw.place(x=17,y=198)
        self.transfer=Button(self.buttonframe,text="Transfer",width=15,height=1,bg="#fff",fg='black',border=0,font=("Microsoft YaHei UI Light",15),command=self.transfer)
        self.transfer.place(x=17,y=256)
        self.transhistorty=Button(self.buttonframe,text="Transaction\nHistory",width=15,height=2,bg="#fff",fg='black',border=0,font=("Microsoft YaHei UI Light",15),command=self.transhis)
        self.transhistorty.place(x=17,y=314)
        self.scheme=Button(self.buttonframe,text="scheme",width=15,height=3,bg="#fff",fg='black',border=0,font=("Microsoft YaHei UI Light",15),command=self.scheme)
        self.scheme.place(x=17,y=380)
        self.exit=Button(self.buttonframe,text="Exit",width=15,height=2,bg="#fff",fg='black',border=0,font=("Microsoft YaHei UI Light",15),command=self.exit)
        self.exit.place(x=17,y=455)
  

    def deposit(self):
        def yes():
            amount=self.amountdeposit.get()
            transaction.trans(self.ACC_no,"1",amount,0)
            self.frameyes = Frame(self, width=1281, height=802, bg="#fff")
            self.frameyes.place(x=197, y=0)
            Label(self.frameyes,text="The confirmation message will go on your whatsapp.",bg="#fff",font=("Bodoni MT",24)).place(x=344,y=320)

        self.framedeposit = Frame(self, width=1281, height=802, bg="#fff")
        self.framedeposit.place(x=197, y=0)
      
        textttt = "your Account number=" + str(self.ACC_no)
        self.accno = Label(self.framedeposit, text=textttt,bg="white", font=("Metalsmith", 36))
        self.accno.place(x=220, y=123)
        self.textdeposit=Label(self.framedeposit,text="Amount",bg="#fff",fg="Black",font=("Bahnschrift Light",32))
        self.textdeposit.place(x=220,y=243)
        self.amountdeposit=Entry(self.framedeposit,bg="#fff",width=50,border=1)
        self.amountdeposit.place(x=392,y=265)
        self.permisson=Label(self.framedeposit,text="Want to proceed?",bg="#fff",font=("Bodoni MT",24))
        self.permisson.place(x=210,y=351)
        self.yesdeposit=Button(self.framedeposit,text="YES",font=("Bodoni MT",20),bg="#fff",border=0,command=yes)
        self.yesdeposit.place(x=221,y=390)
        self.nodeposit=Button(self.framedeposit,text="NO",font=("Bodoni MT",20),bg="#fff",border=0,command=self.home)
        self.nodeposit.place(x=221,y=430)

        # transaction.trans(self.ACC_no,"1")
        
    def withdraw(self):
        def yes():
            amount=self.amountwithdraw.get()
            transaction.trans(self.ACC_no,"2",amount,0)
            self.frameyes = Frame(self, width=1281, height=802, bg="#fff")
            self.frameyes.place(x=197, y=0)
            Label(self.frameyes,text="The confirmation message will go on your whatsapp.",bg="#fff",font=("Bodoni MT",24)).place(x=344,y=320)
        self.framewithdraw=Frame(self,width=1281,height=802,bg="#fff")
        self.framewithdraw.place(x=197,y=0)

        textttt = "your Account number=" + str(self.ACC_no)
        self.accno = Label(self.framewithdraw, text=textttt,bg="white", font=("Metalsmith", 36))
        self.accno.place(x=220, y=123)
        self.textwithdraw=Label(self.framewithdraw,text="Amount",bg="#fff",fg="Black",font=("Bahnschrift Light",32))
        self.textwithdraw.place(x=220,y=243)

        self.amountwithdraw=Entry(self.framewithdraw,bg="#fff",width=50,border=1)
        self.amountwithdraw.place(x=392,y=265)
        self.permisson=Label(self.framewithdraw,text="Want to proceed?",bg="#fff",font=("Bodoni MT",24))
        self.permisson.place(x=210,y=351)
        self.yesdeposit=Button(self.framewithdraw,text="YES",font=("Bodoni MT",20),bg="#fff",border=0,command=yes)
        self.yesdeposit.place(x=221,y=390)
        self.nodeposit=Button(self.framewithdraw,text="NO",font=("Bodoni MT",20),bg="#fff",border=0,command=self.home)
        self.nodeposit.place(x=221,y=430)
    def transfer(self):
        def yes():
            amount=self.amounttransfer.get()
            transaction.trans(self.ACC_no,"2",amount,recacc.get())
            self.frameyes = Frame(self, width=1281, height=802, bg="#fff")
            self.frameyes.place(x=197, y=0)
            Label(self.frameyes,text="The confirmation message will go on your whatsapp.",bg="#fff",font=("Bodoni MT",24)).place(x=344,y=320)
        self.frametransfer=Frame(self,width=1281,height=802,bg="#fff")
        self.frametransfer.place(x=197,y=0)

        textttt = "your Account number=" + str(self.ACC_no)
        self.accno = Label(self.frametransfer, text=textttt,bg="white", font=("Metalsmith", 36))
        self.accno.place(x=220, y=123)
        self.texttransfer=Label(self.frametransfer,text="Amount",bg="#fff",fg="Black",font=("Bahnschrift Light",32))
        self.texttransfer.place(x=220,y=243)
        Label(self.frametransfer,text="Give reciever account number:",bg="#fff",font=("Cambria",24)).place(x=218,y=300)
        recacc=Entry(self.frametransfer,width=40,bg="#fff",border=1)
        recacc.place(x=652,y=320)
        self.amounttransfer=Entry(self.frametransfer,bg="#fff",width=50,border=1)
        self.amounttransfer.place(x=392,y=265)
        self.permisson=Label(self.frametransfer,text="Want to proceed?",bg="#fff",font=("Bodoni MT",24))
        self.permisson.place(x=210,y=351)
        self.yesdeposit=Button(self.frametransfer,text="YES",font=("Bodoni MT",20),bg="#fff",border=0,command=yes)
        self.yesdeposit.place(x=221,y=390)
        self.nodeposit=Button(self.frametransfer,text="NO",font=("Bodoni MT",20),bg="#fff",border=0,command=self.home)
        self.nodeposit.place(x=221,y=430)
    def transhis(self):
        transaction.transaction_details(self.ACC_no)
    def exit(self):
        self.destroy()
    def scheme(self):
        self.framescehme=Frame(self,width=1281,height=802,bg="#fff")
        self.framescehme.place(x=197,y=0)
        Label(self.framescehme,text="UNDER    MAINTAINANCE",bg="#fff",fg="black",font=("Bodoni MT",60)).place(x=250,y=342)





# main_frame("115148465184")

# credential("param123",'1234',"85459145918")

print("Working.....")

app=login()
app.mainloop()