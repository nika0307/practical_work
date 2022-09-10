import sqlite3

connection=sqlite3.connect('sqlite.db')
c=connection.cursor()

def add_user(id, name, surname, patronym, age, address, phone, email):
    c.execute("insert into usern (id, name, surname, patronym, age, address, phone, email)
    values('%s','%s','%s','%s','%s','%s','%s','%s'")%((id, name, surname, patronym, age, address, phone, email))
    connection.comit()

def view_users():
        print("Users list:\n")
        c.execute("SELECT*FROM user")
        row=c.fetchone()
        while row is not None:
            print("id: "+str(row[0])+"name: "+str(row[1])+"surname: "+str(row[2])+"patronym: "+str(row[3])+"age: "+str(row[4])+"address: "+str(row[5])+"phone: "+str(row[6])+"email: "+str(row[7]))
            row=c.fetchone()
        c.close()
        connection.close()

id=input("Your id: ")
name=input("Your name: ")
surname=input("Your surname: ")
patronym=input("Your patronym: ")
age=input("Your age: ")
address=input("Your adress: ")
phone=input("Your phone: ")
email=input("Your email adress: ")

add_user(id, name, surname, patronym, age, address, phone, email address)
