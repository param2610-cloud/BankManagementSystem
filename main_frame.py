import sign_in
import transaction 

a = input("If you are already registered, press 1: ")
acc_no=""
if a != '1':
    name = input("Enter your full name: ")
    address = input("Enter your full address: ")
    phn_no = int(input("Enter your active phone no.: "))
    email = input("Enter your active email: ")
    D_O_B = input("Enter your Date of Birth in DD/MM/YEAR format: ")
    import registration

    user = registration.registration(name, address, phn_no, email, D_O_B)
    user.confirmation()
    user.save_to_file()
    from Database import account_no
    account=account_no(name)
    user,pass1=sign_in.generator(account)
    print("Here is your username:", user)
    print("And it's your password:", pass1)
    
    acc_no=sign_in.sign()
else:
    
    acc_no=sign_in.sign()


transaction.trans(acc_no)





