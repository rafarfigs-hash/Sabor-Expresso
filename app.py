import os

restaurantes = [{'nome':'Figueredo Sushi','categoria':'Italiana', 'ativo':True},
                {'nome':'Ramos Pizza','categoria':'Italiana', 'ativo':False},
                {'nome':'Churrascaria Siqueira','categoria':'Churrascaria', 'ativo':False}]

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
    print('3. Alterar restaurante')
    print('4. Sair\n')

#funcao exibir subtitulo
def exibir_subtitulo(texto):
    linha = '*' * (len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print (linha)
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
    categoria = input(f'Digite o nome da categoria do restaurante {novo_restaurante}: ')
    dados_do_restaurante = {'nome':novo_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {novo_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

# funcao listar restaurantes(opção 2)
def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    print(f'{"Nome do restaurante".ljust(27)} | {"Categoria".ljust(25)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(25)} | {categoria.ljust(25)} | {ativo}')

    voltar_ao_menu_principal()

# funcao ativar restaurante(opção 3)
def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!!' if restaurante ['ativo'] else f'O restaurante foi desativado com sucesso!'
            print(mensagem)
        if not restaurante_encontrado:
            print('O restaurante nao foi encontrado!')

    voltar_ao_menu_principal()

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
            alterar_estado_restaurante()
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

