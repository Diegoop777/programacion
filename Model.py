class usuarios:
    def __init__(self, Id:int,nombre:str,password,rol:str,bloqueado:False)-> None:
        self.__id_usuario = Id
        self.__nombre_usuario = nombre
        self.__password_usuario = password
        self.__rol_usuario = rol
        self.__bloqueado = bloqueado
        
        
    def getIdUsuario(self)->int:
        return self.__id_usuario

    def getNombreUsuario(self)->str:
        return self.__nombre_usuario
    
    def getPasswordUsuario(self)->int:
        return self.__password_usuario
    
    def getRolUsuario(self)->str:
        return self.__rol_usuario
    
    def getUsuarioBloqueado(self):
        return self.__bloqueado
        
    def setNombre(self, nuevonombre:str):
        self.__Nombre = nuevonombre
