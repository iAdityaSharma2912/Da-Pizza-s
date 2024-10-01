'''Project Name: Pizza Resturant Management
Creator Name: Aditya Sharma
owner username-owner
      password-owner@123
'''
import mysql.connector
mysql_passwd="imaditya@123"#Mysql password

def main():
    print("*****************************************************************")
    print("                    WELCOME TO Da Pizza's                        ")
    print("*****************************************************************")
    print("I'm\n")
    print("1. Customer")
    print("2. Owner")
    print("3. Delivery Boy")
    print("4: Exit\n")
    while True:
        try:
            opt=int(input("Choose option: "))
            if opt in [1,2,3,4]:
                break
            print("Give the corret option.")
        except:
            print("Please enter a number.")
    print()
    if opt==1:
        customer()
    elif opt==2:
        login("owner")
    elif opt==3:
        login("delivery man")
    elif opt==4:
        quit()

def customer():
    print("*****************************************************************")
    print("Hello Sir/Madam\n")
    print("1. Give order")
    print("2. Cancel order")
    print("3. Contact us")
    print("4: Back      5: Exit\n")
    while True:
        try:
            opt=int(input("Choose option: "))
            if opt in [1,2,3,4,5]:
                break
            else:
                print("Give the corret option.")
        except:
            print("Enter a number.")
    print()
    if opt==1:
        give_order()
    elif opt==2:
        cancel_order()
    elif opt==3:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
            mycursor=mydb.cursor()
            mycursor.execute("select * from resturant_details")
            myresult=mycursor.fetchall()
            for i in myresult:
                print(i[0],"  ",'\t:',i[1])
            mycursor.close()
            mydb.close()
            press=input('Press enter.')
            customer()
        except Exception as e:
            print(e)
            customer()
    elif opt==4:
        main()
    elif opt==5:
        quit()

def owner():
    print("*****************************************************************")
    print("Welcome Owner")
    print("1. Menu")
    print("2. Employee")
    print("3. Search Order")
    print("4. Change password")
    print("5: Back    6: Exit")
    while True:
        try:
            opt=int(input("Choose option: "))
            if opt in [1,2,3,4,5,6]:
                break
            else:
                print("Give the corret option.")
        except:
            print("Enter a number.")
    print()
    if opt==1:
        menu()
    elif opt==2:
        employee()
    elif opt==3:
        search_order()
    elif opt==4:
        change_passwd("owner","owner")
    elif opt==5:
        main()
    elif opt==6:
        quit()

def login(designation):
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select * from login_details where designation='{}'".format(designation))
        myresult=mycursor.fetchall()
        mycursor.close()
        mydb.close()
        retry='y'
        while retry=='y':
            access=False
            print("Please enter your username and password.\n")
            username_check=input("Username: ")
            password_check=input("Password: ")
            for i in myresult:
                if i[0]==username_check and i[1]==password_check:
                    access=True
            if access==True:
                break
            else:
                print("Incorrect username and password.")
                retry=input('Do you want to retry? (y/n): ')
        else:
            print()
            main()
        if access==True and designation=="owner":
            print()
            owner()
        if access==True and designation=="delivery man":
            print()
            delivery_man(username_check)
    except Exception as e:
        print(e,"\n")
        main()

def menu():
    print("*****************************************************************")
    print('1. Add item in menu')
    print('2. Remove item from menu')
    print('3. Update price of item')
    print('4: Back    5: Exit\n')
    while True:
        try:
            opt=int(input("Choose option: "))
            if opt in [1,2,3,4,5]:
                break
            else:
                print("Give the corret option.")
        except:
            print("Enter a number.")
    print()
    if opt==1:
        add_item()
    elif opt==2:
        remove_item()
    elif opt==3:
        update_price()
    elif opt==4:
        owner()
    elif opt==5:
        quit()

def employee():
    print("*****************************************************************")
    print("1. Add new employee")
    print("2. Remove employee")
    print("3. Update details of employee")
    print("4: Back   5: Exit\n")
    while True:
        try:
            opt=int(input("Choose option: "))
            if opt in [1,2,3,4,5]:
                break
            else:
                print("Give the corret option.")
        except:
            print("Enter a number.")
    print()
    if opt==1:
        add_emp()
    elif opt==2:
        remove_emp()
    elif opt==3:
        update_emp()
    elif opt==4:
        owner()
    elif opt==5:
        quit()

def show_menu():
    #show menu do not need an func to add in except block
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select * from menu")
        myresult=mycursor.fetchall()
        print("\t\t\t=====MENU=====")
        if myresult:
            print("-"*65)
            print("|Item_id|               Name            |  S"+"\t|  "+"  M"+"\t|  "+"  L"+"\t|")
            print("-"*65)
            for a in myresult:
                name=a[1]+" "*(30-len(a[1]))
                print("|  ",a[0],"\t| ",name,"|  ",a[2],"\t|  ",a[3],"\t|  ",a[4],"\t|",sep="")
            print("-"*65)
        else:
            print("There is no item.")
            customer()
        mycursor.close()
        mydb.close()
    except Exception as e:
        print(e)
        mydb.close()

