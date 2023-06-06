from os import system
from colorama import init, Fore, Back, Style
import stdiomask
import json
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
        with open('usuarios.json', 'r', encoding='utf-8') as arquivo_usuarios:
            usuarios = json.load(arquivo_usuarios)
            usuario = usuarios.get(login)
            if usuario and usuario['senha'] == senha:
                return {'login': login, 'senha': senha}
    except FileNotFoundError:
        return None

    return None


def buscar_usuario_para_cadastro(login):
    try:
        with open('usuarios.json', 'r', encoding='utf-8') as arquivo_usuarios:
            usuarios = json.load(arquivo_usuarios)
            if login in usuarios:
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
    with open('dados.json', 'a', encoding='utf8') as arquivo_dados:
        json.dump(dado, arquivo_dados)
        arquivo_dados.write('\n')


def adicionar_dados_contratante(emprego, genero_musical, nome_do_estabelecimento, nome_do_contratante, endereco):
    dado = {'emprego': emprego, 'genero_musical': genero_musical, 'nome_do_estabelecimento': nome_do_estabelecimento,
            'nome_do_contratante': nome_do_contratante, 'endereco': endereco}
    dados.append(dado)
    with open('dados.json', 'a', encoding='utf8') as arquivo_dados:
        json.dump(dado, arquivo_dados)
        arquivo_dados.write('\n')


def varredura_de_oportunidades(usuario_atual):
    emprego_usuario_atual = usuario_atual['emprego']
    genero_musical_usuario_atual = usuario_atual['genero_musical']
    oportunidades = []
    with open('dados.json', 'r', encoding='utf-8') as arquivo_dados:
        for linha in arquivo_dados:
            dados_usuario = json.loads(linha)
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
                with open('usuarios.json', 'a+', encoding='utf-8') as arquivo_usuarios:
                    usuarios = {}
                    if arquivo_usuarios.tell() != 0:
                        arquivo_usuarios.seek(0)
                        usuarios = json.load(arquivo_usuarios)
                    usuarios[login] = {'senha': senha}
                    arquivo_usuarios.seek(0)
                    json.dump(usuarios, arquivo_usuarios)
                    arquivo_usuarios.truncate()
                    while True:
                        emprego = input(Fore.YELLOW + 'Você é [A] artista ou [C] contratante?\t').upper()
                        if emprego == "A":
                            nome_da_banda = input(Fore.YELLOW + 'Qual o nome da sua banda ?\t')
                            genero_musical = input(Fore.YELLOW + 'Qual gênero musical sua banda toca?\t')
                            integrantes_da_banda = input(Fore.YELLOW + 'Defina os integrantes da banda incluindo você:\t')
                            bio = input(Fore.YELLOW + 'Deixe uma breve biografia:\t')
                            link = input(Fore.YELLOW + 'Insira um link de uma música sua:\t')
                            adicionar_dados_artista(emprego, genero_musical, integrantes_da_banda, nome_da_banda, bio, link)
                            break
                        elif emprego == "C":
                            nome_do_estabelecimento = input(Fore.YELLOW + 'Qual o nome do seu estabelecimento ?\t')
                            nome_do_contratante = input(Fore.YELLOW + 'Qual o seu nome?\t')
                            endereco = input(Fore.YELLOW + 'Qual o endereço do estabelecimento?\t')
                            adicionar_dados_contratante(emprego, genero_musical, nome_do_estabelecimento, nome_do_contratante, endereco)
                            break
                        else:
                            sleep(2)
                            print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [A] ou [C]''')
                            print()
                    print()
                    print(Fore.CYAN + 'Cadastro realizado com sucesso!')
                    print()
        elif opcao == 3:  # Sair
            break
        else:
            sleep(2)
            print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
            print()
    except ValueError:
        sleep(2)
        print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
        print()
    except KeyboardInterrupt:
        print(Fore.RED + '\n\nPrograma interrompido pelo usuário!')
        break

print(Fore.GREEN + 'Obrigado por utilizar o PATOLA!')
print(Fore.GREEN + 'Até mais!')
