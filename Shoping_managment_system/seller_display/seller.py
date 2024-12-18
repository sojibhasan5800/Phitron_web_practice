#-------------Connection_System---------------
import re
import os
import sys
from valid_check_sys.valid_data import Cheking_User_data
from admin_valid_check_sys.admin_valid_data import item_checking


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

                itemAdd_checking = item_checking(item_name,item_qun,price_kg)
                
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