def give_order():
    print("*****************************************************************")
    show_menu()
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select order_id from id")
        myresult=mycursor.fetchone()
        order_id=myresult[0]
        mycursor.execute("update id set order_id={}".format(order_id+1))
        count=amount=0
        add_item="y"
        while add_item=="y":
            item_id=input("Enter item id:")
            size=input("Enter size:")
            mycursor.execute("select name,{} from menu where item_id={}".format(size,item_id))
            myresult=mycursor.fetchone()
            name=myresult[0]
            price=myresult[1]
            qty=int(input("Qty: "))
            count+=qty
            amount+=(price*qty)
            mycursor.execute("insert into order_item values({},'{}','{}',{},{})".format(order_id,name,size,price,qty))
            add_item=input("Do you want to add another item? (y/n): ")
        print("\n====Customer Details====")
        cus_name=input("Enter name: ")
        cus_phone=int(input("Enter Phone no: "))
        cus_address=input("Enter Address: ")
        pincode=input("Enter your pincode: ")
        print("*******************************************************************\n")
        print("No of items:",count,"\tTotal Payable:",amount)
        confirm=input("Do you want to confirm order?(y/n): ")
        if confirm=='y':
            mycursor.execute("insert into order_detail values({},'{}','{}','{}','{}',{},{},'Not Delivered')".format(order_id,cus_name,cus_phone,cus_address,pincode,count,amount))
            print("\nYour order has been placed.\n====Thank you for coming.====\ Your Order ID is : ",order_id)
            mydb.commit()
    except Exception as e:
        print(e)
    finally:
        mycursor.close()
        mydb.close()
        customer()

def cancel_order():
    print("*****************************************************************")
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        order_id=int(input("Enter Order id: "))
        mycursor.execute("select * from order_detail where order_id={}".format(order_id))
        myresult=mycursor.fetchall()
        if myresult:
            mycursor.execute("delete from order_detail where order_id={}".format(order_id))
            mycursor.execute("delete from order_item where order_id={}".format(order_id))
            print("Your order has been canceled.")
        else:
            print("Order has already been removed or there is no order with this id.")
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        customer()

def add_item():
    print("*****************************************************************")
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        while True:
            name=input('Name of item:')
            if len(name)<=30:
                break
            else:
                print("Maximum 30 character.")
        mycursor.execute("select item_id from id")
        myresult=mycursor.fetchone()
        item_id=myresult[0]
        mycursor.execute('update id set item_id={}'.format(item_id+1))
        s=int(input('Price of Small:'))
        m=int(input('Price of Medium:'))
        l=int(input('Price of Large:'))
        sql="insert into menu values({},'{}',{},{},{})".format(item_id,name,s,m,l)
        mycursor.execute(sql)
        mydb.commit()
        print("Item added sccessfully.")
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        menu()

def remove_item():
    print("*****************************************************************")
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        show_menu()
        remove_item_id=input("Item_id:")
        mycursor.execute("select * from menu where Item_id={}".format(remove_item_id))
        myresult=mycursor.fetchall()
        if myresult:
            mycursor.execute("delete from menu where Item_id={}".format(remove_item_id))
            print("The item has been removed now.")
        else:
            print("There is no item with this id.")
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        menu()

def update_price():
    print("*****************************************************************")
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        show_menu()
        update_item_id=input("Item_id:")
        mycursor.execute("select * from menu where Item_id={}".format(update_item_id))
        myresult=mycursor.fetchall()
        if myresult:
            s=int(input('New Price of Small:'))
            m=int(input('New Price of Medium:'))
            l=int(input('New Price of Large:'))
            mycursor.execute("update menu set S={},M={},L={} where Item_id={}".format(s,m,l,update_item_id))
            print("Price of item is updated sccessfully")
        else:
            print("There is no item with this id.")
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        mycursor.close()
        mydb.close()
        print()
        menu()

def add_emp():
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select employee_id from id")
        myresult=mycursor.fetchone()
        employee_id=myresult[0]
        mycursor.execute('update id set employee_id={}'.format(employee_id+1))
        print("=====Details of Employee=====\n")
        first_name=input("First name: ")
        last_name=input("Last name: ")
        gender=(input("Gender: ")).capitalize()
        DOB=input("Date of birth (YYYY-MM-DD): ")
        email=input("Email address: ")
        phone_no=int(input("Phone no: "))
        address=input("Address: ")
        pincode=input("Enter the pincode of the area where he/she will deliver pizza: ")
        username="DLV"+pincode
        mycursor.execute("select password from login_details")
        myresult=mycursor.fetchall()
        flag=True
        while flag:
            password=input("Enter login password: ")
            for i in myresult:
                if i[0]!=password:
                    flag=False
                else:
                    print("Duplicate password")
                    flag=True
                    break
        mycursor.execute("insert into login_details values('{}','{}','delivery man')".format(username,password))
        sql="insert into employee values({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(employee_id,first_name,last_name,gender,DOB,email,phone_no,address,pincode)
        mycursor.execute(sql)
        mydb.commit()
        print("Employee is added sccessfully!!!\n")
        print("Name:",first_name,last_name)
        print("Employee id:",employee_id)
        print("Username:","DLV"+pincode)
        print("Password:",password)
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        employee()

