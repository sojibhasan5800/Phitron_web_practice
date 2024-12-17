#-------------Connection_System---------------
import re
import os
import sys
from valid_check_sys.valid_data import Cheking_User_data,inside_checking
from Registration_from.reg import reg_display_from

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

while True:
    print()
    user_display_menu()
    x = input()
    if(Cheking_User_data(x,"Registration")):
        x = int(x)
        if(x==1):
            #-----------Customer_Registration-----------
            while True:
                result,user_id,user_cus_name =reg_display_from()
                if(result):
                    print(f"Dear {user_cus_name} Regsitration is Successfully")
                    print(f"Your Account Id: {user_id}")
                    break
                else:
                    if(inside_checking()):
                        continue
                    else:
                        break


        elif(x==2):
             #-----------Seller_Registration-----------
            pass
        elif(x==3):
             #-----------User_Login-----------
            pass
        elif(x==4):
            #-----------Exit_Programme------------
            print("Exiting system. Goodbye!")
            print(f"-----------------------")
            break
    else:
        #--------again_run_program
        continue






