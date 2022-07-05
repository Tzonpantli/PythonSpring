'''
Created on 5 jul. 2022

@author: nestor.solis
'''
from src.springCon.TokenSecurityHeaders.TokenAutori import api_call_headers
import requests
def Create():
    ids= input("ingrese un id: ")
    nombre= input("ingrese un nombre: ")
    apellido= input("ingrese un apellido: ")
    naciona= input("inrgese una nacionalidad: ")
    lengua= input("ingrese un lenguaje: ")
    aeropuerto= input("aeropuerto: ")
    
    processor_count_api_url = "http://localhost:8080/employee/crear"
    usuario = {
    "id": ids,
    "apellido": apellido,
    "nombre": nombre,
    "nacio": naciona,
    "lenguaje": lengua,
    "aero": aeropuerto
    }
    api_call_response = requests.post(processor_count_api_url, headers=api_call_headers,json=usuario, verify=False)
    print(api_call_response.text)
    