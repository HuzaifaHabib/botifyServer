import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='db2'
    )

cur=mydb.cursor()


s="create table order_test2( customer_id INT NOT NULL ,order_id INT NOT NULL AUTO_INCREMENT,item_name VARCHAR(100) NOT NULL, Price INT NOT NULL, PRIMARY KEY ( order_id ))"

cur.execute(s)

# mydb=mysql.connector.connect(
# host='localhost',
# user='root',
# password='12345',
# database='db2'   )

# cur=mydb.cursor()
# s="insert into order_test2 (customer_id,order_id,item_name,Price) values (%s,%s,%s,%s)"
# userID = 1
# orderID= 10
# item = "Pizza"
# price = 1000

# o= (userID,orderID,item,price)

# cur.execute(s,o)
# mydb.commit()