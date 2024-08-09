import sys

#Leer el contenido del archivo 
archivo = sys.argv[1]
with open("lorem_ipsum.txt","r") as file:
    archivo=file.read()

#Contar caracteres distintos
caracteres_distintos = set(archivo)
numero_caracteres_distintos = len(caracteres_distintos)

#Contar palabras distintas
palabras = archivo.split()
palabras_distintas = set(palabras)
numero_palabras_distintas = len(palabras_distintas)

# Mostrar los resultados
print(f"El número de caracteres distintos es: {numero_caracteres_distintos}")
print(f"El número de palabras distintas es: {numero_palabras_distintas}")