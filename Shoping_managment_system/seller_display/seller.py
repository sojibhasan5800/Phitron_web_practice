#-------------Connection_System---------------
import re
import sys
import os
sys.path.append(r"Shoping_managment_system")
from valid_check_sys.valid_data import Cheking_User_data,inside_checking
from seller_display.admin_data_store_sys.admin_data_store import Store_manager,store_all_item_display,my_store_item_display,search_item
from seller_display.admin_valid_check_sys.admin_valid_data import item_checking



# #---------admin_dispaly_Entry-----------------
admin_dis_list=[]
admin_dis_list.append(" (1) Add     New   Items    Enter : ")
admin_dis_list.append(" (2) Store  View   Items    Enter : ")
admin_dis_list.append(" (3) Our Store View Items   Enter : ")
admin_dis_list.append(" (4) Our Store Delete Items Enter : ")
admin_dis_list.append(" (5) Item  Price  Exchange  Enter : ")
admin_dis_list.append(" (6) Back Main Menu               : ")
admin_dis_list.append(" (7) Exit Enter                   : ")

#----------admin_display_fun------------------
def admin_display_menu():
    for view_menu_admin_dis_list in admin_dis_list:
        print(view_menu_admin_dis_list)

#-------------------------Admin Display Data given---------------------
def seller_display_data(shop_obj):
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
                    item_qun = (input()) 
                    print("Enter Per_kg Price  :")
                    price_kg = (input()) 

                    itemAdd_checking = item_checking(item_name,item_qun,price_kg)
                    item_name = item_name.title()
                    if(itemAdd_checking):
                        item_qun = int(item_qun)
                        price_kg = int(price_kg)
                        shop_obj.add_new_item(item_name,item_qun,price_kg)
                        break
                    else:
                        
                        again_check = inside_checking()
                        if(again_check):
                            continue
                        else:
                            break

            elif(x==2):
                #---------- Store_view_item --------------------
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

                
            elif(x==6):
                #------------Back_return_main_page----------
                return "main_page"
                
            elif(x==7):
                #-----------Exit_Programme------------
                print("Exiting system. Goodbye!")
                print(f"-----------------------")
                return "system_exit"
                
            
        else:
            #--------again_run_program
            continue

