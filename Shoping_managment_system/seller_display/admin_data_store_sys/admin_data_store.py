#-------------Connection_System---------------
import os
import sys
from tabulate import tabulate

class Store_manager:
    __items_list={} # key :shop_id, key_value:item_name,key:item_name, value: list
    __our_store ={} # key :shop_id, value: shop_obj

    def __init__(self,shop_name):
        self.__shop_name = shop_name
        self.__shop_store ={}
        self.__shop_id=None

    def get_shop_id(self):
        return self.__shop_id
    #Store Info add:
    def add_our_store_info(self,shop_id):
        self.__shop_id= shop_id
        Store_manager.__our_store[shop_id]=self

    # Admin added new new item in items_list:
    def add_new_item(self, item_name:str, item_quantity:int, item_price:int):
        
        #************* Main_Store_Add*****************
        if self.__shop_id not in Store_manager.__items_list.keys():
            Store_manager.__items_list[self.__shop_id]={}

        if item_name  in Store_manager.__items_list[self.__shop_id].keys():
            Store_manager.__items_list[self.__shop_id][item_name][0]+= item_quantity 
        else:
            Store_manager.__items_list[self.__shop_id][item_name]=[item_quantity,item_price]   
        
        #************* Shop_Store_Add*****************
        if item_name not in self.__shop_store:
            self.__shop_store[item_name]=[item_quantity,item_price]
        else:
            self.__shop_store[item_name][0]+=item_quantity

        print(f"Item '{item_name}' is added successfully with quantity {item_quantity} and price {item_price}.")
    
    # Admin_display_view_items_All_Store
    def store_view_item(self):
        if not Store_manager.__items_list:
            print("No items available in the store.")
            return True

        # Iterate over all the shops and display their items in a formatted table
        for shop_id, item_name in Store_manager.__items_list.items():
            # Display the Shop ID
            print(f"Shop Name is : '{Store_manager.__our_store[shop_id].__shop_name}' and id is : '{shop_id}'")
            print("+-----------+-----------+-------+")
            print("| Item Name | Quantity  | Price |")
            print("+===========+===========+=======+")
            
            # Prepare data for each shop
            table_data = []
            for item, (quantity, price) in item_name.items():
                table_data.append([item, quantity, price])

            # Display the items in a table
            for row in table_data:
                print(f"| {row[0]:<10} | {row[1]:<9} | {row[2]:<5} |")
            print("+-----------+-----------+-------+")
            print("")  # Empty line for separation between shops

        return True

     # Admin_display_view_items_our_Store
    def our_store_view_item(self,shop_id):
        if shop_id not in Store_manager.__our_store:
            print(f"This Shop_id '{shop_id}' do not match anyone try again !!")
            return False
        
        print(f"Shop Name is : '{Store_manager.__our_store[shop_id].__shop_name}' and id is : '{shop_id}'")
        if not Store_manager.__our_store[shop_id].__shop_store:
            print("No items available in the store.")
            return True

        # Create table data
        table_data = []
        shop_obj = Store_manager.__our_store[shop_id]
        for  item_name,value in shop_obj.__shop_store.items():
            quantity = value[0]
            price = value[1]
            table_data.append([item_name, quantity, price])

        # Display table using tabulate
        headers = ["Item Name", "Quantity", "Price"]
        print(tabulate(table_data, headers=headers, tablefmt="grid", colalign=("center", "center", "center")))
        return True
    
    # Admin_Users deleted Items
    def admin_userRequested_deleted_item(self,shop_id:int,del_item_name:str):

        if shop_id not in Store_manager.__items_list:
            print(f"This shop id '{shop_id}' are not founded")
            return False
        
        if del_item_name not in Store_manager.__items_list[shop_id].keys():
            print(f"Shop id '{shop_id}' Item Name '{del_item_name}' are not founded")
            return False
        
        del Store_manager.__items_list[shop_id][del_item_name]
        shop_obj = Store_manager.__our_store[shop_id]
        del shop_obj.__shop_store[del_item_name]
        print(f"This item {del_item_name} is removed Successfully")
        return True
   
        
    # Admin_auto_deleted Items
    def admin_sell_decrease_item(self,shop_id:int,buy_item_name:str, buy_quantity:int):
        
        # Check if the item quantity exists in the shop
        if Store_manager.__items_list[shop_id][buy_item_name][0]< buy_quantity:
            print(f"Not enough stock or item '{buy_item_name}' does not exist.")
            return False
        
        # Decrease quantity in shop_store
        shop_obj = Store_manager.__our_store[shop_id]
        shop_obj.__shop_store[buy_item_name][0]-=buy_quantity
        if shop_obj.__shop_store[buy_item_name][0]==0:
            del shop_obj.__shop_store[buy_item_name]

        # Decrease quantity in items_list
        Store_manager.__items_list[shop_id][buy_item_name][0]-=buy_quantity
        if Store_manager.__items_list[shop_id][buy_item_name][0]==0:
            del Store_manager.__items_list[shop_id][buy_item_name]
        
    # Admin_Item_price_exchange
    def admin_exchnage_price(self,shop_id:int,item_name:str,ex_item_price:int,exchange_type:str):
        if(exchange_type=="+"):
            shop_obj = Store_manager.__our_store[shop_id]
            shop_obj.__shop_store[item_name][1]+=ex_item_price
            Store_manager.__items_list[shop_id][item_name][1]+=ex_item_price
        elif(exchange_type=='-'):
            shop_obj = Store_manager.__our_store[shop_id]
            shop_obj.__shop_store[item_name][1]-=ex_item_price
            Store_manager.__items_list[shop_id][item_name][1]-=ex_item_price
        print(f"Item Name '{item_name}' Price Added '{ex_item_price} Successfully")
        print(f"Item Name '{item_name}' Per Price are '{Store_manager.__items_list[shop_id][item_name][1]} ")
    
    #Admin_Searching_Store
    def admin_searching_item(self,shop_id,item_name,check=None):
       
       if item_name not in Store_manager.__items_list[shop_id].keys():
           print(f"This item '{item_name}' are not founded !!")
           if(check!=None):
               return False
           return False,False
       per_price = Store_manager.__items_list[shop_id][item_name][1]
       if(check=="Checking"):
           return True
       return True,per_price
    #Admin_get_item_price
    def get_item_price(self,shop_id,item_name):
         return Store_manager.__items_list[shop_id][item_name][1]


