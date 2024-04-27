'''Funcionalidades extras para usarlas en el resto de módulos'''

import os
import platform

def binary_question(msg:str) -> str:
    ''' Permite devolver un caracter a una respuesta si/no sobre una pregunta '''

    resp_list = ['s', 'S', 'n', 'N']
    resp = None
    print(msg, end= " ")

    while resp not in resp_list:
        resp = input()
        if resp not in resp_list:
            print("Opción invalida vuelva a intentarlo")

    if resp == 's' or resp == 'S': 
        return 's'
    else:
        return 'n'
    

def clear_scr() -> None:
    '''Limpia la pantalla de la terminal en cualquier SO'''
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")