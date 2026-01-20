from nota import adicionar_nota, mostrar_resultado

def menu():
    print("\n=== Sistemas de Notas ===")
    print("1 - Adicionar nota")
    print("2 - Mostrar resultado")
    print("0 - Sair\n")

def main():
    notas = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_nota(notas)
        
        elif opcao == "2":
            mostrar_resultado(notas)

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente")

if __name__ == "__main__":
            main()
