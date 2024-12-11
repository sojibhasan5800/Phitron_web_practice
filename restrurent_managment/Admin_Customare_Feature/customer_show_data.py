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
    def add_item(self,cus_item_name,cus_item_qun):
        pass
    def view_card(self):
        pass
    def pay_bill(self,cus_amount):
        pass

#connection Another File
import os
import sys

from admin_show_data import customer_view_items

    
# Devloper Function Created:

class customer_manage(forces):
    
    def __init__(self):
        self.cart=[]

    def view_menu(self):
        customer_view_items()
    
    def add_item(self,cus_item_name,cus_item_qun):
        pass
    def view_card(self):
        pass
    def pay_bill(self,cus_amount):
        pass

#---------admin_dispaly_Entry-----------------
customer_dis_lst=[]
customer_dis_lst.append(" (1) View Menu  Enter       : ")
customer_dis_lst.append(" (2) Add  Items Enter          : ")
customer_dis_lst.append(" (3) View Card Enter        : ")
customer_dis_lst.append(" (4) Pay Bill Enter       : ")
customer_dis_lst.append(" (5) Back Main Menu            : ")
customer_dis_lst.append(" (6) Exit Enter                : ")

#----------admin_display_fun------------------
def customer_display_menu():
    for view_menu_customer_dis_lst in customer_dis_lst:
        print(view_menu_customer_dis_lst)

#------------------Customer_Display_Data-------------------------------

while True:
    print()
    customer_display_menu()
    x = input()
    if(Cheking_User_data(x)):
        pass
    else:
        #Wrong input again loop use
        continue
