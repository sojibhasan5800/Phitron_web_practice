
#-------------Connection_System---------------
import os
import sys
import random
from tabulate import tabulate
sys.path.append(r"Shoping_managment_system")
from seller_display.admin_data_store_sys.admin_data_store import item_per_price,search_item_customer,selling_order
class Customer_manager:
    __custmer_store={} # key :Customer_id , Value : customer_obj
    __order_store={} # key :Customer_id , Value : customer_invoice_no
    __invoice_no_store=set() # Value : Uniqe_customer_invoice_no
    __cus_order_history={} # key :Customer_id , key_Value : invoice_no, value : order_table

 #Working!!!!!!!!!!!
    def __init__(self,cus_name):
        self.__cus_name = cus_name
        self.__cus_cart ={} # key :shop_id , key_Value : Item_name, value : Quantity
        self.__cus_id=None
        self.__total_price=0
        
    
    def get_cus_id(self):
        return self.__cus_id
    
    #Customer Info add:
    def add_cus_info(self,cus_id):
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
        print(f"Item Name :'{item_name}' & Quantity : '{quantity}' Added Susscesfully")
       
        
    #Customer_view_cart:
    def view_cart(self,taken = None):
        if not self.__cus_cart:
            print("No items Add in this cart.")
            return
        
        total_price =0
        headers = ["Product", "Quantity", "per_price", "Total_Price","shop id"]
        table_data=[]

        for shop_id,item_name_ky in self.__cus_cart.items():
            for item_name,quantity in item_name_ky.items():
                item_price = item_per_price(shop_id,item_name)
                item_total_price = item_price*quantity
                total_price+=item_total_price
                table_data.append([item_name,quantity,item_price,item_total_price,shop_id])
        
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
        if shop_id not in self.__cus_cart:
            print(f"Shop id '{shop_id}' are not Founded in Cart")
            return False
        if item_name not in self.__cus_cart[shop_id]:
            print(f"Item Name '{item_name}' are not Founded in Cart")
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
    def order_conframe(self,amount:int,user_id,cus_obj):
        if not self.__cus_cart:
            print("No items Add in this cart.")
            return False
        
        store_not_avaiable_item=[]
        total_price =0
        headers = ["Product", "Quantity", "per_price", "Total_Price","shop id"]
        table_data=[]

        #Checking--item--quantity--avaiable
        for shop_id,item_name_ky in self.__cus_cart.items():   
            for item_name,quantity in item_name_ky.items():

                if(search_item_customer(shop_id,item_name,quantity)==False):
                  wrong_item = f"This item '{item_name}' Shop are not avaiable !!!"
                  store_not_avaiable_item.append(wrong_item)
              
                item_price = item_per_price(shop_id,item_name)
              
            for quantity in item_name_ky.values():
                item_total_price = item_price*quantity
                total_price+=item_total_price
                table_data.append([item_name,quantity,item_price,item_total_price,shop_id])
        
        self.__total_price = total_price
        if( len(store_not_avaiable_item)==0 and amount>=total_price): 
            invoice_no = Customer_manager._generate_invoice_id(None)

            for shop_id,item_name_ky in self.__cus_cart.items():
                for buy_item_name,buy_quantity in item_name_ky.items():
                   selling_order(shop_id,buy_item_name,buy_quantity)
                
            print(f"Youe Invoice No : {invoice_no} Buy Items Successfully")
            Customer_manager.__order_store[user_id]=invoice_no
            if user_id not in Customer_manager.__cus_order_history:
                Customer_manager.__cus_order_history[user_id]={}
            self.__cus_order_history[user_id][invoice_no]= cus_obj.view_cart("table")
            self.__cus_cart.clear()
            print(f"Item Cherging {self.__total_price} tk Last Balance {amount - self.__total_price}")
            return True
        
        elif(len(store_not_avaiable_item)!=0):
            return False
        else:
            print(f"Tola buy items price are '{self.__total_price}' Amount are not enough!!!!!!")
            return False
   
   #Generate_Invoice_Id
    def _generate_invoice_id(self):
        """Generate a unique 4-digit ID."""
        while True:
            invoice_id = random.randint(1000,9999)
            if invoice_id not in Customer_manager.__invoice_no_store:
                return invoice_id
    
    #Seraching_Customer_card:
    def searching_item_card(self,item_name,shop_id):
        if shop_id not in self.__cus_cart.keys():
            print(f"Not Founded  Shop id '{shop_id}'")
            return False
        if item_name not in self.__cus_cart[shop_id].keys():
            print(f"Not Founded Item Name of Cart '{item_name}'")
            return False
        return True
    #Customer_card_history:
    def cus_card_history(self,customer_id):
        if customer_id in Customer_manager.__cus_order_history:
            for invoice_no_key, history_order_table in Customer_manager.__cus_order_history[customer_id].items():
                print(history_order_table)
        else:
            print(f"Customer ID {customer_id} Card is Empty!!!!!.")




def create_customer(cus_name,cus_id):
    cus_obj = Customer_manager(cus_name)
    cus_obj.add_cus_info(cus_id)
    return cus_obj






    

    
    