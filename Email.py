class Email: #Creo Clase Email
    __idcuenta = ''
    __dominio = ''     #Empieza con "@"
    __tipodominio = '' #Empieza con un "."
    __passw = ''
    def __init__(self, idcuenta = '', dominio = '', tipodominio = '', passw = ''):    #Constructor
        self.__idcuenta = idcuenta
        self.__dominio = dominio
        self.__tipodominio = tipodominio
        self.__passw = passw
    def retornaEmail(self):                  #Metodo Retorna Email Final
        return self.__idcuenta+'@'+self.__dominio+'.'+self.__tipodominio
    def getdominio(self): #Metodo Obtener Dominio
        return self.__dominio
    def getContraseña(self): #Metodo Obtener Dominio
        return self.__passw

    def setContraseña(self, passwNUEVA):
        self.__passw = passwNUEVA

    def verificaContraseña(self, contraseña):
        return self.__passw==contraseña
