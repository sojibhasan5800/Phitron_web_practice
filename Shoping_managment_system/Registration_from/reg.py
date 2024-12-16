#-------------Connection_System---------------
import re
import os
import sys
from valid_check_sys.valid_data import user_data_check

def reg_display_from():
    print("Enter First Name : ")
    first_name = str(input()).strip()
    print("Enter Last  Name : ")
    last_name = str(input()).strip()
    user_cus_name ="".join((first_name + " "+ last_name))
    user_cus_name=re.sub(r'\s{2,}',' ',user_cus_name)

    print("Enter Email  Id  : ")
    user_cus_email = str(input()).strip()  

    print("Enter Phone Number  : ")
    user_cus_Number = str(input()).strip()

    print("Create a strong password: ")
    user_cus_Password = str(input()).strip()
    print("Retype your password: ")
    user_retype_cus_password = str(input()).strip()

    result = user_data_check(user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user_retype_cus_password)
    return result
