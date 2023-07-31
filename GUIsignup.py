# # from tkinter import *
# # from tkinter import messagebox
# # import ast
# # import registration

# window=Tk()
# window.title("SignUp")
# window.geometry('750x600+300+100')
# window.configure(bg='#fff')
# window.resizable(False,False)


# img=PhotoImage(file='signup.png')
# Label(window,image=img,border=0,bg="white").place(x=30,y=150)

# frame= Frame(window,width=325,height=500,bg='#fff')
# frame.place(x=410,y=50)

# # def signup():
# #     Name=name.get()
# #     Address=address.get()
# #     PHN_no=phn_no.get()
# #     email=Email.get()
# #     DOB=Dob.get()
# #     user=registration.registration(Name,Address,PHN_no,email,DOB)
# #     user.confirmation()
# #     user.save_to_file()
# #     run_tkinter_app()
# #     return name
    
# # heading=Label(frame,text="Register",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
# # heading.place(x=100,y=5)
# # ###----------------------------------------------------------------------------
# def on_enter(e):
#     if name.get()=='Enter Your Full Name':
#         name.delete(0,'end')
# def on_leave(e):
#     if name.get()=='':
#         name.insert(0,"Enter Your Full Name")
# name=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# name.place(x=30,y=80)
# name.insert(0,"Enter Your Full Name")
# name.bind("<FocusIn>",on_enter)
# name.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
# # ###----------------------------------------------------------------------------
# def on_enter(e):
#     if address.get()=='Enter Your Address':
#         address.delete(0,'end')
# def on_leave(e):
#     if address.get()=='':
#         address.insert(0,"Enter Your Address")
# address=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# address.place(x=30,y=150)
# address.insert(0,"Enter Your Address")
# address.bind("<FocusIn>",on_enter)
# address.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


# # ###----------------------------------------------------------------------------
# def on_enter(e):
#     if phn_no.get()=='Enter Your Phone Number':
#         phn_no.delete(0,'end')
# def on_leave(e):
#     if phn_no.get()=='':
#         phn_no.insert(0,"Enter Your Phone Number")
# phn_no=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# phn_no.place(x=30,y=220)
# phn_no.insert(0,"Enter Your Phone Number")
# phn_no.bind("<FocusIn>",on_enter)
# phn_no.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


# # ###----------------------------------------------------------------------------
# def on_enter(e):
#     if Email.get()=='Enter Your Email':
#         Email.delete(0,'end')
# def on_leave(e):
#     if Email.get()=='':
#         Email.insert(0,"Enter Your Email")
# Email=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# Email.place(x=30,y=290)
# Email.insert(0,"Enter Your Email")
# Email.bind("<FocusIn>",on_enter)
# Email.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)
# # ###----------------------------------------------------------------------------
# def on_enter(e):
#     if Dob.get()=='Enter Your Date Of Birth':
#         Dob.delete(0,'end')
# def on_leave(e):
#     if Dob.get()=='':
#         Dob.insert(0,"Enter Your Date Of Birth")
# Dob=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# Dob.place(x=30,y=360)
# Dob.insert(0,"Enter Your Date Of Birth")
# Dob.bind("<FocusIn>",on_enter)
# Dob.bind("<FocusOut>",on_leave)
# Frame(frame,width=295,height=2,bg='black').place(x=25,y=387)
# #-----------------------------------------------------------------------------------------
# Button(frame,width=39,pady=7,text="Sign Up",bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=430)
# label=Label(frame,text='I have an account!!',fg='black',bg='white',font=("Microsoft YaHei UI Light",9))
# label.place(x=90,y=470)

# signin=Button(frame,width=6,text='sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
# signin.place(x=200,y=470)

# # #------------------------------------------------------------------------------------------------------------------

# # # window.title("CREDENTIAL")
# # # window.geometry('1024x682+300+100')
# # # window.configure(bg='#fff')
# # # window.resizable(False,False)



# # # frame=Frame(window,height=400,width=1200,bg='#fff')
# # # frame.place(x=200,y=300)

# # # background1=PhotoImage(file='background.png')
# # # Label(window,image=background1,bg='white').place(x=0,y=0)




# # import subprocess


# # def execute_another_module():
# #     window.destroy()
# #     subprocess.Popen(['python', 'credential.py'])

