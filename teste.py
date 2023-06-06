from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep
init(autoreset=True)


def exibir_menu_principal():
    print(Fore.GREEN + '''Opções:
[1] Login
[2] Cadastro
[3] Sair
''')
    opcao = int(input('Escolha a opção desejada:\t'))
    return opcao


def fazer_login():
    login = input('Nome de usuário:\t')
    senha = stdiomask.getpass(prompt='Senha:\t', mask='$')
    return login, senha


def buscar_usuario(login, senha):
    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo_usuarios:
            for linha in arquivo_usuarios:
                linha = linha.strip()
                if linha:
                    usuario = linha.split()
                    if len(usuario) == 2:
                        username = usuario[0]
                        password = usuario[1]
                        if login == username and senha == password:
                            return {'login': username, 'senha': password}
    except FileNotFoundError:
        return None

    return None


def buscar_usuario_para_cadastro(login):
    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo_usuarios:
            for linha in arquivo_usuarios:
                linha = linha.strip()
                if linha:
                    usuario = linha.split()
                    if len(usuario) == 2:
                        username = usuario[0]
                        if login == username:
                            return True
    except FileNotFoundError:
        return False

    return False


def menu_pos_login():
    print(Fore.GREEN + '''Opções:
[1] Realizar varredura de oportunidades
[2] Alterar dados Cadastrados
[3] Logout
''')
    resposta = int(input('Escolha a opção desejada:\t'))
    return resposta


def artistas_indecisos():
    print()


def contratantes_indecisos():
    print()


def adicionar_dados_artista(emprego, genero_musical, integrantes_da_banda, nome_da_banda, bio, link):
    dado = {'emprego': emprego, 'genero_musical': genero_musical, 'integrantes_da_banda': integrantes_da_banda,
            'nome_da_banda': nome_da_banda, 'bio': bio, 'link': link}
    dados.append(dado)
    arquivo_dados = open('dados.txt', 'a', encoding='utf8')
    arquivo_dados.write(str(dado) + '\n')
    arquivo_dados.close()


def adicionar_dados_contratante(emprego, genero_musical, nome_do_estabelecimento, nome_do_contratante, endereco):
    dado = {'emprego': emprego, 'genero_musical': genero_musical, 'nome_do_estabelecimento': nome_do_estabelecimento,
            'nome_do_contratante': nome_do_contratante, 'endereco': endereco}
    dados.append(dado)
    arquivo_dados = open('dados.txt', 'a', encoding='utf8')
    arquivo_dados.write(str(dado) + '\n')
    arquivo_dados.close()


def varredura_de_oportunidades(usuario_atual):
    emprego_usuario_atual = usuario_atual['emprego']
    genero_musical_usuario_atual = usuario_atual['genero_musical']
    oportunidades = []
    with open('dados.txt', 'r', encoding='utf-8') as arquivo_dados:
        for linha in arquivo_dados:
            linha = linha.strip()
            if linha:
                dados_usuario = eval(linha)
                if dados_usuario['emprego'] == 'C' and dados_usuario['genero_musical'] == genero_musical_usuario_atual:
                    oportunidades.append(dados_usuario)
    return oportunidades


print(Fore.GREEN + '''======================================================================
                    Bem-vindo ao PATOLA!
======================================================================''')
dados = []
while True:
    try:
        opcao = exibir_menu_principal()
        if opcao == 1:  # login
            login, senha = fazer_login()
            usuario_atual = buscar_usuario(login, senha)
            if usuario_atual:
                print()
                print(Fore.CYAN + 'Login realizado com sucesso!')
                print()
                sleep(1)
                while True:
                    resposta = menu_pos_login()
                    sleep(2)
                    if resposta == 1:  # [1] Realizar varredura de oportunidades
                        usuarios_encontrados = varredura_de_oportunidades(usuario_atual)
                        if usuarios_encontrados:
                            print(Fore.GREEN + 'Oportunidades encontradas:')
                            for usuario in usuarios_encontrados:
                                print(usuario)
                        else:
                            print(Fore.YELLOW + 'Nenhuma oportunidade encontrada.')
                        print()
                    elif resposta == 2:  # [2] Alterar dados Cadastrados
                        print(Fore.RED + 'PROVISÓRIO')
                        print(Fore.RED + 'Alterando cadastros...')
                        print()
                    elif resposta == 3:  # [3] Logout
                        break
                    else:
                        sleep(2)
                        print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')

            else:
                print(Fore.RED + 'Usuário ou senha incorretos!')
                sleep(2)
        elif opcao == 2:  # Cadastro
            login, senha = fazer_login()
            user = buscar_usuario_para_cadastro(login)
            if user == True:
                print()
                print(Fore.RED + 'O Usuário já existe!')
                print()
                sleep(2)
            else:
                with open('usuarios.txt', 'a+', encoding='Utf_8', newline='') as arquivo_usuarios:
                    arquivo_usuarios.writelines(f'{login} {senha}\n')
                    while True:
                        emprego = input(Fore.YELLOW + 'Você é [A] artista ou [C] contratante?\t').upper()
                        if emprego == "A":
                            nome_da_banda = input(Fore.YELLOW + 'Qual o nome da sua banda ?\t')
                            genero_musical = input(Fore.YELLOW + 'Qual genero musical sua banda toca?\t')
                            integrantes_da_banda = input(Fore.YELLOW + 'Defina os integrantes da banda incluindo você:\t')
                            bio = input(Fore.YELLOW + 'Deixe uma breve biografia:\t')
                            link = input(Fore.YELLOW + 'Insira um link de uma musica sua:\t')
                            adicionar_dados_artista(emprego, genero_musical, integrantes_da_banda, nome_da_banda, bio, link)
                            break
                        elif emprego == "C":
                            nome_do_estabelecimento = input(Fore.YELLOW + 'Qual o nome do seu estabelecimento ?\t')
                            nome_do_contratante = input(Fore.YELLOW + 'Qual o seu nome?\t')
                            endereco = input(Fore.YELLOW + 'Insira o endereço do seu estabelecimento:\t')
                            adicionar_dados_contratante(emprego, genero_musical, nome_do_estabelecimento, nome_do_contratante, endereco)
                            break
                        else:
                            print(Fore.RED + 'Resposta inválida, digite A para artista ou C para contratante')
                            sleep(1)
                print()
                print(Fore.CYAN + 'Cadastro realizado com sucesso!')
                print()
                sleep(2)
        elif opcao == 3:  # Sair
            break
        else:
            sleep(2)
            print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
    except ValueError:
        sleep(2)
        print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
