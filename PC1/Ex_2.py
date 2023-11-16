consumo = float(input('Cuanto fue su consumo?: '))
porcen = float(input('Que porcentaje de propina desea dar?: '))
tip = consumo * (porcen/100)
print(f'La propina a dejar es de ${tip:.2f}')