# # def run_tkinter_app():
# #     # Create your Tkinter application here
    
# #     # ...
# #     # Add your Tkinter code

    
# #     execute_another_module()

# #     # Start the Tkinter event loop
# #     window.mainloop()

# # # Call the function to run your Tkinter application















# # window.mainloop()










# #====================================================================================================================================





# # from tkinter import *
# # from tkinter import messagebox
# # import pymysql
# # import Database
# # import sign_in
# # import registration
# # import subprocess
# # window=Tk()

# # class register:
# #     def __init__(self):
# #         window.title("SignUp")
# #         window.geometry('750x600+300+100')
# #         window.configure(bg='#fff')
# #         window.resizable(False,False)
# #     def image():
# #         img=PhotoImage(file='signup.png')
# #         Label(window,image=img,border=0,bg="white").place(x=30,y=150)
   
# #     def entry():
# #         frame= Frame(window,width=325,height=500,bg='#fff')
# #         frame.place(x=410,y=50)
# #         heading=Label(frame,text="Register",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
# #         heading.place(x=100,y=5)
# #         def on_enter(var,text):
# #             if var.get()==text:
# #                 var.delete(0,'end')
# #         def on_leave(var,text):
# #             if var.get()=='':
# #                 var.insert(0,text)
# #         name=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# #         name.place(x=30,y=80)
# #         name.insert(0,"Enter Your Full Name")
# #         name.bind("<FocusIn>",on_enter(name,"Enter Your Full Name"))
# #         name.bind("<FocusOut>",on_leave(name,"Enter Your Full Name"))
# #         Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
# #         address=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# #         address.place(x=30,y=150)
# #         address.insert(0,"Enter Your Address")
# #         address.bind("<FocusIn>",on_enter(address,"Enter Your Address"))
# #         address.bind("<FocusOut>",on_leave(address,"Enter Your Address"))
# #         Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)  
# #         phn_no=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# #         phn_no.place(x=30,y=220)
# #         phn_no.insert(0,"Enter Your Phone Number")
# #         phn_no.bind("<FocusIn>",on_enter)
# #         phn_no.bind("<FocusOut>",on_leave)
# #         Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)  
# #         Email=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# #         Email.place(x=30,y=290)
# #         Email.insert(0,"Enter Your Email")
# #         Email.bind("<FocusIn>",on_enter)
# #         Email.bind("<FocusOut>",on_leave)
# #         Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)
# #         Dob=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
# #         Dob.place(x=30,y=360)
# #         Dob.insert(0,"Enter Your Date Of Birth")
# #         Dob.bind("<FocusIn>",on_enter)
# #         Dob.bind("<FocusOut>",on_leave)
# #         return name.get(),address.get(),phn_no.get(),Email.get(),Dob.get()
# #     def button():
# #         frame= Frame(window,width=325,height=500,bg='#fff')
# #         frame.place(x=410,y=50)
# #         Frame(frame,width=295,height=2,bg='black').place(x=25,y=387)
# #         Button(frame,width=39,pady=7,text="Sign Up",bg='#57a1f8',fg='white',border=0).place(x=35,y=430)
# #         label=Label(frame,text='I have an account!!',fg='black',bg='white',font=("Microsoft YaHei UI Light",9))
# #         label.place(x=90,y=470)

# #         signin=Button(frame,width=6,text='sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
# #         signin.place(x=200,y=470)
# #     def signup(Name,Address,PHN_no,email,DOB):
       
# #         user=registration.registration(Name,Address,PHN_no,email,DOB)
# #         user.confirmation()
# #         user.save_to_file()
# #         run_tkinter_app()
# #         return 
# #     def credit():
# #         window.title('Login')
# #         window.geometry("1387x750+300+200") 
# #         window.configure(bg="#fff")
# #         window.resizable(False,False)
# #         background1=PhotoImage(file='kolkata_colour.png')
# #         my_canvas= Canvas(window,width=1387,height=750)
# #         my_canvas.pack(fill='both',expand=True)
# #         my_canvas.create_image(0,0, image=background1,anchor="nw")



# # register.image()
# # Name,Address,PHN_no,email,DOB=register.entry()
# # register.button()
# # register.signup(Name,Address,PHN_no,email,DOB)
# # register.credit()


