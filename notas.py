def adicionar_nota(notas):
    try:
        nota = float(input("Digite a nota (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            print("Nota adicionada com sucesso.")
        else:
            print("Nota inválida.")
    except ValueError:
        print("Digite um número válido.")

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)
    