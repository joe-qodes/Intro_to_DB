import mysql.connector


my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Joequao241204???&"
)


try:
    cursor = my_db.cursor()
    create_db = cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    cursor.close()
    my_db.close()
except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)



# my_db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Joequao241204???&",
#     database = "my_db"
# )
