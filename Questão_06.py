def tituloEleitor(idade):
    if idade >= 16:
        return "você pode emitir seu título de eleitor(a)."
    else:
        return "você não está apto(a) a obter seu título de eleitor(a)."

nome = input("Digite seu nome: ")    
idade = int(input("Digite sua idade: "))
print(f'{nome},',tituloEleitor(idade))