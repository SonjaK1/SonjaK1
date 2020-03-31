def obrnuti_tekst(paragraf):
  recenice = paragraf.split('. ')
  recenice[-1] = recenice[-1].strip('.')
  recenice.reverse()
  recenice[-1] += '.'
  print('. '.join(recenice))
