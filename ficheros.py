#!/usr/bin/python3

fich = open("/etc/passwd","r")
lineas = fich.readlines()
for linea in lineas:
    login = linea.split(':')[0]
    shell = linea.split(':')[-1][:-1]
    print(login,shell)
print(len(lineas))
fich.close()
