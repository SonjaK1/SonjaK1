# zbroj kockica  kockice('2, 4, 1, 6, 4') 

def kockice(string_brojeva):
  suma = 0
  lista = string_brojeva.split(', ')
  for i in range(len(lista)):
    suma += int(lista[i])
  return suma


# obrnute riječi u rečenici  obrnute_rijeci('danas je dobar dan') 
  
def obrnute_rijeci(recenica):

  lista_rijeci = recenica.split(' ')
  lista_rijeci.reverse()

  return ' '.join(lista_rijeci)


# obrni redoslijed recenica u paragrafu
# obrnuti_text('Imam cijelu čokoladu. Poof. Čokolade nema.')

def obrnuti_text(paragraf):
  recenice = paragraf.split('. ')
  recenice[-1] = recenice[-1].strip('.')
  recenice.reverse()
  recenice[-1] += '.'
  print('. '.join(recenice))


# produžena nejednakost  nejedn('56 23 1 12 32 51 11 132 2 12')

def nejedn(niz):

  lista_brojeva = niz.split(' ')

  for i in range(len(lista_brojeva)):
    lista_brojeva[i] = int(lista_brojeva[i])

  lista_brojeva.sort()

  for i in range(len(lista_brojeva)):
    lista_brojeva[i] = str(lista_brojeva[i])    

  print(' < '.join(lista_brojeva))


# sortiraj listu imena
#popis('ANA ANIĆ, Mia Mijić, SARA SARIĆ, lucija lucić, Petra Petrić, LUKA LUKIĆ, IVAN IVANOVIĆ, Marko Markić, petar petrić, filip filipić')

def popis(imena):
  lista_imena = imena.split(', ')
  for i in range(len(lista_imena)):
    osoba = lista_imena[i].split(' ')
    osoba[0] = osoba[0].lower().capitalize()
    osoba[1] = osoba[1].lower().capitalize()
    lista_imena[i] = ' '.join(osoba)
  lista_imena.sort()
  print(', '.join(lista_imena))
