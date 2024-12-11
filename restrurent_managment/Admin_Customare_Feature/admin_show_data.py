import os
import sys
# Ignore this append path because inside of folder data
# sys.path.append( r"E:\CSE\Python\extra\Restrurent_web\restrurent_managment\Admin_feature\admin_sys")
from admin_sys.admin_system import*

#---------admin_dispaly_Entry-----------------
admin_dis_list=[]
admin_dis_list.append(" (1) Add New Items Enter       : ")
admin_dis_list.append(" (2) View Items Enter          : ")
admin_dis_list.append(" (3) Delete Items Enter        : ")
admin_dis_list.append(" (4) Add Employees Enter       : ")
admin_dis_list.append(" (5) View Employees List Enter : ")
admin_dis_list.append(" (6) Back Main Menu            : ")
admin_dis_list.append(" (7) Exit Enter                : ")

#----------admin_display_fun------------------
def admin_display_menu():
    for view_menu_admin_dis_list in admin_dis_list:
        print(view_menu_admin_dis_list)

#----------------------- Admin Given Data Checking ----------------------------------

#checking_input_comment
def Cheking_User_data(x,users):
    if  x.isalpha():
        print(f"This {x} is alpha Character Place given integer Number !")
        return False
    elif x.isdigit():
        x = int(x)
        if ( users=="Admin" and ( x<1 or x>7)  ):
            print(f"Place Sir given This Number (1 to 7) are inclusive")
            return False
        elif(users=="customer" and ( x<1 or x>6) ):
            print(f"Place Sir given This Number (1 to 6) are inclusive")
            return False
        else:
            return True
    else:
        print(f"This {x} is Numeric number Place given integer Number !")
        return False
    
#Checking_inside_input_comment
def inside_checking(users_check="Admin"):
     if(users_check=="Again_add_card"):
         print("If you more Items Added In Card Press (1) :")
         print("If you not  Items Added In Card Press (0) :")
     elif(users_check=="Invalid_promt"):
         print("If you again Added Item  press     (1): ")
         print("If you  Not again Added Item press (0): ")
     elif(users_check=="Admin"):
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

    username_pattern = r'^[a-zA-Z][a-zA-Z\s]{3,29}$'
    return re.match(username_pattern, user_emp_name) is not None

#Checking_Valid_Number
import phonenumbers
def validate_and_format_number(number,default_code="BD"):
    try:
        parse_number = phonenumbers.parse(number,default_code)
        if phonenumbers.is_valid_number(parse_number):
            formatted_number = phonenumbers.format_number(parse_number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            return formatted_number
        else:
         return False
    except phonenumbers.NumberParseException:
        return False
        

def emp_data_check(user_emp_name:str,user_emp_mail:str,user_emp_Number:str):
    invalid_list=[]
    if not (is_valid_mail(user_emp_email)):
        invalid_mail = f"This Mail {user_emp_email} is invalid"
        invalid_list.append(invalid_mail)

    if not (is_valid_name(user_emp_name)):
         invalid_name = f"This Name {user_emp_name} is Invalid"
         invalid_extra = f"Name Must be Only (4 to 30) Character Between"
         invalid_list.append(invalid_name)
         invalid_list.append(invalid_extra)

    if not(validate_and_format_number(user_emp_Number)):
        invalid_number = f"This number {user_emp_Number} is Invalid"
        invalid_list.append(invalid_number)
    
    if(len(invalid_list)):
        for invalid_item in invalid_list:
            print(invalid_item)
        return False
    else:
        return True

    

   


                      


    
#-------------------------Admin Display Data given---------------------

while True:
    print()
    admin_display_menu()
    x = input()
    if(Cheking_User_data(x,"Admin")):
        x = int(x)
        if(x==1):
            # ---------Admin add New Items-----------
            while True:

                print("Enter Item Name     :")
                item_name = (input()).strip()
                item_name = re.sub(r'\s{2,}',' ',item_name)
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
                 delete_item_name= str(input()).strip()
                 delete_item_name =re.sub(r'\s{2,}', ' ', delete_item_name)

                 itemDel_checking = admin_manage.deleted_item_admin(None,delete_item_name)
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
                user_emp_name ="".join((first_name + " "+ last_name))
                user_emp_name=re.sub(r'\s{2,}',' ',user_emp_name)

                print("Enter Email  Id  : ")
                user_emp_email = str(input()).strip()

                print("Enter Phone Number  : ")
                user_emp_Number = str(input()).strip()

                emp_info_checking = emp_data_check(user_emp_name,user_emp_email,user_emp_Number)
                
                if(emp_info_checking and admin_manage.add_employe(None,user_emp_name,user_emp_email,user_emp_Number)):
                     
                    break
                else:
                    again_check = inside_checking()
                    if(again_check):
                        continue
                    else:
                        break
        elif(x==5):
            #-----------view_emp_list-----------
            admin_manage.view_employee_list(None)
            
        elif(x==6):
            #------------back_main_menu----------
            pass
        elif(x==7):
            #-----------Exit_Programme------------
            print("Exiting system. Goodbye!")
            print(f"-----------------------")
            break
            
        
    else:
        #--------again_run_program
        continue

# customer_service_part

def customer_view_items():
    admin_manage.view_item(None)

    





