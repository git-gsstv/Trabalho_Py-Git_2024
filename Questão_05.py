def periodoDia(hora):
    if hora >= 0 and hora < 12:
        return "Manhã"
    elif hora >= 12 and hora < 18:
        return "Tarde"
    elif hora >= 18 and hora <= 23:
        return "Noite"
    
hora = int(input("Digite o horário atual: "))
print(f'O período atual é: {periodoDia(hora)}')