#-------------- Seller_Service ---------------------------------
def create_shop(shop_name,shop_id):
    shop = Store_manager(shop_name)
    shop.add_our_store_info(shop_id)
    return shop

def store_all_item_display():
    Store_manager.store_view_item(None)

def my_store_item_display(shop_id):
    Store_manager.our_store_view_item(None,shop_id)

def search_item(shop_id,item_name,check=None):
    return Store_manager.admin_searching_item(None,shop_id,item_name,check)

#-------------- Customer_Service ---------------------------------
def item_per_price(shop_id,item_name):
    return Store_manager.get_item_price(shop_id,item_name)




#-------------- main_function ----------------------------------
# shop1 = create_shop("Shop1", 1)
# shop2 = create_shop("Shop2", 2)
# shop3= create_shop("ss",50)


# # Adding items
# shop1.add_new_item("Potato", 100, 5)
# shop1.add_new_item("Onion", 50, 10)
# shop3.add_new_item("alo",30,5)

# # Selling items
# shop1.admin_sell_decrease_item(1,"Potato", 20)
# shop1.admin_sell_decrease_item(1,"Potato", 20)
# shop3.admin_sell_decrease_item(50,"alo", 60)

# shop1.store_view_item()
# shop1.our_store_view_item(1)













        

            
                
          
