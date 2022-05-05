class ViajeroFrecuente:
    __numviajero=''
    __DNI=''
    __nombre=''
    __apellido=''
    __millasacum=''
    
    def __init__(self,numviajero,DNI,nombre,apellido,millasacum):
        self.__numviajero=numviajero
        self.__DNI=DNI
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasacum=millasacum
    
    def muestra(self):
        return self.__numviajero+';'+self.__DNI+';'+self.__apellido+';'+self.__millasacum
    def returnnumviajero(self):
        return self.__numviajero
    def canttotalmillas(self):
        return self.__millasacum
    def acumularmillas(self,act):
        self.__millasacum+=act
        return self.__millasacum
    
    def canjearmillas(self,millascanj):
        if millascanj<=self.__millasacum:
            self.__millasacum-=millascanj
        else: print('ERROR')
    def __eq__(self,otroViajero): #Sobrecarga de operador mayor
        if self.__millasacum==otroViajero.__millasacum:
            return True
        else: return False
    def __radd__(self,milla):
        if type(milla)==int:
            return ViajeroFrecuente(self.__numviajero,self.__DNI,self.__nombre,self.__apellido,self.__millasacum+int(milla))
    def __rsub__(self,milla):
        if type(milla)==int:
            if self.__millasacum>=milla:
                return ViajeroFrecuente(self.__numviajero,self.__DNI,self.__nombre,self.__apellido,self.__millasacum-int(milla))