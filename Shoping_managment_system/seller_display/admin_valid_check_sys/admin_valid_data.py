#-------------Connection_System---------------


#------------ Item_Check -----------------------
def item_checking( item_name:str, item_quantity:int, item_price:int,itemer =None):
   if(itemer==None):
       if isinstance(item_name,str) and item_quantity.isdigit() and item_price.isdigit():
        return True
       
       else:
          if not item_quantity.isdigit():
                    print("item_quantity are Invalid Place given Only integer Number")
          if not item_price.isdigit():
                    print("item_price are Invalid Place given Only integer Number")
                
          print("Sir place check your items information and try again !")
          return False
#    elif(itemer=="exchange"):
#         if isinstance(item_name,str) and  item_price.isdigit():
#              return True
#         else:
#             if not item_price.isdigit():
#                 print("item_price are Invalid Place given Only integer Number")
#             print("Sir place check your items information and try again !")
#             return False

            

