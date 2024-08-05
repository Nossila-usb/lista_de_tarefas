# lista nomes
tarefas_de_malhacao = []
tarefas_domestica = []

# inicio de loop
while True:
    # MENU
    print('1 - lista_malhacao.')
    print('2 - exibir_malhacao.')
    print('3 - lista_domestica.')
    print('4 - exibir_donmestica.')
    print('5 - encerrra programa.')

    # opcao do usuario
    opcao = input('opcao do usuario')

     # verificacao a opcao escolhida
    match opcao:
        case '1':
            lista_malhacao = input('lista de tarefas_malhacao: ')
            tarefas_de_malhacao.append(lista_malhacao)
            print(f'{lista_malhacao} inserido com sucesso.')
            continue
        case '2':
            print('\nLISTA DE MALHACAO:\n')
            for nome in tarefas_de_malhacao:
                print(tarefas_de_malhacao)
                continue
        case '3':
            lista_domestica = input('insira tarefa_domestica: ')
            tarefas_domestica.append(lista_domestica)
            print(f'{lista_domestica} inserido com sucesso.')
            continue
        case '4':
            print('\nLISTA DOMESTICA:\n')
            for nome in tarefas_domestica:
                print(tarefas_domestica)
                continue
        case '5':
            print('Programa encerrado.')
            break 
        case _:
            print('opcao invalida')

        
