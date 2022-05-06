titulo = 'ARBOL DE DECISIÓN'
print (titulo.center(80,('"')))
print(f"Se presentará un ejemplo de un modelo de árbol para tomar una decisión de Mantener \n dinero o Cambiar de Teléfono, Se cuenta con Q2000 en disponibilidad, cabe destacar que \n contamos con 1 pagos pendiente en la Universidad. Y la importancia gira sobre mi \n satisfacción de cambiar de teléfono y dejar que pase el tiempo sin pagar y que aumente la mora. (Endeudarme)")
print ('Mantener Dinero: ')
print ('•	Pagar colegiatura de Universidad (90%) V=0.2')
print ('•	Ahorrar (10%)')
print ('        o	Con el tiempo comprar un teléfono de mayor valor (75%) V=0.7')
print ('        o	Comprar ropa (25%) V=0.2')
print ('Comprar el Teléfono:')
print ('        •	Xiaomi (20%) V=0.85')
print ('        •	Huawei (80%) V=0.20')



# lambda= 2 pacientes/hora
# miu = 3 clientes por hora 
print ('Mantiene el dinero')

lam = float(input("Si mantiene el dinero Cual es la probabilidad de que pague la cuota de la U?  \n"))
por1 = float(input("Cual sería el grado de molestia que te causaría? \n"))
miu = float(input("Cual es la probabilidad de que ahorre el dinero? \n"))
op1 = float(input("Si ahorra el dinero cual es la probabilidad de que con el tiempo se compre un teléfono mas reciente? \n"))
op11 = float(input("Cual sería el grado de molestia que te causaría? \n"))
op2 = float(input("Si ahorra el dinero cual es la probabilidad de que compre ropa? \n"))
op21 = float(input("Cual sería el grado de molestia que te causaría? \n"))

print ('Compra un Teléfono\n')
op3 = float(input("Si compras un teléfono cual es la probabilidad de que sea Xiaomi? \n"))
op33 = float(input("Cual sería el grado de molestia que te causaría? \n"))

op4 = float(input("Cual es la probabilidad de que sea Huawei? \n"))
op44 = float(input("Cual sería el grado de molestia que te causaría? \n"))







##inciso a 
Ls = lam*por1

#inciso b
Ws= miu*op1*op11

#inciso c
P= miu*op2*op21
#inciso d 
Lq= op3*op33

#inciso e
Po= op4*op44

#operaciones 

if Ls>=Ws and Ls>=P and Ls>=Lq and Ls>=Po:
    total1=Ls
    total2="Pagar deudas"
elif Ws>=Ls and Ws>=P and Ws>=Lq and Ws>=Po:
    total1=Ws
    total2="Esperar un modelo reciente"
elif P>=Ls and P>=Ws and P>=Lq and P>=Po:
    total1=P
    total2="Comprar ropa"
elif Lq>=Ls and Lq>=Ws and Lq>=P and Lq>=Po:
    total1=Lq
    total2="Compra un Xiaomi"
elif Po>=Ls and Po>=Ws and Po>=P and Po>=Lq:
    total1=Po
    total2="Comprar Samsumg"
#imprimimos resultados 
print('Datos \n')

print('Pagar Deuda:                                     %.0f' %Ls)
print('Esperar modelo Reciente:                                     %.0f' %Ws)
print('Comprar Ropa:                                     %.0f' %P)
print('Comprar Xiaomi:                                     %.0f' %Lq)
print('Comprar Samgung:                                     %.0f' %Po)


print('No funciono :|')



print('""""""""""""""""""')
print('De acuerdo a los datos la mejor opción es  :                                     %.0f' %total1)
print('Con un porcentaje de   :                                     %.0f' %total2)


print('""""""""""""""""""')
print("Fin de la simulacion")