def situacao(media):
    if media >= 6:
        return "aprovado(a)"
    else:
        return "reprovado(a)"
    
nome = input("Digite o nome: ")
materia = input("Digite a matéria que você deseja calcular a média: ")
n1 = float(input("Digite a primeira nota nessa matéria: "))
n2 = float(input("Digite a segunda nota nessa matéria: "))
media = (n1+n2)/2
print(f'A média é: {media}')
print(f'{nome} está {situacao(media)} na disciplina {materia}')