from abc import ABC,abstractmethod
#Developer Must be Use Below this Function
class forces(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def view_menu(self):
        pass
    @abstractmethod
    def add_item_card(self,cus_item_name,cus_item_qun):
        pass
    def customer_view_card(self):
        pass
    def pay_bill(self,cus_amount):
        pass

#connection Another File
import os
import sys

from admin_show_data import customer_view_items
from admin_show_data import customer_buy_items
from admin_sys.admin_system import cus
import re
    
# Devloper Function Created:

class customer_manage(forces):
    
    def __init__(self):
        self.__cart=[]
        self.__invalid_cart=[]

    def view_menu(self):
        customer_view_items()
    
    def add_item_card(self,cus_card_lst:dict):

        = 
        for key,value in cus_card_lst.items():


        pass
    def customer_view_card(self):
        pass
    def pay_bill(self,cus_amount):
        pass

#---------admin_dispaly_Entry-----------------
customer_dis_lst=[]
customer_dis_lst.append(" (1) View Items Menu  Enter       : ")
customer_dis_lst.append(" (2) Add  Items Enter          : ")
customer_dis_lst.append(" (3) View Card Enter        : ")
customer_dis_lst.append(" (4) Pay Bill Enter       : ")
customer_dis_lst.append(" (5) Back Main Menu            : ")
customer_dis_lst.append(" (6) Exit Enter                : ")

#----------admin_display_fun------------------
def customer_display_menu():
    for view_menu_customer_dis_lst in customer_dis_lst:
        print(view_menu_customer_dis_lst)

#----------------------- Customer Given Data Checking ----------------------------------
from admin_show_data import Cheking_User_data,inside_checking


#Valid_item & Qunatity_Check
def valid_item_quantity(cus_item_name,cus_item_price):
    if not cus_item_name.isalpha():
        print(f"This item name {cus_item_name} is invalid !")
        print(f"Place item name {cus_item_name} is Only String Character")
        return False
    if not isinstance(cus_item_quantity,int):
        print(f"This item {cus_item_name} Quantity '{cus_item_quantity}' Value is invalid !")
        print(f"Place item Quantity is Only Digit Value ")
        return False
    return True

#------------------Customer_Display_Data-------------------------------

while True:
    print()
    customer_display_menu()
    x = input()
    if(Cheking_User_data(x,"customer")):
        x = int(x)
        if(x==1):
            # ---------Customer View Items Menu-----------
            customer_view_items()
            pass
        elif(x==2):
            # ---------Customer add New Items of Card-----------
            customer_card_list={}
            while True:

                print(f"Enter Item Name: ")
                cus_item_name = input().strip()
                cus_item_name =re.sub(r'\s{2,}', ' ', cus_item_name)
                print(f"Enter Quantity: ")
                cus_item_quantity = int(input())

                if(valid_item_quantity(cus_item_name,cus_item_quantity)):
                    customer_card_list[cus_item_name] = customer_card_list.get(cus_item_name,0)+cus_item_quantity
                    if(inside_checking("Again_add_card")):
                        continue
                    else:
                        break
                else:

                    if(inside_checking("Invalid_promt")):
                        continue
                    else:
                        break
                        
            #working
            ex = customer_manage()
            ex.add_item_card(customer_card_list)
            




            
        elif(x==3):
            # ---------Admin add New Items-----------
            pass
        elif(x==4):
            # ---------Admin add New Items-----------
            pass
        elif(x==5):
            # ---------Admin add New Items-----------
            pass
        elif(x==6):
            # ---------Admin add New Items-----------
            pass

    else:
        #Wrong input again loop use
        continue
