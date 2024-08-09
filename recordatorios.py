#Lista de recordatorios 
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#Agregar un eventp el 2 de Febrero de 2021 , a las 6 de la mañana 
recordatorios.insert(1,['2021-02-02', '06:00', 'Empezar el Año'])

#Editar el evento del 15 de Julio para que sea el 16 de Julio
for evento in recordatorios:
    if evento[0] == '2021-07-15': evento[0] = '2021-07-16'

#Eliminar el evento del dia del trabajo 
recordatorios = [evento for evento in recordatorios if evento[1] != '09:00']

#Agregar una cena de navidad y de año nuevo a las 22:00
recordatorios.insert(4,['2021-12-24','22:00','cena de navidad'])
recordatorios.append(['2021-12-31','22:00','cena de año nuevo'])


# Output
print(recordatorios)
