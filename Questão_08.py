def adicao(p,g):
    return p + g
def subtracao(p,g):
    return p - g
def multiplicacao(p,g):
    return p * g
def divisao(p,g):
    return p / g


p = int(input("Digite um número: "))
g = int(input("Agora digite outro número: "))
print(f'A soma desses números é: {adicao(p,g)}')
print(f'A diferença entre esses números é: {subtracao(p,g)}')
print(f'O produto desses números resulta em: {multiplicacao(p,g)}')
print(f'A divisão desses números equivale a: {divisao(p,g)}')