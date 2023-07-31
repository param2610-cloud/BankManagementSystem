import pymysql
connection=pymysql.connect(host='localhost',user='root',password='#S^9k6B0%N7',database='user_details',autocommit=True)
mycursor=connection.cursor()

def sign(username,password):
    
    user_input=username

    pass_input=password
    query = "SELECT account_number FROM users WHERE user_id = %s AND password = %s"
    cursor = connection.cursor()
    cursor.execute(query, (user_input, pass_input))
    result = cursor.fetchone()
    if result:
        return result
    else:
        print("Wrong username or password.")
        return 
    



def generator(account_number):
    import random
    query = "SELECT phn_no, name FROM users WHERE account_number = %s"
    values = (account_number)
    mycursor.execute(query, values)


    result = mycursor.fetchone()


    
    phn_no, name = result
    phn_no=str(phn_no)
    username=name[:4]+phn_no[:2]
    password=''.join(random.sample("1234567890",int(4)))  
    sql="UPDATE users SET user_id = %s, password = %s WHERE account_number = %s"
    val=(username,password,account_number)
    mycursor.execute(sql,val)
    
    return username,password








         

    