from entidades.empleado import Empleado
# Importa desde el modulo Entidades la clase Empleado


class EmpleadoServicio():
    '''
        Función que valida que una cadena no este vacia.
        Retorna un String.
    '''

    def validarString(self, msj):
        while True:
            cadena = input(msj)
            if (not cadena):
                print("Error!")
            else:
                break
        return cadena

    '''
        Función que crea un objeto con todo sus atributos.
        La creacion de un objeto.
    '''

    def crearEmpleado(self):
        es = EmpreadoServicio()
        nombre = es.validarString("Ingrese el nombre: ")
        apellido = es.validarString("Ingrese el apellido: ")
        contrasenia = es.validarString("Ingrese el contraseña: ")
        correo = es.validarString("Ingrese el correo: ")

        return Usuario(nombre, apellido, contrasenia, correo)
        print(Empreado)
