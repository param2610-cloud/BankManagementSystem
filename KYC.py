import sign_in
import datetime
# import transaction
def kyc():
    print("what [TYPE] of account it is:\n     Savings=======1\n     Current=======2\n     fixed deposit=======3")
    a=input("Enter=") 
    if a==1: acctype="Savings" 
    elif a==2: acctype="Current" 
    elif a==3: acctype="Fixed Deposit"
    print("It is ",acctype,"account.")
    print("Name: ",sign_in.Name)
    print("Address: ",sign_in.Address)
    print("Your phone no.: ",sign_in.Phone_number)
    print("Email: ",sign_in.Email)
    print("Date Of Birth: ",sign_in.Date_of_Birth)
    print("Acc No.=",sign_in.Acc_no)
import random
def password_manager():
        
        digit1="1234567890"
        
        
        password2=''.join(random.sample(digit1,int(11)))
        return password2

def credential( credit,deposit):
      
      y,mo,d,h,mi,s=timedate()
      
      Balance=Balance+int(credit)-int(deposit)
      print("Your current balance is:",Balance)
      print("                           Transaction History                       ")
      print("    Date                       Time               Amount(credit:debit)           Acc no.             Balance")
      print(d,'/',mo,'/',y,"             ",h,':',mi,':',s,"                ",credit,':',deposit,'             ',sign_in.Acc_no,"           ",Balance)
      
      return y,mo,d,h,mi,s,Balance

