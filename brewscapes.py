import mysql.connector as mc
import colorama
import os
import sys
from colorama import Fore

colorama.init(autoreset=True)

con= mc.connect(host ="sql12.freesqldatabase.com", user= "sql12656598", password= "ZhJ229DI5k", database="sql12656598")
cur= con.cursor()
cur.execute("Select * from menu;")
items = cur.fetchall()


def logo():
     os.system("cls")
     print(Fore.LIGHTCYAN_EX + ''' 
  ____                                                  
 | __ ) _ __ _____      _____  ___ __ _ _ __   ___  ___ 
 |  _ \| '__/ _ \ \ /\ / / __|/ __/ _` | '_ \ / _ \/ __|
 | |_) | | |  __/\ V  V /\__ \ (_| (_| | |_) |  __/\__ |
 |____/|_|  \___| \_/\_/ |___/\___\__,_| .__/ \___||___/
                                       |_|              
    
  Developed By: Nuha and Mudit- Class XII-B

''')
     
def options():
    print(Fore.RED + "Select an option: ")
    print()
    print(Fore.LIGHTMAGENTA_EX + '''(1) View Menu
(2) Take new order
(3) View orders
(4) Delete order
(5) Add new item to menu
(6) Delete item from menu
(7) Change Prices
(8) Search for an item
(9) Exit 
           ''')
    try:
        x = int(input("Enter option: "))
        if(x>9 or x<1):
            print(Fore.RED + "Enter a valid option! ")
            x = 10
    except:
        print(Fore.RED + "Enter a valid option! ")
        x = 10
    return x 

def menu():
    logo()
    cur.execute("Select * from menu order by SNo;")
    data = cur.fetchall()
    for row in data:
        s = str(row[0])
        i = row[1]
        p = str(row[2])
        t = row[3]
        print(Fore.LIGHTMAGENTA_EX + s + ". " + i + " - " + t  + ": " + "Rs." + p)
    print()
    x = input("Press enter to go back")

def order():
    total = 0
    while True:
        logo()
        on = int(input("Enter Order Number: "))
        i = input("Enter item name: ")
        q = int(input("Enter qty: "))
        query= "Insert into orders(Orderno, Item, Qty) values(%s, %s, %s)"
        value = (on, i, q) 
        try:
            cur.execute(query, value)
            con.commit()
        except:
            print(Fore.RED + "Error Occured! ")
            continue
        for j in items:
            if (j[1] == i):
                price = j[2]
        total = total + (price*q)
        x = input("Would u like to add another item? (y/n): ")
        if(x == "n"):
            break
    print(Fore.GREEN + "Order Successfully Placed! ")
    print()
    print(Fore.RED + "Your total amount is: ", total)
    x = input("Press enter to go back ")

def view():
    logo()
    cur.execute("Select * from orders;")
    data = cur.fetchall()
    for row in data:
        on = str(row[0])
        i = row[1]
        q = str(row[2])
        print(Fore.LIGHTMAGENTA_EX + on + ": " + i + " - " + q)
    x = input("Press enter to go back")

def delorder():
    logo()
    x = int(input("Enter order number to delete: "))
    q = "Delete from orders where Orderno = %s;"
    v = (x,)
    try:
        cur.execute(q, v)
        con.commit()
        print(Fore.GREEN + "Successfully Deleted! ")
    except:
        print(Fore.RED + "Order not found! ")
    a = input("Press enter to go back ")

def add():
    logo()
    s = int(input("Enter Serial No: "))
    i = input("Enter Item Name: ")
    p = int(input("Enter Price: "))
    t = input("Enter Category: ")
    q = "Insert into menu(SNo, Item, Price,Type) values(%s, %s, %s, %s);"
    v = (s, i, p, t)
    try:
        cur.execute(q, v)
        con.commit()
        print(Fore.GREEN + "Item successfully added! ")
    except:
        print(Fore.RED + "Erroe Occured! ")
    x = input("Press enter to go back ")

def delete():
    logo()
    i = input("Enter item to delete: ")
    q = "delete from menu where Item= %s;"
    v = (i,)
    try:
        cur.execute(q, v)
        con.commit()
        print(Fore.GREEN + "Item successfully deleted! ")
    except:
        print(Fore.RED + "Error Occured! ")
    x = input("Press enter to go back ")

def change():
    logo()
    i = input("Enter item name whose price is to be changed: ")
    p = int(input("Enter new price: "))
    q = "Update menu set Price = %s where Item = %s;"
    v = (p, i)
    try:
        cur.execute(q,v)
        con.commit()
        print(Fore.GREEN + "Successfully updated price! ")
    except:
        print(Fore.RED + "Error Occured! ")
    x = input("Press enter to go back ")

def search():
    logo()
    i = input("Enter item to search: ")
    q = "Select * from menu where Item = %s"
    v = (i,)
    try:
        cur.execute(q,v)
        data = cur.fetchall()
        for j in data:
            print(Fore.LIGHTMAGENTA_EX + j[1] + " - " + j[3] + ": Rs." + str(j[2]) )
    except:
        print(Fore.RED + "Error Occured! ")
    x = input("Press enter to go back ")
        
while True:
    logo()
    o = options()
    if (o == 1):
        menu()
    elif(o == 2):
        order()
    elif(o == 3):
        view()
    elif(o == 4):
        delorder()
    elif(o == 5):
        add()
    elif(o == 6):
        delete()
    elif(o == 7):
        change()
    elif(o == 8):
        search()
    elif(o == 9):
        print(Fore.CYAN + "Thank you for using our program <3")
        con.close()
        sys.exit()
    elif(o == 10):
        continue


