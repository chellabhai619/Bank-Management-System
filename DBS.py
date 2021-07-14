import mysql.connector as mysql
id=(input("Enter id: "))
name=input("Enter Name: ")
phone=input("Enter Ph.no: ")
con=mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="example"
)
cursor=con.cursor()
cursor.execute("insert into student values('"+ id +"','"+ name +"','"+ phone +"')")
cursor.execute("commit")
print("Executed")
con.close()

print(con)