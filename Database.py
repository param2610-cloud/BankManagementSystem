import pymysql
connection=pymysql.connect(host='localhost',user='root',password="#S^9k6B0%N7",database="user_details",autocommit=True)
mycursor=connection.cursor()
# import requests
# url = 'http://localhost/phpmyadmin/index.php'  # Replace with the correct URL of your PHPMyAdmin installation
# username = 'myrule'  # Replace with your PHPMyAdmin username
# password = 'gpampa123param_'  # Replace with your PHPMyAdmin password
cursor=connection.cursor()
def create_database():
    cursor=connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS user_details")
    cursor.close()
def create_tables():
    cursor=connection.cursor()
    cursor.execute("USE user_details")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
  account_number BIGINT UNSIGNED PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(100),
  phn_no BIGINT,
  email VARCHAR(100),
  date_of_birth DATE
)

           """)
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS transactions (
     transaction_id INT PRIMARY KEY AUTO_INCREMENT,
     account_number BIGINT UNSIGNED ,
     transaction_date_time DATETIME,
     transaction_type ENUM('Credit','Debit'),
     amount DECIMAL(10,2),
     balance DECIMAL(10,2),
     FOREIGN KEY (account_number) REFERENCES users(account_number)
     )
     """)
    
    cursor.close()
# import pymysql
# connection=pymysql.connect(host='localhost',user='root',password='#S^9k6B0%N7',database='user_details',autocommit=True)
# cursor=connection.cursor()

def account_no(name12):
    with connection:
        with connection.cursor() as cursor:
            sql = 'SELECT account_number FROM users WHERE name='+"'"+name12+"'"
            cursor.execute(sql)
            account_numbers = cursor.fetchall()
            ACCNO = ''
            for account_number in account_numbers:
                ACCNO = account_number[0]

            return ACCNO

# create_database()
# create_tables()