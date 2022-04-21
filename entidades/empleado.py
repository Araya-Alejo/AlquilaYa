class Empleado():
    def __init__(self, nombre, apellido, contrasenia, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contrasenia = contrasenia
        self.__correo = correo


    #Getters
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getContrasenia(self):
        return self.__contrasenia

    def getCorreo(self):
        return self.__correo


    #Setter
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    def setCorreo(self, correo):
        self.__correo = correo
