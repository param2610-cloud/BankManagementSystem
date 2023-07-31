import KYC
import pymysql
from datetime import datetime
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='#S^9k6B0%N7',
    database='user_details',
    autocommit=True

)
mycursor=connection.cursor()
import random
class registration:
    def __init__(self,name,address,phn_no,email,D_O_B):
        self.name=name
        self.address=address
        self.phn_no=phn_no
        self.email=email
        self.d_o_b=D_O_B
        
    def confirmation(self):
      pass
    def save_to_file(self):
      
        


        date_of_birth_str = self.d_o_b
        date_of_birth = datetime.strptime(date_of_birth_str, '%d/%m/%Y').date()



        account_no=random.randint(10**10, (10**11)-1)
        sql="INSERT INTO users(account_number,name,address,phn_no,email,date_of_birth) VALUES(%s,%s,%s,%s,%s,%s)"
        val=(account_no,self.name,self.address,self.phn_no,self.email,date_of_birth)
        mycursor.execute(sql,val)
        
        




