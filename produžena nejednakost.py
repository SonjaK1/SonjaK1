def nejednakost(niz):

  lista_brojeva = niz.split(' ')

  for i in range(len(lista_brojeva)):
    lista_brojeva[i] = int(lista_brojeva[i])

  lista_brojeva.sort()

  for i in range(len(lista_brojeva)):
    lista_brojeva[i] = str(lista_brojeva[i])    

  print(' < '.join(lista_brojeva))
