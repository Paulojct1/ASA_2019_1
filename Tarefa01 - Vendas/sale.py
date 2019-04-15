class Sale:
    __id__ = None
    __user__ = None
    __product__ = None
    __quantity__ = None
    __total__ = None    

    def __init__(self, id, user, product, quantity, total):
        self.__id = id
        self.__user = user        
        self.__product = product
        self.__quantity = quantity
        self.__total = total

    def getSaleId(self):
        return self.__id

    def getSaleUser(self):
        return self.__user

    def getSaleProduct(self):
        return self.__product

    def getSaleQuantity(self):
        return self.__quantity

    def getSaleTotal(self):
        return self.__total