# #==================================================================================
# from tkinter import *
# from tkinter import messagebox
# import pymysql
# import Database
# import sign_in
# import registration
# import subprocess
# window=Tk()
# class register:
#     def __init__(self):
#         window = Tk()
#         window.title("SignUp")
#         window.geometry('750x600+300+100')
#         window.configure(bg='#fff')
#         window.resizable(False, False)

#     @staticmethod
#     def image():
#         img = PhotoImage(file='signup.png')
#         Label(window, image=img, border=0, bg="white").place(x=30, y=150)

#     @staticmethod
#     def entry():
#         def on_enter(var, text):
#             if var.get() == text:
#                 var.delete(0, 'end')

#         def on_leave(var, text):
#             if var.get() == '':
#                 var.insert(0, text)

#         frame = Frame(window, width=325, height=500, bg='#fff')
#         frame.place(x=410, y=50)
#         heading = Label(frame, text="Register", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
#         heading.place(x=100, y=5)

#         name = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
#         name.place(x=30, y=80)
#         name.insert(0, "Enter Your Full Name")
#         name.bind("<FocusIn>", lambda event: on_enter(name, "Enter Your Full Name"))
#         name.bind("<FocusOut>", lambda event: on_leave(name, "Enter Your Full Name"))
#         Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
#         address=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
#         address.place(x=30,y=150)
#         address.insert(0,"Enter Your Address")
#         address.bind("<FocusIn>", lambda event: on_enter(address, "Enter Your Address"))
#         address.bind("<FocusOut>", lambda event: on_leave(address, "Enter Your Address"))
#         Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)  
#         phn_no=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
#         phn_no.place(x=30,y=220)
#         phn_no.insert(0,"Enter Your Phone Number")
#         phn_no.bind("<FocusIn>",lambda event: on_enter(phn_no, "Enter Your Phone Number"))
#         phn_no.bind("<FocusOut>",lambda event: on_leave(phn_no, "Enter Your Phone Number"))
#         Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)  
#         Email=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
#         Email.place(x=30,y=290)
#         Email.insert(0,"Enter Your Email")
#         Email.bind("<FocusIn>",lambda event: on_enter(Email, "Enter Your Email"))
#         Email.bind("<FocusOut>",lambda event: on_leave(Email, "Enter Your Email"))
#         Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)
#         Dob=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
#         Dob.place(x=30,y=360)
#         Dob.insert(0,"Enter Your Date Of Birth")
#         Dob.bind("<FocusIn>",lambda event: on_enter(Dob, "Enter Your Date of Birth"))
#         Dob.bind("<FocusOut>",lambda event: on_enter(Dob, "Enter Your Date of Birth"))


#         # Add other entry widgets (address, phone number, email, DOB) similarly

#         return name.get(), address.get(), phn_no.get(), Email.get(), Dob.get()

#     @staticmethod
#     def button():
#         frame = Frame(window, width=325, height=500, bg='#fff')
#         frame.place(x=410, y=50)
#         Frame(frame, width=295, height=2, bg='black').place(x=25, y=387)
#         Button(frame, width=39, pady=7, text="Sign Up", bg='#57a1f8', fg='white', border=0).place(x=35, y=430)
#         label = Label(frame, text='I have an account!!', fg='black', bg='white', font=("Microsoft YaHei UI Light", 9))
#         label.place(x=90, y=470)

#         signin = Button(frame, width=6, text='sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
#         signin.place(x=200, y=470)

#     @staticmethod
#     def signup(Name, Address, PHN_no, email, DOB):
#         user = registration.registration(Name, Address, PHN_no, email, DOB)
#         user.confirmation()
#         user.save_to_file()
        
#         return

#     @staticmethod
#     def credit():
#         window.title('Login')
#         window.geometry("1387x750+300+200")
#         window.configure(bg="#fff")
#         window.resizable(False, False)
#         background1 = PhotoImage(file='kolkata_colour.png')
#         my_canvas = Canvas(window, width=1387, height=750)
#         my_canvas.pack(fill='both', expand=True)
#         my_canvas.create_image(0, 0, image=background1, anchor="nw")


# register.image()
# Name, Address, PHN_no, Email, Dob = register.entry()
# register.button()
# register.signup(Name, Address, PHN_no, Email, Dob)
# register.credit()

# window.mainloop()
