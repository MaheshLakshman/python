import mysql.connector

connectDb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'test_python_db'
)

dbcursor = connectDb.cursor()

#dbcursor.execute('CREATE DATABASE test_python_db')

#dbcursor.execute('SHOW DATABASES')
# dbcursor.execute('SHOW TABLES')

# for x in dbcursor:
#     print(x)

#dbcursor.execute('CREATE TABLE customers (name VARCHAR(255), email VARCHAR(255), address TEXT)')

#dbcursor.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

sql = 'INSERT INTO customers (name, email, address) VALUES (%s, %s, %s)'

val = ('mah', 'test@gmail.com', 'test address')

dbcursor.execute(sql, val)

connectDb.commit()

print('Done', 'row count : ', dbcursor.rowcount, 'last insert id : ', dbcursor.lastrowid)






