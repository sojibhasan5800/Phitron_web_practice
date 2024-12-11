import random
import phonenumbers
from tabulate import tabulate


from abc import ABC,abstractmethod
# Creater Must be Subclass Under this method Use:
class shape(ABC):
    @abstractmethod
    def add_new_item(self,item_name:str,item_quantity:int, item_price:int):
        pass
    @abstractmethod
    def view_item(self):
        pass
    @abstractmethod
    def delete_item(self,delete_item_name:str):
        pass
    @abstractmethod
    def add_employe(self,emp_name:str,emp_mail:str,emp_num:str):
        pass

class admin_manage(shape):
    __items_list={}
    __employe_info={}
    __store_emp_id=set()
    

    # Admin added new new item in items_list:
    def add_new_item(self, item_name:str, item_quantity:int, item_price:int):

        try:

            if isinstance(item_name,str) and item_name.isalpha() and isinstance(item_quantity,int) and isinstance(item_price,int):

                new_value_lst=[item_quantity,item_price]
                admin_manage.__items_list[item_name]= admin_manage.__items_list.get(item_name,[0]*len(new_value_lst))
                admin_manage.__items_list[item_name]=list(map(lambda x,y : x+y,admin_manage.__items_list[item_name],new_value_lst))
                print(f"item_list {item_name} is added in successfully")
            else:
                print("item_name are Invalid Place given Only string Character")
                return False


        except Exception as e:

            if "item_quantity" not in  locals():
                print("item_quantity are Invalid Place given Only integer Number")
            elif "item_price" not in  locals():
                print("item_price are Invalid Place given Only integer Number")

            print(f"{type(e).__name__} : Sir place check your items information and try again !")
            return False
        
        return True

    #admin View of this items of list:  
    def view_item(self):
        print("Below this item are Store :")
        print("---------------------------")
        if not admin_manage.__items_list:
            print("Can not be Store Any items")
            return
        
        view_item_table =[" Item_Name "," Quantity ", " Price "]
        table_item_data =[
            [item,qun_price[0],qun_price[1]]
            for item,qun_price in admin_manage.__items_list.items()
        ]
        print(tabulate(table_item_data,headers=view_item_table,tablefmt="grid"
                       , stralign="center", numalign="center"))

    # Admin deleted Items
    def deleted_item_admin(self,del_item_name:str):

        if isinstance (del_item_name,str):
            item_exit = admin_manage.__items_list.get(del_item_name,False)
        #Problem
            if(item_exit):
                del admin_manage.__items_list[del_item_name]
                print(f"This item {del_item_name} is removed Successfully")
                return True
            else:
                print(f"Sorry Sir This item {del_item_name} name are not founded !")
                return False
            
        else:
            #this part are Igonore not necessary
            print(f"Place Check Item Name are Only string !")
  
        return True
        

    # Admin added employees

    def add_employe(self, emp_name_split:str, emp_mail:str, emp_num:str):
        #Named must be first and last name use

        
        
        #Duplicated Email Check
        if emp_mail in [e['Email_id'] for e in admin_manage.__employe_info.values()]:
            print(f"Error: The email {emp_mail} is already in use.")
            return False
        #Duplicated Number Check
        if emp_num in [p ['Phone_Number'] for p in admin_manage.__employe_info.values()]:
            print(f"Error: The employee number {emp_num} is already in use.")
            return False
        
        #generate unique id
        def _generate_emp_id(self):
            """Generate a unique 4-digit ID."""
            while True:
                un_emp_id = random.randint(1000,9999)
                if un_emp_id not in admin_manage.__store_emp_id:#PRB
                    return un_emp_id
                

        emp_id = _generate_emp_id(None)
        
        def validate_and_format_number_sys(number,default_code="BD"):
            parse_number = phonenumbers.parse(number,default_code)
            if phonenumbers.is_valid_number(parse_number):
                formatted_number = phonenumbers.format_number(parse_number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                return formatted_number
                
         
               
        admin_manage.__employe_info[emp_id]={
            "Name": emp_name_split,
            "Email_id":emp_mail,
            "Phone_Number":validate_and_format_number_sys(emp_num)

        }
        print(f"Employee ID: {emp_id} & name: {emp_name_split} is added Successfully")
        return True
    
    #Admin_View_Employee_list:
    def view_employee_list(self):
        if not admin_manage.__employe_info:
            print("No employee data available.")
            return
        headers= ["Employee ID", "Name", "Email", "Phone Number"]
        table_data=[
            [key_emp_id, data["Name"], data["Email_id"], data["Phone_Number"]]
            for key_emp_id,data in admin_manage.__employe_info.items()
        ]
        print(tabulate(table_data, headers=headers, tablefmt="double_grid",
                        stralign="center", numalign="center"))
        return
    
    #Customer_view_item_aviable
    def customer_check_avaiable_item(self,cus_item_name,cus_item_quan):
        item_not_avaiable_list=[]
        item_added_list=[]
        
        check_avle_item = admin_manage.__items_list.get(cus_item_name,False)
        if(check_avle_item):
            store_quantity = admin_manage.__items_list[cus_item_name][0]
            if(store_quantity>=cus_item_quan):
                return True
            else:
                no_quantity=f"This '{cus_item_name}' item are not enough '{store_quantity}' quantity in our Store !"
                ava_quantity=f"This '{cus_item_name}' item are avaiable  quantity is ==> '{store_quantity}'"
                item_not_avaiable_list.append(no_quantity)
                item_not_avaiable_list.append(ava_quantity)

        else:
            no_item=f"This '{cus_item_name}' item are not founded in our Store !"
            item_not_avaiable_list.append(no_item)
        return

    

       




if __name__ == "__main__":
    pass



        
        

        



        



        
        




     

        