from abc import ABC,abstractmethod
class Forces(ABC):
     @abstractmethod
     def add_product(self,name,price):
          self.name=name
          self.price=price
     def buy_product(self,amount):
        self.amount = amount


class ProDucts:
    value={}
    def __init__(self,dictonary):
        try:
                for name,price in dictonary.items():
                     if isinstance(name,str) and isinstance(price,int):
                     
                        self.value[name]=price
                     else:
                        print("check your item")
                
        except Exception as e:
             print("you have been missing this type :",e)


# if __name__=="__main__":
dv = {"oil":2000,"gold":5000,"patrol":50000}
dvk = ProDucts(dv)

     
    
             


        