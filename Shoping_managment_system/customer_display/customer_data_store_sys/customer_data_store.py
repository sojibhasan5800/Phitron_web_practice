
#-------------Connection_System---------------
import os
import sys
import random
from tabulate import tabulate
sys.path.append(r"Shoping_managment_system")
from seller_display.admin_data_store_sys.admin_data_store import item_per_price,search_item
class Customer_manager:
    __custmer_store={}
    __order_store={}
    __invoice_no_store=set()
    __cus_order_history={}

 #Working!!!!!!!!!!!
    def __init__(self,cus_name):
        self.__cus_name = cus_name
        self.__cus_cart ={}
        self.__cus_id=None
        self.__total_price=0
        
    
    def get_cus_id(self):
        return self.__cus_id
    
    #Customer Info add:
    def add_our_store_info(self,cus_id):
        self.__cus_id= cus_id
        Customer_manager.__custmer_store[cus_id]=self

    # Customer Add cart:
    def add_to_cart(self,item_name,quantity,shop_id):
        if shop_id not in self.__cus_cart.keys():
            self.__cus_cart[shop_id]={}
            self.__cus_cart[shop_id][item_name]=quantity
        elif item_name not in self.__cus_cart[shop_id].keys():
            self.__cus_cart[shop_id][item_name]=quantity
        else:
            self.__cus_cart[shop_id][item_name]+=quantity
       
        
    #Customer_view_cart:
    def view_cart(self,taken = None):
        if not self.__cus_cart:
            print("No items Add in this cart.")
        
        total_price =0
        headers = ["Product", "Quantity", "per_price", "Total_Price","shop id"]
        table_data=[]

        for shop_id,item_name in self.__cus_cart:
            item_per_price = item_per_price(shop_id,item_name)
            for quantity in item_name.values():
                item_total_price = item_per_price*quantity
                total_price+=item_total_price
                table_data.append([item_name,quantity,item_per_price,item_total_price,shop_id])
        
        self.__total_price = total_price
        table = tabulate(table_data, headers, tablefmt="fancy_grid",colalign=("center", "center", "center"))
        print(table)
        print(f"Customer_card : {self.__cus_id}")
        print(f"Total_Price   : {total_price}")
        print()
        if(taken!=None):
            return table
        
    #Customer_remove_item_cart:
    def remove_item_quantity_cart(self,shop_id,item_name,symbol,quantity=0):
        
        x,y,z=search_item(shop_id,item_name)
        if(x==False):
            print(f"This item '{item_name}' is not founded !!!!")
            return False
        if(quantity==0):
            del self.__cus_cart[shop_id][item_name]
            print(f"Item Name '{item_name}' Removed Susscessfully")
            return True
        elif (symbol=='+'):
               self.__cus_cart[shop_id][item_name]+=quantity
               print(f"Item Name '{item_name}' & Quantity {quantity} Added Susscessfully")
               return True
        elif(symbol=='-'):
            if(self.__cus_cart[shop_id][item_name]<quantity):
                print(f"This cart not enough Quantity '{quantity}' & max Decrease '{self.__cus_cart[shop_id][item_name]}'")
                return False
            else:
                self.__cus_cart[shop_id][item_name]-=quantity
                print(f"Item Name '{item_name}' & Quantity {quantity} Decrease Susscessfully")
                return True
            
    #Customer_Order_Confirm:
    def order_conframe(self,amount:int,user_id):
        if not self.__cus_cart:
            print("No items Add in this cart.")
            return False
        invoice_no = Customer_manager._generate_invoice_id(None)
        store_not_avaiable_item=[]
        total_price =0
        headers = ["Product", "Quantity", "per_price", "Total_Price","shop id"]
        table_data=[]

        for shop_id,item_name in self.__cus_cart:

            if(search_item(shop_id,item_name,"Checking")==False):
                wrong_item = f"This item '{item_name}' Shop are not avaiable !!!"
                store_not_avaiable_item.append(wrong_item)
            
            item_per_price = item_per_price(shop_id,item_name)
            for quantity in item_name.values():
                item_total_price = item_per_price*quantity
                total_price+=item_total_price
                table_data.append([item_name,quantity,item_per_price,item_total_price,shop_id])
        
        self.__total_price = total_price
        if( len(store_not_avaiable_item)==0 and amount>=total_price):
            print(f"Youe Invoice No : {invoice_no} Buy Items Successfully")
            self.__order_store[user_id]=invoice_no
            if user_id not in self.__cus_order_history:
                self.__cus_order_history[user_id]={}
            self.__cus_order_history[user_id][invoice_no]= Customer_manager.view_cart(None,"table")
            return True
        elif(len(store_not_avaiable_item)!=0):
            #Working


    def _generate_invoice_id(self):
        """Generate a unique 4-digit ID."""
        while True:
            invoice_id = random.randint(1000,9999)
            if invoice_id not in Customer_manager.__invoice_no_store:
                return invoice_id







    

    
    