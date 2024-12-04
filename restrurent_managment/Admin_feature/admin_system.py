import random
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

            if isinstance(item_name,str) and isinstance(item_quantity,int) and isinstance(item_price,int):
                self.__items_list[item_name]=[item_quantity,item_price]
                print(f"item_list {item_name} is added in successfully")
        except Exception as e:
            print(f"{e} : Sir place check your items information and try again !")
            return

    #admin View of this items of list:  
    def view_item(self):
        print("Below this item are Store :")
        for item,qun_price in self.__items_list.items():
            qun = qun_price[0]
            pri = qun_price[1]
            print(f"Item_Name ==> {item} Qunatity is: {qun} Price is: {pri}")

    # Admin added employees
    def add_employe(self, emp_name_split:str, emp_mail:str, emp_num:str):
        #Named must be first and last name use

        #Duplicated Email Check
        if emp_mail in [e['Email_id'] for e in self.__employe_info.values()]:
            print(f"Error: The email {emp_mail} is already in use.")
            return "dup_mail"
        #Duplicated Number Check
        if emp_num in [p ['Phone_Number'] for p in self.__employe_info.values()]:
            print(f"Error: The employee number {emp_num} is already in use.")
            return "dup_number"
        
        #generate unique id
        def _generate_emp_id(self):
            """Generate a unique 4-digit ID."""
            while True:
                un_emp_id = random.randint(1000,9999)
                if un_emp_id not in admin_manage.__store_emp_id:#PRB
                    return un_emp_id
                

        emp_id = _generate_emp_id()
        self.__employe_info[emp_id]={
            "Name": emp_name_split,
            "Email_id":emp_mail,
            "Phone_Number":emp_num

        }
        print(f"Employee ID: {emp_id} & name: {emp_name_split} is added Successfully")
    
    # Admin deleted Items
    def _deleted_item(self,del_item_name:str):
        if isinstance (del_item_name,str):
            item_exit = self.__items_list.get(del_item_name,False)
            if(item_exit):
                del self.__items_list[del_item_name]
                print(f"This item {del_item_name} is removed Successfully")
            else:
                print(f"Sorry Sir This item {del_item_name} name are not founded !")
            
        else:
            print(f"Place Check Item Name are Only string !")
            return



        
        

        



        



        
        




     

        