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
