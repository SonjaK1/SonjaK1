# test primjer  kockice('2, 4, 1, 6, 4') 

def kockice(string_brojeva):
  suma = 0
  lista = string_brojeva.split(', ')
  for i in range(len(lista)):
    suma += int(lista[i])
  return suma
