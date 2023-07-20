#Cronometro
import os
import time

print('CRONOMETRO\n')

for h in range(0,24):
  for m in range(0,60):
    for s in range(0,60):
        os.system('clear')
        print('Hora: ',h,'Minutos: ',m,'Segundos: ',s)
        time.sleep(1)