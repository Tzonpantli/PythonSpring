'''
Created on 5 jul. 2022

@author: nestor.solis
'''
from src.springCon.TokenSecurityHeaders.TokenAutori import api_call_headers
import requests
def Listar():
    processor_count_api_url = "http://localhost:8080/employee/listar"
    api_call_response = requests.get(processor_count_api_url, headers=api_call_headers, verify=False)
    print(api_call_response.text)

