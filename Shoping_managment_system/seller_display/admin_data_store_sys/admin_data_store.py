#-------------Connection_System---------------
import os
import sys


class Store_manager:
    __items_list={}
    __our_store ={}

    def __init__(self,shop_name):
        self.__shop_name = shop_name
        self.__shop_store ={}
        self.__shop_id=None

    #Store Info add:
    def add_our_store_info(self,shop_id):
        self.__shop_id= shop_id
        self.__our_store[shop_id]=self.__shop_name

    # Admin added new new item in items_list:
    def add_new_item(self, item_name:str, item_quantity:int, item_price:int):
        
        #************* Main_Store_Add*****************
        if self.__shop_id not in self.__items_list.keys():
            self.__items_list[self.__shop_id]={}

        if item_name  in self.__items_list[self.__shop_id]:
            self.__items_list[self.__shop_id][item_name][0]+= item_quantity 
        else:
            self.__items_list[self.__shop_id][item_name]=[item_quantity,item_price]   
        
        #************* Shop_Store_Add*****************
        if item_name not in self.__shop_store:
            self.__shop_store[item_name]=[item_quantity,item_price]
        else:
            self.__shop_store[item_name][0]+=item_quantity

        print(f"Item '{item_name}' is added successfully with quantity {item_quantity} and price {item_price}.")
    
    # Admin_Users deleted Items
    def admin_userRequested_deleted_item(self,shop_id:int,del_item_name:str):

        if shop_id not in self.__items_list:
            print(f"This shop id '{shop_id}' are not founded")
            return False
        
        if self.__items_list[shop_id][del_item_name] not in self.__items_list[shop_id].values():
            print(f"Shop id '{shop_id}' Item Name '{del_item_name}' are not founded")
            return False
        
        del self.__items_list[shop_id][del_item_name]
        del self.__our_store[del_item_name]
        print(f"This item {del_item_name} is removed Successfully")
        return True
   
        
    # Admin_auto_deleted Items
    def admin_auto_deleted_item(self,shop_id:int,buy_item_name:str, quantity:int):
        
        self.__items_list[shop_id][buy_item_name][0]-=quantity
        
    


       
            
            
        
  
    




#-------------- Seller_Service ---------------------------------
def create_shop(shop_name,shop_id):
    shop = Store_manager(shop_name)
    shop.add_our_store_info(shop_id)

#-------------- main_function ----------------------------------
shop = Store_manager("hi")
shop.add_our_store_info(20)
shop.add_new_item("alo",20,10)
shop.add_new_item("alo",60,90)








        

            
                
          
