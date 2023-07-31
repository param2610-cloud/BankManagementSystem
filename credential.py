from tkinter import *
from tkinter import messagebox
import pymysql

import Database
import sign_in
# import GUIsignup
connection=pymysql.connect(host="localhost",user='root',password='#S^9k6B0%N7',database='user_details',autocommit=True)
mycursor=connection.cursor()


root=Tk()
root.title('Login')
root.geometry("1387x750+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

root.title('Login')
root.geometry("1387x750+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

background1=PhotoImage(file='kolkata_colour.png')
# Label(root,image=background1,bg='white').place(x=0,y=0)


# usersname=GUIsignup.name.get()
# account_no=Database.account_no(usersname)
# username,password=sign_in.generator(account_no)






my_canvas= Canvas(root,width=1387,height=750)
my_canvas.pack(fill='both',expand=True)



my_canvas.create_image(0,0, image=background1,anchor="nw")



# Textual="Username:"+username+"\n"+"Password:"+password+"Account No.:"+account_no

# label=Label(frame,text=Textual,fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
# label.place(x=4,y=300)











root.mainloop()