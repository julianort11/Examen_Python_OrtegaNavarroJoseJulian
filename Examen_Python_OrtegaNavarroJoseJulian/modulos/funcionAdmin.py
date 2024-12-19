import os
import json
import modulos.mensajes as mensajes
import modulos.ui as menus 
#---------------------------------------------------------------------------------------------

def guardarArchivo(Diccionario, archivo):
    with open(f"./modulos/{archivo}.json",'w') as f: 
        json.dump(Diccionario, f, indent=4) 
    return True

def abrirArchivo(archivo): 
    with open(f"./modulos/{archivo}.json",'r') as entrada:
        nuevoDiccionario = json.load(entrada)
        return nuevoDiccionario
    
entradaAdmin = abrirArchivo('baseDatos')
admin_datos = abrirArchivo('baseDatos')

def crearUsuario (aggClientes: dict):

    nombres = input("Ingrese el nombre del usuario/cliente: ").capitalize()
    apellido = input("Ingrese el apellido del usuario/cliente: ").capitalize()
    id = int(input("Ingrese el ID del usuario/cliente: "))
    direccion = input("Ingrese la direccion del usuario/cliente: ")

    informacionCliente = {
        "nombre" : nombres,
        "apellidos" : apellido,
        "id": id,
        "direccion" : direccion,
        "categoria" : {
            "nuevos clientes": False,
            "clientes Regulares": False,
            "clientes leales": False
        }
    }

    aggClientes['clientes'].append(informacionCliente)
    guardarArchivo(entradaAdmin,"baseDatos")

    print(mensajes.msgNuevoUsuiaro)
    print(f"El acceso del usuario es con su numero de ID {id}")
    return entradaAdmin

#---------------------------------------------------------------------------------------------
#funcio Principal
def administrador (admin_datos: dict):
    while True:
#        DocumentoIngresado =int(input("Ingrese su codigo de ingreso como administrador: "))
#        encontrado = False  
#        for admin in admin_datos["administracionInfo"]: 
#            if DocumentoIngresado == admin["codigo"]: 
#                encontrado = True
#                nombreAdmin = admin["codigo"]
#                print(f"""
#                    ====================================
#                      Camper encontrado: {nombreAdmin}
#                    ====================================
#                    """)
                while True:
                    print(menus.menuOpcionAdmin1)
                    OpcionAdmin1 = int(input(":D_ "))
                    match OpcionAdmin1:
                        case 1:
                            crearUsuario(entradaAdmin)
                            x=input("presione cualquier tecla para continuar..")
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            return
                    #os
                break
#            else:
#                print(mensajes.mensajeSinencontrar)
#                #os
#                return