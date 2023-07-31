import sign_in
import KYC
import pymysql
# connection=pymysql.connect(host='localhost',user='root',password='#S^9k6B0%N7',database='user_details',autocommit=True)
connection=pymysql.connect(host='localhost',user='root',password="#S^9k6B0%N7",database="user_details",autocommit=True)
mycursor=connection.cursor()

def trans(account_numbers,choice,amount,sendacc):
    
  
        
        if choice == "1":
           
           credit=amount
           
        
           from datetime import datetime
           transaction_date_time = datetime.now()

           account_num=account_numbers

           sq="INSERT INTO transactions(account_number,transaction_date_time,transaction_type,amount) VALUES(%s,%s,%s,%s)"
           val=(account_num,transaction_date_time,'Credit',credit)
           mycursor.execute(sq,val)
           sq = "UPDATE transactions SET balance = balance + %s WHERE account_number = %s"
           val = (credit, account_numbers)
           mycursor.execute(sq, val)
           
           return
        elif choice == "2":
           
           debit=amount
           
        
           from datetime import datetime
           transaction_date_time = datetime.now()

           

           sq="INSERT INTO transactions(account_number,transaction_date_time,transaction_type,amount) VALUES(%s,%s,%s,%s)"
           val=(account_numbers,transaction_date_time,'Debit',debit)
           mycursor.execute(sq,val)
           sq = "UPDATE transactions SET balance = balance - %s WHERE account_number = %s"
           val = (debit, account_numbers)
           mycursor.execute(sq, val)
           

            
           return
        elif choice == "3":
            
            senderaccno=sendacc
            
            sq="UPDATE transactions SET balance = balance + %s WHERE account_number=%s"
            val=(amount,senderaccno)
            mycursor.execute(sq,val)
            from datetime import datetime
            transaction_date_time=datetime.now()
            sq="INSERT INTO transactions(account_number,transaction_date_time,transaction_type,amount) VALUES(%s,%s,%s,%s)"
            val=(account_numbers,transaction_date_time,"Credit",amount)
            mycursor.execute(sq,val)
            sq="INSERT INTO transactions(account_number,transaction_date_time,transaction_type,amount) VALUES(%s,%s,%s,%s)"
            val=(senderaccno,transaction_date_time,"Credit",amount)
            mycursor.execute(sq,val)

            sq="UPDATE transactions SET balance = balance - %s WHERE account_number=%s"
            val=(amount,account_numbers)
            mycursor.execute(sq,val)
            
            
            return
        elif choice == "4":
            sq="SELECT balance FROM transactions WHERE account_number=%s"
            mycursor.execute(sq,(account_numbers))
            strbalance=mycursor.fetchall()
            balance0=convertTuple(strbalance)
            balance=balance0.split("\n")
            print("Your ACCOUNT NUMBER= ",account_numbers)
            print("Your reamining balance=",balance[0])
            pass
        elif choice == "5":
            transaction_details(account_numbers)
            pass
        elif choice == "0":
            print("Thank you for using the Bank Management System. Goodbye!")
            
        else:
            print("Invalid choice. Please try again.")









def deposit():
    print("Your Account No.=",sign_in.Acc_no)
    print("Type the amount to be deposit:")
    credit=input()
    
    
    return credit



def withdraw():
    print("Your Account No.=",sign_in.Acc_no)
    print("what amount you want to withdraw:")
    debit=input()
    return debit 

def transaction_details(account_numbers):
    sq = "SELECT transaction_date_time FROM transactions WHERE account_number=%s"
    mycursor.execute(sq, (account_numbers,))
    timedate = mycursor.fetchall()
    strtimedate = convertTuple(timedate)
    
    date_time = strtimedate.split("\n")
    

    sq = "SELECT transaction_type from transactions WHERE account_number=%s"
    mycursor.execute(sq, (account_numbers,))
    typo = mycursor.fetchall()

    sq = "SELECT amount from transactions WHERE account_number=%s"
    mycursor.execute(sq, (account_numbers,))
    amount = mycursor.fetchall()

    print("    Date     Time                          (credit:debit)   Amount")
    for i in range(len(timedate)):
        print(date_time[i], "                         ",typo[i][0],"      ", amount[i][0])

    return


