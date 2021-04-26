# Sorteando os números
from random import sample,seed

numeros_sorteados = sample(range(1, 61), 6)
numeros_sorteados = sorted(numeros_sorteados)

# registrando chute
chute = []

for i in range(1, 7):
  num = 0
  while num < 1 or num > 60 or num in chute:
    num = int(input(f'{i}º número - Digite um número entre 1 e 60 '))
  chute.append(num)

chute = sorted(chute)
print('Seu chute é', chute)

# Conferindo resultados e acertos
import numpy as np
resultado = np.in1d(chute, numeros_sorteados)
acertos = len(np.intersect1d(chute, numeros_sorteados))

# Resultados
print('Você ganhou na Mega') if resultado.all() else print(f'Você perdeu e acertou {acertos} número(s).')
print('\nSorteio   ', numeros_sorteados)
print('Seu chute ', chute)