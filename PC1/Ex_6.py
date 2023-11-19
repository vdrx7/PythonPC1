usuario_edad= int(input('Introduzca la edad del usuario: '))

if usuario_edad<=4:
    print('La entrada es gratis')
elif 4<usuario_edad<=18:
    print('La entrada le cuesta $5')
elif usuario_edad>18:
    print('La entrada le cuesta $10')