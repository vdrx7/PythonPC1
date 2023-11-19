archivo = input('Insertar nombre del archivo: ')
nombre, extension = archivo.split(".")

if extension == 'gif':
    print('image/gif')

if extension == 'jpg':
    print('image/jpeg')

if extension == 'jpeg':
    print('image/jpeg')

if extension == 'png':
    print('image/png')

if extension == 'pdf':
    print('application/pdf')

if extension == 'txt':
    print('text/plain')

if extension == 'zip':
    print('application/zip')