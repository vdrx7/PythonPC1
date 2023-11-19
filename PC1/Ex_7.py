num1=float(input('Introduce el primer número: '))
num2=float(input('Introduce el segundo número: '))

suma = num1+num2
resta= num1-num2
multiplicación= num1*num2

print('\nMenú:')
print('1. Suma')
print('2. Resta')
print('3. Multiplicación')

opcion= input('Selecciona entre la opción 1,2 o 3: ')
if opcion == '1':
    print(str(suma))
elif opcion== '2':
    print(str(resta))
elif opcion== '3':
    print(str(multiplicación))
else:
    print('Opción no valida, seleccionar 1, 2 o 3')