import sys


# Obtener las tasas de conversión y el valor en pesos chilenos desde los argumentos
tasa_sol = float(sys.argv[1])
tasa_peso_arg = float(sys.argv[2])
tasa_dolar = float(sys.argv[3])
valor_peso_chileno = float(sys.argv[4])

#Realiza las conversiones
valor_sol = valor_peso_chileno * tasa_sol
valor_peso_arg = valor_peso_chileno * tasa_peso_arg
valor_dolar = valor_peso_chileno * tasa_dolar

#Mostrar los resultados
print(f"{valor_peso_chileno} pesos equivalen a:")
print(f"{valor_sol:.1f} Soles")
print(f"{valor_peso_arg:.1f} Pesos Argentinos")
print(f"{valor_dolar:.1f} Dólares")
