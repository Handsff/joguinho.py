#Tentar criar um joguinho de acerto ou erro

# Numeros pares acerta / numeros impares erra

n = int(input('Numero: '))

if n == 2 or n == 4 or n == 6 or n == 8 or n == 10:
  print('Acertou')
elif n == 1 or n == 3 or n == 5 or n == 7 or n == 9:
  print('errou')
else:
  print('Apenas de 1 ao 10')
