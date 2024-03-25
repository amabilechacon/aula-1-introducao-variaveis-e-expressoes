"""
#### Exercício

Dado um número digitado pelo usuário, imprima seu antecessor, seu sucessor, seu dobro e sua raiz quadrada

Exemplo:
Digite seu número: 4

Resposta:

O antecessor do número 4 é 3.
O sucessor do número 4 é 5.
O dobro do número 4 é 8.
A raiz quadrada do número 4 é 2.
"""
numero=int(input('digite seu numero:'))

antecessor=numero-1
sucessor=numero+1
dobro=numero*2
raiz=numero**(1/2)

print(f'0 antecessor do numero {numero} é {antecessor}')
print(f'0 sucessor do numero {numero} é {sucessor}')
print(f'O dobro do número {numero} é {dobro}')
print(f'A raiz do numero{numero} é {raiz}')

print(f'O antecessor do número {numero} é {antecessor}')
