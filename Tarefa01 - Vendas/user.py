class User:
    __id = None
    __nome = None    
    __idade = None
    __documento = None

    def __init__(self, id, nome, idade, documento):
        self.__id = id
        self.__nome = nome        
        self.__idade = idade
        self.__documento = documento

    def getUserId(self):
        return self.__id

    def getUserNome(self):
        return self.__nome

    def getUserIdade(self):
        return self.__idade

    def getUserDoc(self):
        return self.__documento

    def getUserName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "usuario nao encontrado!!"
        return (retorno)