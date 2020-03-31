def popis(imena):
  lista_imena = imena.split(', ')
  for i in range(len(lista_imena)):
    osoba = lista_imena[i].split(' ')
    osoba[0] = osoba[0].lower().capitalize()
    osoba[1] = osoba[1].lower().capitalize()
    lista_imena[i] = ' '.join(osoba)
  lista_imena.sort()
  print(', '.join(lista_imena))
