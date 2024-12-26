#-------------Connection_System---------------
import re
import sys
import os
sys.path.append(r"Phitron_web_practice\Shoping_managment_system")
from seller_display.admin_data_store_sys.admin_data_store import store_all_item_display
from valid_check_sys.valid_data import Cheking_User_data
from seller_display.admin_valid_check_sys.admin_valid_data import item_checking
from valid_check_sys.valid_data import inside_checking
from customer_display.customer_data_store_sys.customer_data_store import Customer_manager


# #---------Customer_dispaly_Entry-----------------
customer_dis_list=[]

customer_dis_list.append(" (1) Store  View   Items    Enter                  : ")
customer_dis_list.append(" (2) Add To Cart   Enter                           : ")
customer_dis_list.append(" (3) View Cart Enter                               : ")
customer_dis_list.append(" (4) Order Conframe Cart Enter                     : ")
customer_dis_list.append(" (5) Order Quantity & Items Exchange Enter         : ")
customer_dis_list.append(" (6) My Card Order History Enter         : ")
customer_dis_list.append(" (7) Back Main Menu                                : ")
customer_dis_list.append(" (8) Exit Enter                                    : ")

#----------Customer_display_fun------------------
def customer_display_menu():
    for view_menu_admin_dis_list in customer_dis_list:
        print(view_menu_admin_dis_list)

#-------------------------Admin Display Data given---------------------
def Customer_display_data(cus_obj,cus_id):
    while True:
        print()
        customer_display_menu()
        x = input()
        if(Cheking_User_data(x,"Customer")):
            x = int(x)
            if(x==1):

                # ---------Customer Store View Item -----------
                store_all_item_display()

            elif(x==2):
                #---------- Customer Add to Cart  --------------------
                while True:
                    print("Enter Item Name     :")
                    item_name = (input()).strip()
                    item_name = re.sub(r'\s{2,}',' ',item_name)
                    print("Enter Item_quantity : ")
                    item_qun = (input()) 
                    print("Enter Shop Id  :")
                    shop_id = (input()) 
                    itemCardAdd_checking = item_checking(item_name,item_qun,shop_id)
                    item_name = item_name.title()
                    if(itemCardAdd_checking):
                            item_qun = int(item_qun)
                            shop_id = int(shop_id)
                            cus_obj.add_to_cart(item_name,item_qun,shop_id)
                            break
                    else:
    
                        again_check = inside_checking()
                        if(again_check):
                            continue
                        else:
                            break
               
            elif(x==3):
                #----------Customer View Cart Enter--------------------
                cus_obj.view_cart()

            elif(x==4):
                #----------Customer Order Conframe Cart Enter --------------------
                while True:
                    print("Enter Amount  : ")
                    try:
                        amount = int(input())
                    except Exception as e:
                        print(f"you are invalid Promt enter Place Only integer Number!!!!")
                        continue
                    order_valid = cus_obj.order_conframe(amount,cus_id,cus_obj)
                    if(order_valid):
                        break                                          
                    else:
                        again_check = inside_checking("cus_Amount")
                        if(again_check):
                            continue
                        else:
                            break
            elif(x==5):

                #----------- Customer Order Quantity & Items Exchange-----------
                while True:
                    print("(1) Item Remove of Cart Press :")
                    print("(2) Item Quantity Incrase Press :")
                    print("(3) Item Quantity Decrease Press :")
                    print("(4) Back Main Menu       :")
                    try:
                        exchnage_type = int(input().strip())
                        exchnage_type_str = str(exchnage_type)
                    except Exception as e:
                        print(f"{e} Place again '{exchnage_type}' input added Only integer !!!!")
                        continue

                    if(Cheking_User_data(exchnage_type_str,"Customer_exchange")):

                        if(exchnage_type==1):
                            print("Enter Item Name : ")
                            item_names = str(input())
                            item_names = item_names.title()
                            try:
                                print("Enter Shop Id : ")
                                shop_id = int(input())
                            except Exception as e:
                                print(f"{e} Place again input added Only integer !!!!")
                                continue 
                            if(cus_obj.searching_item_card(item_names,shop_id)):
                                 cus_obj.remove_item_quantity_cart(shop_id,item_names,"del")
                            else:
                                continue


                        elif(exchnage_type==2):
                            
                            print("Enter Item Name : ")
                            item_names = str(input())
                            item_names = item_names.title()                       
                            try:
                                print("Enter Item Increase Qauntity : ")
                                item_quantity = int(input())
                                print("Enter Shop Id : ")
                                shop_id = int(input())
                                
                            except Exception as e:
                                print(f"{e} Place again input added Only integer !!!!")
                                continue
                            if(cus_obj.searching_item_card(item_name,shop_id)):
                                cus_obj.remove_item_quantity_cart(shop_id,item_name,"+",item_quantity)
                            else:
                                continue
                        elif(exchnage_type==3):
                            
                            print("Enter Item Name : ")
                            item_names = str(input()) 
                            item_names = item_names.title()                      
                            try:
                                print("Enter Item Decrease Qauntity : ")
                                item_quantity = int(input())
                                print("Enter Shop Id : ")
                                shop_id = int(input())
                            except Exception as e:
                                print(f"{e} Place again input added Only integer !!!!")
                                continue
                            if(cus_obj.searching_item_card(item_name,shop_id)):
                                cus_obj.remove_item_quantity_cart(shop_id,item_name,"-",item_quantity)
                            else:
                                continue

                        elif(exchnage_type==4):
                            break                                               

                    else:
                        again_check = inside_checking()
                        if(again_check):
                            continue
                        else:
                            break

                
            elif(x==6):
                #------------Customer_card_history----------
                customer_id = cus_obj.get_cus_id()
                cus_obj.cus_card_history(customer_id)
            elif(x==7):
                #------------Back_return_main_page----------
                return "main_page"
                
            elif(x==8):
                #-----------Exit_Programme------------
                print("Exiting system. Goodbye!")
                print(f"-----------------------")
                return "system_exit"
                
            
        else:
            #--------again_run_program
            continue

