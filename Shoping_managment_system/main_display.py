#-------------Connection_System---------------
import re
import os
import sys
sys.path.append(r"Shoping_managment_system")
from valid_check_sys.valid_data import Cheking_User_data,inside_checking
from Registration_from.reg import reg_display_from,login_display_from
from seller_display.seller import seller_display_data


#---------Users_dispaly_Entry-----------------
main_lst=[]
main_lst.append(" (1) Customer Registration Press : ")
main_lst.append(" (2) Seller   Registration Press : ")
main_lst.append(" (3) User       Login      Press : ")
main_lst.append(" (4) Exit      Program     Press : ")

#----------Users_display_fun------------------
def user_display_menu():
    for view_menu_user_dis_list in main_lst:
        print(view_menu_user_dis_list)



#-------------------------Users Display Data given---------------------
#Wk connection on main Page
while True:
    print()
    user_display_menu()
    x = input()
    if(Cheking_User_data(x,"Registration")):
        x = int(x)
        if(x==1):
            #-----------Customer_Registration-----------
            while True:
                result,user_id,user_cus_name =reg_display_from("Customer")
                if(result):
                    print(f"Dear {user_cus_name} Regsitration is Successfully")
                    print(f"Your Account Id: {user_id}")
                    continue
                else:
                    if(inside_checking()):
                        continue
                    else:
                        break


        elif(x==2):
             #-----------Seller_Registration-----------
            result,shop_id,user_cus_name =reg_display_from("Seller")
            if(result):
                    print(f"Dear {user_cus_name} Regsitration is Successfully")
                    print(f"Your Shop Id: {shop_id}")
                    continue
            else:
                if(inside_checking()):
                    continue
                else:
                    break    
            
        elif(x==3):
             #-----------User_Login-----------
            result,user_id,users,shop_obj = login_display_from()
            if(result):
                print(f"Login successful for user ID: {user_id}")

                #-----------seller_display-----------
                if(users=="Seller"):
                    running = seller_display_data(shop_obj)
                    if(running == "main_page"):
                        continue
                    elif(running == "system_exit"):
                        break
                    
                #-----------customer_display-----------
                elif(users=="Customer"):
                    pass
            else:
                print("Invalid email or password")
                continue
            
                 
            
        elif(x==4):
            #-----------Exit_Programme------------
            print("Exiting system. Goodbye!")
            print(f"-----------------------")
            break
    else:
        #--------again_run_program
        continue






