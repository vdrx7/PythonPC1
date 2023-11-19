time = input('Indique la hora: ')
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

if hours==7 or (hours==8 and minute==0):
    print('Es hora de tomar desayuno')

if hours==12 or (hours==13 and minute==0):
    print('Es hora de almorzar')

if hours==18 or (hours==19 and minute==0):
    print('Es hora de cenar')