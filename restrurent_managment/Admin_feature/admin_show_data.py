import os
import sys
# Ignore this append path because inside of folder data
#sys.path.append("")
from admin_sys.admin_system import *
#---------admin_dispaly_Entry-----------------
lst=[]
lst.append(" (1) Add New Items Enter : ")
lst.append(" (2) View Items Enter    : ")
lst.append(" (3) Delete Items Enter  : ")
lst.append(" (4) Add Employees Enter : ")
lst.append(" (5) Exit Enter          :")

#----------admin_display_fun------------------
def admin_display_menu():
    for view_menu_lst in lst:
        print(view_menu_lst)

#----------------------- User Given Data Checking ----------------------------------

#checking_input_comment
def Cheking_User_data(x):
    if  x.isalpha():
        print(f"This {x} is alpha Character Place given integer Number !")
        return False
    elif x.isdigit():
        x = int(x)
        if not((x>=1 and x<=5)):
            print(f"Place Sir given This Number (1 to 5) are inclusive")
            return False
        else:
            return True
    else:
        print(f"This {x} is Numeric number Place given integer Number !")
        return False
    
#Checking_inside_input_comment
def inside_checking():
     
     print("If you again item  add  Press (1) :")
     print("Otherwise you exit then Press (0) :")
     again_input = input()
     if(again_input=="1"):
         return True
     else:
         return False

#Checking_Valid_Emp_Information
#Checking_Valid_Email
import re
def is_valid_mail(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

#Checking_Valid_Name
def is_valid_name(user_emp_name):

    username_pattern = r'^[a-zA-Z][a-zA-Z_]{2,30}$'
    return re.match(username_pattern, user_emp_name) is not None
       





def emp_data_check(user_emp_name:str,user_emp_mail:str,user_emp_Number:str):
    invalid_list=[]
    if not (is_valid_mail(user_emp_email)):
        invalid_mail = f"This Mail {user_emp_email} is invalid"
        invalid_list.append(invalid_mail)
    if not (is_valid_name(user_emp_name)):
         invalid_name = f"This Name {user_emp_name} is Invalid"
         invalid_extra = f"Name Must be Only 30 Character"
         invalid_list.append(invalid_name)
         invalid_list.append(invalid_extra)
    

   


                      


    
#-------------------------Admin Display Data given---------------------

while True:
    print()
    admin_display_menu()
    x = input()
    if(Cheking_User_data(x)):
        x = int(x)
        if(x==1):
            # ---------Admin add New Items-----------
            while True:

                print("Enter Item Name     :")
                item_name = str(input())
                item_name = item_name.strip()
                item_name =" ".join(item_name.split())
                print("Enter Item_quantity : ")
                item_qun = int(input()) 
                print("Enter Per_kg Price  :")
                price_kg = int(input()) 

                itemAdd_checking = admin_manage.add_new_item(None,item_name,item_qun,price_kg)
                if(itemAdd_checking):
                    break
                else:
                    
                    again_check = inside_checking()
                    if(again_check):
                        continue
                    else:
                        break

        elif(x==2):
            #----------Admin_View_items--------------------
            admin_manage.view_item(None)
            
        elif(x==3):

            #----------Admin_Delete_items--------------------
            while True:
                 print("Delete Item Name : ")
                 delete_item_name= str(input())

                 itemDel_checking = admin_manage.delete_item(None,delete_item_name)
                 if(itemDel_checking):
                    break
                 else:
                    again_check = inside_checking()
                    if(again_check):
                        continue
                    else:
                        break
        elif(x==4):
            #----------Admin_Add_Employees--------------------
            while True:
                
                print("Enter First Name : ")
                first_name = str(input()).strip()
                print("Enter Last  Name : ")
                last_name = str(input()).strip()
                user_emp_name =" ".join((first_name + " "+ last_name).split())

                print("Enter Email  Id  : ")
                user_emp_email = str(input()).strip()

                print("Enter Phone Number  : ")
                user_emp_Number = str(input()).strip()

                emp_info_checking = emp_data_check(user_emp_name,user_emp_email,user_emp_Number)
                emp_Duplicate_checking = admin_manage.add_employe(None,user_emp_name,user_emp_email,user_emp_Number)

                if(itemDel_checking):
                    break
                else:
                    
                    again_check = inside_checking()
                    if(again_check):
                        continue
                    else:
                        break

            print("Enter First Name : ")
            first_name = str(input()).strip()
            print("Enter Last  Name : ")
            last_name = str(input()).strip()
            user_emp_name =" ".join((first_name + " "+ last_name).split())

            print("Enter Email  Id  : ")
            user_emp_email = str(input()).strip()

            print("Enter Phone Number  : ")
            user_emp_Number = str(input()).strip()


            
        elif(x==5):
            pass
        
    else:
        continue






