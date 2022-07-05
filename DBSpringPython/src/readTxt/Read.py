'''
Created on 5 jul. 2022

@author: nestor.solis
'''
def Archivo():
    archivo=open("C:/Users/nestor.solis/Documents/PythonLuis/DBSpringPython/src/Clientes.txt","r")
    data = [tuple(line.split(",")) for line in archivo]
    for i in range(len(data)):
        val=list(data[i])
        print(val)