def remove_emp():
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        emp_id=int(input("Enter employee id:"))
        mycursor.execute("select * from employee where employee_id={}".format(emp_id))
        myresult=mycursor.fetchone()
        if myresult==None:
            print("There is no employee with this id.")
        else:
            mycursor.execute("delete from employee where employee_id={}".format(emp_id))
            print("Employee details has been removed.")
            mydb.commit()
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        employee()

def update_emp():
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        emp_id=int(input("Enter employee id:"))
        print("Which detail you want to update:")
        print("1. Email   2. Phone no   3. Address")
        print('4: Back    5: Exit\n')
        while True:
            opt=eval(input("Choose option: "))
            if opt in [1,2,3,4,5]:
                print()
                break
            else:
                print("Give the corret option.")
        if opt==1:
            new_email=input("Enter new email:")
            sql="update employee set email='{}' where employee_id={}".format(new_email,emp_id)
        elif opt==2:
            new_phone=input("Enter new phone no:")
            sql="update employee set phone_no='{}' where employee_id={}".format(new_phone,emp_id)
        elif opt==3:
            new_address=input("Enter new address:")
            sql="update employee set address='{}' where employee_id={}".format(new_address,emp_id)
        elif opt==4:
            employee()
        elif opt==5:
            quit()
        mycursor.execute(sql)
        print("Employee details has been updated.")
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        mycursor.close()
        mydb.close()
        employee()

def change_passwd(username,designaton):
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select Password from login_details")
        myresult=mycursor.fetchall()
        flag=True
        while flag:
            new_passwd=input("Enter new password:")
            for i in myresult:
                if i[0]==new_passwd:
                    print("Duplicate password")
                    break
            else:
                flag=False
        mycursor.execute("update login_details set password='{}' where username='{}'".format(new_passwd,username))
        print("Password changed successfully.")
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        mycursor.close()
        mydb.close()
        if designaton=='delivery man':
            delivery_man(username)
        else:
            owner()

def delivery_man(username):
    print("*****************************************************************")
    try:
        pincode=username[3:]
        print("1. View order")
        print("2. Mark Delivered")
        print("3. Change Password")
        print("4: Back    5: Exit\n")
        while True:
            try:
                opt=int(input("Choose option: "))
                if opt in [1,2,3,4,5]:
                    print()
                    break
                else:
                    print("Give the corret option.")
            except:
                print("Enter a number.")
        if opt==1:
            print()
            view_order(pincode)
        elif opt==2:
            print()
            mark_delivered(pincode)
        elif opt==3:
            print()
            change_passwd(username,"delivery man")
        elif opt==4:
            print()
            main()
        elif opt==5:
            quit()
    except Exception as e:
        print(e)
        delivery_man(username)

def view_order(pincode):
    print("*****************************************************************")
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select order_id from order_detail where pincode='{}' and status='Not Delivered'".format(pincode))
        myresult=mycursor.fetchall()
        for i in myresult:
            print("->",i[0])
        if myresult:
            order_id=int(input("Enter order id whose details you want to get:"))
            p=['order id', 'customer name', 'customer phone no', 'customer address', 'no of items','amount']
            mycursor.execute("select order_id, customer_name, customer_phone_no, customer_address, count_items, amount from order_detail where order_id={}".format(order_id))
            myresult=mycursor.fetchone()
            print("\n=====Order Details=====")
            for j in range(6):
                    print(p[j],":",myresult[j])
        else:
            print("You have no order for delivering.\n")
        press=input("Press enter to go back.")
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        delivery_man("DLV"+pincode)

def mark_delivered(pincode):
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("select order_id from order_detail where pincode='{}' and status='Not Delivered'".format(pincode))
        myresult=mycursor.fetchall()
        if myresult:
            order_id=int(input("Enter order id: "))
            mycursor.execute("update order_detail set status='Delivered' where order_id={}".format(order_id))
        else:
            print("You have no order for delivering.")
        mydb.commit()
    except:
        print("Something went wrong!!!")
    finally:
        mycursor.close()
        mydb.close()
        delivery_man("DLV"+pincode)

def search_order():
    try:
        print("*****************************************************************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=mysql_passwd,database='resturant')
        mycursor=mydb.cursor()
        mycursor.execute("desc order_detail")
        myresult=mycursor.fetchall()
        srch_order_id=int(input("Enter order id to search:"))
        mycursor.execute("select * from order_detail where order_id={}".format(srch_order_id))
        myresult1=mycursor.fetchone()
        no=0
        print("\n=====Order Details=====")
        for i in myresult:
            print(i[0],":",myresult1[no])
            no+=1
        press=input("Press enter to go back.")
    except Exception as e:
        print(e)
    finally:
        print()
        mycursor.close()
        mydb.close()
        owner()

main()
