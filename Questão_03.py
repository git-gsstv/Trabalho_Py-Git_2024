def contagemCaracteres(frase):
    semEspacos = frase.replace(" ", "")
    numeroCaracteres = len(semEspacos)
    return numeroCaracteres

frase = input("Digite uma frase: ")
print("Sua frase possui", contagemCaracteres(frase), "caracteres.")