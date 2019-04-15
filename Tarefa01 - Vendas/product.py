class Product:
    __id = None
    __nome = None    
    __preco = None

    def __init__(self, id, nome, preco):
        self.__id = id
        self.__nome = nome        
        self.__preco = preco

    def getProductId(self):
        return self.__id

    def getProductNome(self):
        return self.__nome

    def getProductPreco(self):
        return self.__preco