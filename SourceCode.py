import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os	
def clrscreen():
    print('\n' *5)

def ShowIssuedBooks():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='Sanket@1704',host='localhost' , database='Library')
        Cursor = cnx.cursor()
        query = ("SELECT B.Bookno,Book_Name,M.Memberno,Member_Name,Date_of_issue,Date_of_return FROM bookrecord B,issue I ,member M where B.bookno=I.bookno and I.memberno=M.memberno")
        Cursor.execute(query)
        for (Bookno,Book_name,Memberno,Member_name,date_of_issue,date_of_return) in Cursor:
            print("==============================================================")
            print("Book Code : ",Bookno)
            print("Book Name : ",Bookname)
            print("Member Code : ",Memberno)
            print("Member Name : ",Membername)
            print("Date of issue : ",date_of_issue)
            print("Date of return : ",date_of_return)
            print("===============================================================")
            Cursor.close()
            cnx.close()
            print("You have done it!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
         cnx.close()
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


import Book
import MenuLib
import issue


def clrscreen():
    print('\n' *5)


def display():
    try:
        cnx = connection.MySQLConnection(user='root', password='Sanket@1704',  host='localhost',database='Library')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM member")
        Cursor.execute(query)
        for (Memberno,Member_name,Mobile,Date_of_membership,Address) in Cursor:
            print("==============================================================")
            print("Member Code : ",Memberno)
            print("Member Name : ",Member_name)
            print("Mobile No.of Member : ",Mobile)
            print("Date of Membership : ",Date_of_Membership)
            print("Address : ",Address)
            print("===============================================================")
        Cursor.close()
        cnx.close()
        print("You have done it!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:  
            print(err)
    else:
        cnx.close()

def insertMember():
    try:
        cnx = connection.MySQLConnection(user='root' , password='Sanket@1704' , host='localhost',database='Library')
        Cursor = cnx.cursor()
        memberno=input("Enter Member Code : ")
        member_name=input("Enter Member Name : ")
        mobile=input("Enter Member Mobile No. : ")
        print("Enter Date of Membership (Date/Month and Year separately: ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        address=input("Enter Member Address : ")
        Qry = ("INSERT INTO Member  VALUES (%s, %s, %s, %s, %s)")
        data = (memberno,member_name,mobile,date(YY,MM,DD),address)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted..............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()

        
def deleteMember():
    try:
        cnx = connection.MySQLConnection(user='root' , password='Sanket@1704', host='localhost', database='Library')
        Cursor = cnx.cursor()
        memberno=input("Enter Member Code to be deleted from the Library : ")
        Qry =("""DELETE FROM Member WHERE MemberNO = %s""")
        del_rec=(memberno,)
        Cursor.execute(Qry,del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def SearchMember():
    try:
        cnx = connection.MySQLConnection(user='root',password='Sanket@1704', host='localhost', database='Library')
        Cursor = cnx.cursor()
        membername=input("Enter Member Name to be Searched from the Library : ")
        query = ("SELECT * FROM Member where Member_name = %s ;")
        rec_srch=(member_name,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (Memberno,Member_name,MOBile,Date_of_membership,Address) in Cursor:
            Rec_count+=1
            print("==============================================================")
            print("Member Code : ",Memberno)
            print("Member Name : ",Member_name)
            print("Mobile No.of Member : ",MOBile)
            print("Date of Membership : ",Date_of_membership)
            print("Address : ",Address)
            print("===============================================================")
            if Rec_count%2==0:
                 input("Press any key to continue")
                 clrscreen()
            print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
             print("Database does not exist")
        else:
             print(err)
        cnx.close()
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform


def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))



def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='Sanket@1704',host='localhost', database='Library')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM BookRecord")
        Cursor.execute(query)
        for (bookno , Bookname , Author , price , publisher , quantity , date_of_purchase) in Cursor:
            print("==============================================================")
            print("Book Code : ",bookno)
            print("Book Name : ",Bookname)
            print("Author of Book : ",Author)
            print("Price of Book : ",price)
            print("Publisher : ",publisher)
            print("Total Quantity in Hand : ",quantity)
            print("Purchased On : ",date_of_purchase)
            print("===============================================================")
        Cursor.close()
        cnx.close()
        print("You Have done it !!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


        
def insertData():
    try:
        cnx = connection.MySQLConnection(user='root',password='Sanket@1704', host='localhost',database='Library')
        Cursor = cnx.cursor()
        bookno=input("Enter Book Code : ")
        bookname=input("Enter Book Name : ")
        Author=input("Enter Book Author's Name : ")
        price=int(input("Enter Book Price : "))
        publisher=input("Enter Publisher of Book : ")
        quantity=int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/Month and Year seperately: ")
        DD=int(input("Enter Date : "))   
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        Qry = ("INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (bookno,bookname,Author,price,publisher,quantity,date(YY,MM,DD))
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted . . . . . . . . . . . . . .")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
def deleteBook():
    try:
        cnx = connection.MySQLConnection(user='root',password='Sanket@1704', host='localhost', database='Library')

        Cursor = cnx.cursor()
        bookno=input("Enter Book Code of Book to be deleted from the Library : ")
        Qry =("""DELETE FROM BookRecord WHERE BookNO = %s""")
        del_rec=(bno,)
        Cursor.execute(Qry,del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfully. . . . . . . . . . . . .")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()

def SearchBookRec():
    try:
        cnx = connection.MySQLConnection(user='root', password='Sanket@1704',  host='localhost', database='Library')
        Cursor = cnx.cursor()
        bookno=input("Enter Book No to be Searched from the Library : ")
        query = ("SELECT * FROM BookRecord where BookNo = %s ;")
        rec_srch=(bno,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (Bookno,Bookname,Author,price,publisher,quantity,date_of_purchase) in Cursor:
            Rec_count+=1
            print("==============================================================")
            print("Book Code : ",Bookno)
            print("Book Name : ",Bookname)
            print("Author of Book : ",Author)
            print("Price of Book : ",price)
            print("Publisher : ",publisher)
            print("Total Quantity in Hand : ",quantity)
            print("Purchased On : ",date_of_purchase)
            print("===============================================================")
            if Rec_count%2==0:
                input("Press any key to continue")
                clrscreen()
            print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()

def UpdateBook():
    try:
        cnx = connection.MySQLConnection(user='root',password='Sanket@1704', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bookno=input("Enter Book Code of Book to be Updated from the Library : ")
        query = ("SELECT * FROM BookRecord where BookNo = %s ")
        rec_srch=(bookno,)
        print("Enter new data ")
        bookkname=input("Enter Book Name : ")
        Author=input("Enter Book Author's Name : ")
        price=int(input("Enter Book Price : "))
        publisher=input("Enter Publisher of Book : ")
        quantity=int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/Month and Year seperately: ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        Qry = ("UPDATE BookRecord SET bookname=%s,Author=%s,\
                    price=%s,publisher=%s,quantity=%s,date_of_purchase=%s WHERE BookNO=%s")
        
        data = (bookname,Author,price,publisher,quantity,date(YY,MM,DD),bookno)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Updated Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
        UpdateBook()
import MenuLib
import Book
import issue
while True:
    Book.clrscreen()
    print("\t\t\t Library Management\n")
    print("==============================================================")
    print("\t1. Book Management ")
    print("\t2. Members Management")
    print("\t3. Issue/Return Book ")
    print("\t4.  Exit ")
    print("===============================================================")
    choice=int(input("Enter Choice between 1 to 4-------> : "))
    if choice==1:
        MenuLib.MenuBook()
    elif choice==2:
        MenuLib.MenuMember()
    elif choice==3:
        MenuLib.MenuIssueReturn()
    elif choice==4:
        break
    else:
        print("Wrong Choice. . . . . .Enter Your Choice again")
        x=input("Enter any key to continue")
