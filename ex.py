class ka:
    __order=[]
    def __init__(self,name):
        self.name = name
    def logic(self):
        self.__order.append(10)
    def p(self):
        print(*self.__order)

la = ka("s")
la.logic()
la.p()