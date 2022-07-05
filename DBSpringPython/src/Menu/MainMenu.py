'''
Created on 5 jul. 2022

@author: nestor.solis
'''
from src.readTxt.Read import Archivo
from src.springCon.CreateEmployee import Create
from src.springCon.DeleteEmploye import Delete
from src.springCon.CreateWithTxt import CreateTxt
from src.springCon.FindEmployee import Find
from src.springCon.Listaremployee import Listar
from src.springCon.UpdateEmployee import Update

def mainmenu():
    print(" agenda ".title().center(85, "#"))
    menu=[["1. Ver info de archivo Txt"],["2. Agregar a DB datos Archivo TXT"],["3. Crear Employee"], \
          ["4. Eliminar Employee"], ["5. Encontrar Employee por id"],["6. Listar todos los Employee"],["7. Actualizar info Employee"],["8. Salir"]]
    for i in range(len(menu)):
            print(menu[i])
            print("")
    opcion=int(input("Introduzca la opción: "))
    if opcion==1:
        Archivo()
    elif opcion==2:
        CreateTxt()
    elif opcion==3:
        Create()
    elif opcion==4:
        Delete()
    elif opcion==5:
        Find()
    elif opcion==6:
        Listar()
    elif opcion==7:
        Update()
    elif opcion==8:
        exit()
    mainmenu()