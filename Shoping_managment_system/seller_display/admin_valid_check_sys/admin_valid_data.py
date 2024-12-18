#-------------Connection_System---------------


#------------ Item_Check -----------------------
def item_checking( item_name:str, item_quantity:int, item_price:int):
    if isinstance(item_name,str) and item_name.isalpha() and isinstance(item_quantity,int) and isinstance(item_price,int):
        return True
    else:
        if "item_quantity" not in  locals():
                print("item_quantity are Invalid Place given Only integer Number")
        elif "item_price" not in  locals():
                print("item_price are Invalid Place given Only integer Number")
        elif "item_name" not in locals():
              print("item_name are Invalid Place given Only string Character")
              
        print("Sir place check your items information and try again !")
        return False
