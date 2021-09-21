#Longest Word: Have the function LongestWord(sen) take the sen parameter being passed and 
# return the longest word in the string. If there are two or more words that are the same length, 
# return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 
# Words may also contain numbers, for example "Hello world123 567"

def LongestWord(sen): 

  words = {}         
  word = ""
  length = 0
  for i in range(0, len(sen)):  # Recorremos el string que se nos pasa.
    if sen[i].isalpha():        # Comprobamos si es una letra.
      word += sen[i]            # Vamos formando la palabra conforme se encuentra letras.
      length += 1               # Y, con cada letra que forma, aumenta la longitud de ésta.
      if i == len(sen)-1:       # Si ha llegado al final del string, añade al diccionario 
        if length > 0:          # la palabra en cuestión junto con su longitud
          words[word] = length
      
    if not sen[i].isalpha():    # Si se encuentra con un espacio,
      words[word] = length      # añade la palabra en cuestión junto con su longitud, y vuelve a poner a 0 length 
      length = 0                # y word para continuar contando las palabras posteriores.
      word = ""
  length =0                     # Pone a 0 el contador length una vez el for termina, para reutilizarlo ahora
  for key, value in words.items():  # Recorre el diccionario, viendo sus claves y valores
    if length < value:          # Si la longitud de las palabras del diccionario es mayor que length (inicialmente 0),
      length = value            # length pasa a tomar como valor esa longitud
      sen = key                 # Y sen pasa a ser esa palabra más larga

  return sen                    # Una vez examinado todo el diccionario, devuelve la palabra más larga
    
# keep this function call here  
print(LongestWord(input()))