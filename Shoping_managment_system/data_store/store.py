#-------------Connection_System-----------------------
import random 
#-----------Seller & Customer_Account Store-----------
       
class Account:
    __account_store={}
    __store_user_id=set()
    __shop_store_obj={}
    
    def _generate_emp_id(self):
         """Generate a unique 4-digit ID."""
         while True:
             un_user_id = random.randint(1000,9999)
             if un_user_id not in Account.__store_user_id:
                 return un_user_id
    
    def customer_seller_account_store(self,user_cus_name,
                                       user_cus_email,user_cus_Number,
                                       user_cus_Password,user):
          user_id = Account._generate_emp_id(None)
          Account.__account_store[user_id]={
           "Name": user_cus_name,
           "Email_id":user_cus_email,
           "Phone_Number":user_cus_Number,
           "Password":user_cus_Password,
           "User" : user

          }
          return user_id
    
    def seller_shop_obj_store(self,user_cus_email:str,shop_obj):
        Account.__shop_store_obj[user_cus_email]=shop_obj
    
    def mail_matching(self,user_cus_email,user_cus_password):
         
         for user_id, details in Account.__account_store.items():
            if details["Email_id"] == user_cus_email and details["Password"] == user_cus_password:
                if(details["User"]=="Seller"):
                    return True,user_id,details["User"],Account.__shop_store_obj[user_cus_email]
                else:
                    return True,user_id,details["User"],None
            else:
                return False,False,False,False
         
         
         
          
            
