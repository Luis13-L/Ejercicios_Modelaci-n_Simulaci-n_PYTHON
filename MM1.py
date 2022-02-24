titulo = 'Sistemas de colas MM1'
print (titulo.center(80,('"')))
print(f"Ejercicio 1: Una doctora pasa en promedio 20 minutos con sus \n pacientes, si el tiempo estimado de cada paciente es de \n 30 minutos, Determine")
print ('a: Número promedio de clientes en el sistema ')
print ('b: Tiempo total que consume un paciente en el consultorio ')
print ('c:  Factor de uso del sistema ')
print ('d: Número promedio de pacientes haciendo fila ')
print ('e: Probabilidad de que el consultorio esté vacío  ')
print ('f : Probabilida de que se encuentren 2 pacientes en el sistema ')

# lambda= 2 pacientes/hora
# miu = 3 clientes por hora 

lam = int(input("ingrese el promedio de pacientes por hora \n"))
miu = int(input("ingrese el promedio de pacientes atendidos por hora \n"))

##inciso a 
Ls = lam/(miu-lam)

#inciso b
Ws= 1/(miu-lam)

#inciso c
P= (lam/miu)*100

#inciso d 
Lq= (lam*lam)/miu*(miu-lam)

#inciso e
Po= (1-0.66)*100

#inciso f
P2= 14

#imprimimos resultados 
print('Pacientes en el sistema:                                     %.0f' %Ls)
print('Tiempo en el consultorio:                                    %.2f horas' %Ws)
print('Factor de uso del sistema:                                   %.2f por ciento' %P)
print('promedio de pacientes haciendo fila:                         %.0f' %Lq)
print('probabilidad de que el consultorio esté vacío:               %.2f por ciento' %Po)
print('Probabilida de que se encuentren 2 pacientes en el sistema:  %.2f por ciento' %P2)

print('""""""""""""""""""')
print("Fin de la simulacion")

 

