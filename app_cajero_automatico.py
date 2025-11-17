print('*** Cajero Automatico ***')
salir = False
saldo = 1000
while not salir:
    print('''Elige la opcion que deseas
    1. Depositar
    2. Retirar
    3. Consultar''')
    opcion = int(input('Elige la opcion: '))
    if opcion == 1:
        deposito = int(input('Cuanto deseas depositar: '))
        saldo += deposito
    elif opcion == 2:
        retiro = int(input('Cuanto deseas retirar: '))
        if retiro <= saldo:
            saldo -= saldo
    elif opcion == 3:
        print(f'Tu saldo actual es de ${saldo} pesos')
    else:
        print('opcion no valida')
else:
    print('Saliendo del sistema')