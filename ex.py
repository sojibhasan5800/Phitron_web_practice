class Store_manager:
    __items_list = {}  # Shared across all instances
    __our_store = {}   # Shared across all instances

    def __init__(self, shop_name):
        self.__shop_name = shop_name
        self.__shop_store = {}
        self.__shop_id = None

    # Store Info add:
    def add_our_store_info(self, shop_id):
        self.__shop_id = shop_id
        self.__our_store[shop_id] = self  # Store the object itself

    # Admin added new item in items_list:
    def add_new_item(self, item_name: str, item_quantity: int, item_price: int):
        #************* Main_Store_Add*****************
        if self.__shop_id not in self.__items_list:
            self.__items_list[self.__shop_id] = {}

        if item_name in self.__items_list[self.__shop_id]:
            self.__items_list[self.__shop_id][item_name][0] += item_quantity
        else:
            self.__items_list[self.__shop_id][item_name] = [item_quantity, item_price]

        #************* Shop_Store_Add*****************
        if item_name not in self.__shop_store:
            self.__shop_store[item_name] = [item_quantity, item_price]
        else:
            self.__shop_store[item_name][0] += item_quantity

        print(f"Item '{item_name}' is added successfully with quantity {item_quantity} and price {item_price}.")

    # Sell an item and decrease quantity
    def sell_item(self, item_name: str, quantity: int):
        # Check if the item exists in the shop
        if item_name not in self.__shop_store or self.__shop_store[item_name][0] < quantity:
            print(f"Not enough stock or item '{item_name}' does not exist.")
            return False

        # Decrease quantity in shop_store
        self.__shop_store[item_name][0] -= quantity
        if self.__shop_store[item_name][0] == 0:
            del self.__shop_store[item_name]

        # Decrease quantity in items_list
        self.__items_list[self.__shop_id][item_name][0] -= quantity
        if self.__items_list[self.__shop_id][item_name][0] == 0:
            del self.__items_list[self.__shop_id][item_name]

        print(f"Item '{item_name}' sold successfully. Quantity decreased by {quantity}.")
        return True

    # Admin deleted an item by request
    def admin_userRequested_deleted_item(self, shop_id: int, del_item_name: str):
        if shop_id not in self.__items_list:
            print(f"This shop ID '{shop_id}' is not found.")
            return False

        if del_item_name not in self.__items_list[shop_id]:
            print(f"Shop ID '{shop_id}' Item Name '{del_item_name}' is not found.")
            return False

        del self.__items_list[shop_id][del_item_name]
        if del_item_name in self.__shop_store:
            del self.__shop_store[del_item_name]

        print(f"This item '{del_item_name}' is removed successfully.")
        return True

#-------------- Seller_Service ---------------------------------
def create_shop(shop_name, shop_id):
    shop = Store_manager(shop_name)
    shop.add_our_store_info(shop_id)
    return shop

#-------------- main_function ----------------------------------
# Creating shops
shop1 = create_shop("Shop1", 1)
shop2 = create_shop("Shop2", 2)

# Adding items
shop1.add_new_item("Potato", 100, 5)
shop1.add_new_item("Onion", 50, 10)

# Selling items
shop1.sell_item("Potato", 20)

# Check inventory
print("Shop1 inventory:", shop1._Store_manager__shop_store)
print("Global inventory:", Store_manager._Store_manager__items_list)
