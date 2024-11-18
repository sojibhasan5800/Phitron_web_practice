class card:
    __balance =0
    def __init__(self,money):
        self.__balance+=money
    def get_balance(self):
        print(f"your account balance is : {self.__balance}")
# cm = card(2000)
# cm._balance=100
# cm.get_balance()
# cm = card(100)
# cm.__balance=20
# cm.get_balance()