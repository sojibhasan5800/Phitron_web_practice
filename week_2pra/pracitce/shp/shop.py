import os
import sys
# target_folder ="e:/CSE/Python/oop/phitron_pracitce/week_2pra/pracitce/prd"
target_folder1 ="E:\CSE\Python\oop\phitron_pracitce\week_2pra\pracitce"
target_folder2 ="E:/CSE/Python/oop/phitron_pracitce/week_2pra/pracitce/bank_account"
sys.path.append(target_folder1)
sys.path.append(target_folder2)
print(sys.path)
from prd.product import*
from bank_account_copy.acc_credit import*

class Shops(Forces):
    def __init__(self):
        # user display in products;
        for item,price in ProDucts.value.items():
            print(item,"->",price)
            

        
        
    def add_product(self,*item_name):
        stock=[]
        for items in item_name:
            self.stock.append(items)
    def buy_products(self,amount):
        flag=True
        not_avaiable=[]
        for prd_names in self.stock:
            having = ProDucts.value.get(prd_names,'empty')
            if(having=='empty'):
                flag =False
                not_avaiable.append(prd_names)
        if(flag):
            self.amount-=200
            add = card(200)
            for prd_names in self.stock:
                ProDucts.value.pop([prd_names])
            


            print(f"cogratess your abivable balance is {amount}")
        else:
            print("not abile able this product")
            for x in not_avaiable:
                print(x,end=" ")
    def __repr__(self):
        return "Thanks sir comming again"

if __name__=="__main__":
    rahim = Shops()
    owner = card(2000)
    owner.get_balance()
    
    

        

