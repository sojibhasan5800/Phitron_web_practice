#-------------Connection_System---------------
import re
import sys
import os
sys.path.append(r"Shoping_managment_system")
from seller_display.admin_data_store_sys.admin_data_store import store_all_item_display
from valid_check_sys.valid_data import Cheking_User_data



# #---------Customer_dispaly_Entry-----------------
customer_dis_list=[]

customer_dis_list.append(" (1) Store  View   Items    Enter : ")
customer_dis_list.append(" (2) Add To Cart   Enter          : ")
customer_dis_list.append(" (3) View Cart Enter              : ")
customer_dis_list.append(" (4) Order To Cart  Enter         : ")
customer_dis_list.append(" (5) Back Main Menu               : ")
customer_dis_list.append(" (6) Exit Enter                   : ")

#----------Customer_display_fun------------------
def customer_display_menu():
    for view_menu_admin_dis_list in customer_dis_list:
        print(view_menu_admin_dis_list)

#-------------------------Admin Display Data given---------------------
def Customer_display_data(shop_obj):
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
                store_all_item_display()
                
            elif(x==3):
                #----------Our_store_view_item--------------------
                shop_id = shop_obj.get_shop_id()
                my_store_item_display(shop_id)

            elif(x==4):
                #----------Our_store_delete_item--------------------
                while True:
                    print("Delete Item Name : ")
                    delete_item_name= str(input()).strip()
                    delete_item_name =re.sub(r'\s{2,}', ' ', delete_item_name)
                    delete_item_name = delete_item_name.title()

                    shop_id = shop_obj.get_shop_id()
                    itemDel_checking = shop_obj.admin_userRequested_deleted_item(shop_id,delete_item_name)
                    if(itemDel_checking):
                        break
                    else:

                        again_check = inside_checking()
                        if(again_check):
                            continue
                        else:
                            break
            elif(x==5):

                #-----------Item_Price_Exchnage-----------
                while True:
                    print("Item Name : ")
                    print("Back Main Menu Press(0) :")
                    item_name= str(input()).strip()
                    if(item_name=="0"):
                        break
                    item_name =re.sub(r'\s{2,}', ' ', item_name)
                    item_name = item_name.title()
                    print("(1) Price Increase Press :")
                    print("(2) Price Decrease Press :")
                    print("(3) Back Main Menu       :")
                    try:
                        exchnage_type = int(input().strip())
                        exchnage_type_str = str(exchnage_type)
                    except Exception as e:
                        print(f"{e} Place again input added !!!!")
                        continue
                   
                    shop_id = shop_obj.get_shop_id()
                    item_exit,per_price = search_item(shop_id,item_name)

                    if(Cheking_User_data(exchnage_type_str,"Seller_exchange") and item_exit):
                        if(exchnage_type==1):
                            print(f"Item Name '{item_name}' & Before Price '{per_price}'")
                            print("Increase After Per Item Pirce Enter : ")
                            try:
                                ex_price = int(input().strip())
                                shop_obj.admin_exchnage_price(shop_id,item_name,ex_price,"+")
                            except Exception as e:
                                print(f"{e} Item Price '{ex_price}' are Wrong !!")
                                continue
                            

                        elif(exchnage_type==2):
                            print(f"Item Name '{item_name}' & Before Price '{per_price}'")
                            print("Increase After Per Item Pirce Enter : ")
                            try:
                                ex_price = int(input().strip())
                                if(ex_price<0):
                                    print(f"Item Price '{ex_price}' are Wrong !!")
                                else:
                                    shop_obj.admin_exchnage_price(shop_id,item_name,ex_price,"-")
                            except Exception as e:
                                print(f"{e} Item Price '{ex_price}' are Wrong !!")
                                continue
                        else:
                            break

                    else:
                        again_check = inside_checking()
                        if(again_check):
                            continue
                        else:
                            break

                
            elif(x==5):
                #------------Back_return_main_page----------
                return "main_page"
                
            elif(x==6):
                #-----------Exit_Programme------------
                print("Exiting system. Goodbye!")
                print(f"-----------------------")
                return "system_exit"
                
            
        else:
            #--------again_run_program
            continue