def convertTuple(lst):
    result = ''
    for tup in lst:
        for item in tup:
            result =result+ str(item)+"\n"
    return result

def getyouknow(table,inputval,input1,output1,output2,output3,output4,output5,output6,output7):
    if output2 == "0" and output3=="0"and output4=="0"and output5=="0"and output6=="0"and output7=="0":

        sq = "SELECT {} FROM {} WHERE {} = %s".format(output1, table, input1)
        value = (inputval,)
        mycursor.execute(sq, value)
        result = mycursor.fetchone()

        if result is not None:
            return str(result[0])
        else:
            return None

    elif output3 == "0" and output4 == "0" and output5 == "0" and output6 == "0" and output7 == "0":
        sq = "SELECT {}, {} FROM {} WHERE {} = %s".format(output1, output2, table, input1)
        value = (inputval,)
        mycursor.execute(sq, value)
        result = mycursor.fetchone()
    
        if result is not None:
            result1, result2 = str(result[0]), str(result[1])
            return result1, result2
        else:
            return None, None
        
    elif output4=="0"and output5=="0"and output6=="0"and output7=="0":
        sq="SELECT "+output1+","+output2+","+output3+" FROM "+table+" WHERE "+input1+" = %s "
        value=(inputval)
        mycursor.execute(sq,value)
        result=mycursor.fetchone()
        result1,result2,result3=result
        return result1,result2,result3
    elif output5=="0"and output6=="0"and output7=="0":
        sq="SELECT "+output1+","+output2+","+output3+","+output4+" FROM "+table+" WHERE "+input1+" = %s "
        value=(inputval)
        mycursor.execute(sq,value)
        result=mycursor.fetchone()
        result1,result2,result3,result4=result
        return result1,result2,result3,result4
    elif output6=="0"and output7=="0":
        sq="SELECT "+output1+","+output2+","+output3+","+output4+","+output5+" FROM "+table+" WHERE "+input1+" = %s "
        value=(inputval)
        mycursor.execute(sq,value)
        result=mycursor.fetchone()
        result1,result2,result3,result4,result5=result
        return result1,result2,result3,result4,result5
    elif output7=="0":
        sq="SELECT "+output1+","+output2+","+output3+","+output4+","+output5+","+output6+" FROM "+table+" WHERE "+input1+" = %s "
        value=(inputval)
        mycursor.execute(sq,value)
        result=mycursor.fetchone()
        result1,result2,result3,result4,result5,result6=result
        return result1,result2,result3,result4,result5,result6
    else:
        sq="SELECT "+output1+","+output2+","+output3+","+output4+","+output5+","+output6+","+output7+" FROM "+table+" WHERE "+input1+" = %s "
        value=(inputval)
        mycursor.execute(sq,value)
        result=mycursor.fetchone()
        result1,result2,result3,result4,result5,result6,result7=result
        return result1,result2,result3,result4,result5,result6,result7
    

import tkinter as tk
from tkinter import ttk
from tkinter import *
def transaction_details(account_numbers):
    sq = "SELECT transaction_date_time FROM transactions WHERE account_number=%s"
    mycursor.execute(sq, (account_numbers,))
    timedate = mycursor.fetchall()
    strtimedate = convertTuple(timedate)

    date_time = strtimedate.split("\n")

    sq = "SELECT transaction_type from transactions WHERE account_number=%s"
    mycursor.execute(sq, (account_numbers,))
    typo = mycursor.fetchall()

    sq = "SELECT amount from transactions WHERE account_number=%s"
    mycursor.execute(sq, (account_numbers,))
    amount = mycursor.fetchall()

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Transaction Details")

    # Create a Treeview widget to display the transaction details
    tree = ttk.Treeview(window)

    # Define columns
    tree["columns"] = ("date", "time", "type", "amount")

    # Format column headers
    tree.heading("date", text="Date")
    tree.heading("time", text="Time")
    tree.heading("type", text="Transaction Type")
    tree.heading("amount", text="Amount")

    # Insert data into the Treeview
    for i in range(len(timedate)):
        tree.insert("", "end", values=(date_time[i], typo[i][0], amount[i][0]))

    # Add Treeview to the window
    tree.pack()

    # Run the Tkinter event loop
    window.mainloop()

# Call the function with an account number

