from src.service.service_user import ServiceUser

def main():
    service = ServiceUser()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar usuário")
        print("2 - Remover usuário")
        print("3 - Atualizar usuário")
        print("4 - Exibir usuário por nome")
        print("5 - Exibir todos usuários")
        print("6 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            name = input("Digite o nome do usuário: ")
            job = input("Digite o trabalho do usuário: ")
            resultado = service.add_user(name, job)
            print(resultado)

        elif opcao == "2":
            name = input("Digite o nome do usuário para remover: ")
            resultado = service.remove_user(name)
            print(resultado)

        elif opcao == "3":
            name = input("Digite o nome do usuário que deseja atualizar: ")
            new_job = input("Digite o novo Job do usuário: ")
            resultado = service.update_user(name, new_job)
            print(resultado)

        elif opcao == "4":
            # Exibir usuário por nome
            name = input("Digite o nome do usuário para exibir: ")
            resultado = service.get_user_by_name(name)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"Nome: {resultado.name}, Job: {resultado.job}")

        elif opcao == "5":
            if service.store.bd:
                print("\nLista de usuários:")
                for i, user in enumerate(service.store.bd, start=1):
                    print(f"{i}. Nome: {user.name}, Job: {user.job}")
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "6":
            print("Sua sessão foi encerrada.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
main()
