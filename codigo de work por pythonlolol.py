from io import open
import pickle
import os
texto = input("escriba el texto ")
nombre = input("escriba el nombre del archivo que quiera crear y al final escriba esto .pckl sin espacion al momento de escribirlo ")
fichero = open(nombre,"wb")
pickle.dump(texto,fichero)
fichero.close()
del(fichero)
os.system("cls")
cargar = input("escriba el archivo pckl con su extencion ")
fichero = open(cargar,"rb")
lista = pickle.load(fichero)
os.system("cls")
print(lista)
input("")