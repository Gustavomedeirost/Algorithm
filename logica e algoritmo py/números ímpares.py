#Objetivo: imprimir todos os números ímpares entre 1 e 250.
"""
passo a passo:

1. iniciar um loop: Loope for para percorrer todos os números de 1 a 250.

2. Verificar se o número é ímpar: Dentro do loop, usar o operador de modulo % para verificar se o número não é divisível por 2 (i % 2 != 0).

3. Imprimir o número ímpar: Se o número for ímpar, imprima-o.

"""

for i in range(1,251):
    if i % 2 != 0:
        print(i)
