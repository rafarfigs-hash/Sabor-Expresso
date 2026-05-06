import os

restaurantes = ['Pizzaria Figueredo', 'Sushi Ramos' , 'Churrascaria Siqueira']

#funcao exibir nome
def exibir_nome_do_programa():
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

#funcao exibir opções
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#funcao exibir subtitulo
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

#função voltar ao menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

#funcao opção invalida(opção x)
def opcao_invalida():
    print('\nOpção invalida')
    voltar_ao_menu_principal()

#funcao cadastrar novo restaurante(opção 1)
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    novo_restaurante = str(input("Digite o nome do restaurante: "))
    restaurantes.append(novo_restaurante)
    print(f'O restaurante cadastrado foi: {novo_restaurante}')
    voltar_ao_menu_principal()

# funcao listar restaurantes(opção 2)
def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

# funcao ativar restaurante(opção 3)


#funcao finalizar app(opção 4)
def finalizar_app(): #na opção 4
    exibir_subtitulo('Finalizando o app')

#funcao escolher opcao

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Você escolheu a opção "Ativar restaurante"\n')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida

#tornar esse aquivo o principal do código

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()