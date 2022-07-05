'''
Created on 5 jul. 2022

@author: nestor.solis
'''
from src.springCon.TokenSecurityHeaders.TokenAutori import api_call_headers
import requests
def CreateTxt():
    archivo=open("C:/Users/nestor.solis/Documents/PythonLuis/DBSpringPython/src/Clientes.txt","r")
    data = [tuple(line.split(",")) for line in archivo]
    for i in range(len(data)):
        val=list(data[i])
        print(val)
        #print(val[0])
        usuario = {
        "id": i,
        "apellido": val[0],
        "nombre": val[1],
        "nacio": val[2],
        "lenguaje": val[3],
        "aero": val[4]
        }
        processor_count_api_url = "http://localhost:8080/employee/crear"
        api_call_response = requests.post(processor_count_api_url, headers=api_call_headers,json=usuario, verify=False)
        print("La data añadida es:")
        print(api_call_response.text)
        print("")
    
