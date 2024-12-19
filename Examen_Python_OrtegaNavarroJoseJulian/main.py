import os
import modulos.ui as menu
import modulos.mensajes as mensajes
import modulos.funcionAdmin as administrador
#funcion principal

if __name__ == "__main__":
    while True:
        print(mensajes.Bienvenido)
        print(menu.memnuIngreso)
        opcionIngreso = int(input(":D_ "))
        match opcionIngreso:
            case 1:
                pass
            case 2:
                administrador.administrador(administrador.entradaAdmin)
            case 3:
                break
            case _:
                print(mensajes.mensajeSinOpcion)
                os.system('pause')
