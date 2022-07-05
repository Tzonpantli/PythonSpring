'''
Created on 5 jul. 2022

@author: nestor.solis
'''
from src.springCon.TokenSecurityHeaders.TokenAutori import api_call_headers
import requests
def Find():
    ids=input("ingrese el id del employee para consultar detalles: ")
    processor_count_api_url = "http://localhost:8080/employee/detalles/{}".format(ids)
    api_call_response = requests.get(processor_count_api_url, headers=api_call_headers, verify=False)
    print(api_call_response.text)
