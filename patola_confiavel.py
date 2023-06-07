from os import system
from colorama import init, Fore, Back, Style
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
                            return True
    except FileNotFoundError:
        return False

    return False


def buscar_usuario_cadastro(login):
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


def adicionar_dados_artista(login, emprego, nome_da_banda, integrantes_da_banda, genero_musical,bio, link):
    dado = {'login': login, 'emprego': emprego, 'nome_da_banda': nome_da_banda, 'integrantes_da_banda': integrantes_da_banda, 'genero_musical': genero_musical, 'bio': bio, 'link': link}
    dados.append(dado)
    arquivo_dados = open('dados.txt', 'a', encoding='utf8')
    arquivo_dados.write(str(dado) + '\n')
    arquivo_dados.close()


def adicionar_dados_contratante(login, nome_do_estabelecimento, nome_do_contratante, emprego,genero_musical, endereco):
    dado = {'login': login, 'nome_do_estabelecimento': nome_do_estabelecimento, 'nome_do_contratante': nome_do_contratante, 'emprego': emprego, 'genero_musical': genero_musical, 'endereco': endereco}
    arquivo_dados = open('dados.txt', 'a', encoding='utf8')
    arquivo_dados.write(str(dado) + '\n')
    arquivo_dados.close()


def obter_emprego_por_login(login):
    try:
        with open('dados.txt', 'r', encoding='utf-8') as arquivo_dados:
            for linha in arquivo_dados:
                dicionario = eval(linha)  # Converte a linha em um dicionário
                if dicionario.get('login') == login:
                    return dicionario.get('emprego')
    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")
    return None


def varredura_de_oportunidades(genero_musical_desejado, login):
    cont = 0
    emprego_usuario_logado = obter_emprego_por_login(login)
    if emprego_usuario_logado is None:
        print("Usuário não encontrado.")
        return

    try:
        with open('dados.txt', 'r', encoding='utf-8') as arquivo_dados:
            for linha in arquivo_dados:
                dicionario = eval(linha)  # Converte a linha em um dicionário
                genero_musical = dicionario.get('genero_musical')

                # Verificar se o usuário atual é um artista
                if emprego_usuario_logado == 'Artista' and genero_musical_desejado in genero_musical:
                    if dicionario.get('login') != login and dicionario.get('emprego') == 'Contratante':
                        cont += 1
                        for chave, valor in dicionario.items():
                            if chave not in ('login', 'emprego'):
                                print(Fore.MAGENTA + f'{chave}: {valor}')
                        print()

                # Verificar se o usuário atual é um contratante
                if emprego_usuario_logado == 'Contratante' and genero_musical_desejado in genero_musical:
                    if dicionario.get('login') != login and dicionario.get('emprego') == 'Artista':
                        cont += 1
                        for chave, valor in dicionario.items():
                            if chave not in ('login', 'emprego'):
                                print(Fore.MAGENTA + f'{chave}: {valor}')
                        print()

            if cont == 0:
                print(Fore.RED + "Nenhum resultado encontrado.")
                print()

    except FileNotFoundError:
        print(Fore.RED + "O arquivo 'dados.txt' não foi encontrado.")



print(Fore.GREEN + '''======================================================================
                    Bem-vindo ao PATOLA!
======================================================================''')
dados = []
while True:
    try:
        opcao = exibir_menu_principal()
        if opcao == 1:  # login
            login, senha = fazer_login()
            user = buscar_usuario(login, senha)
            if user == True:
                print()
                print(Fore.CYAN + 'Login realizado com sucesso!')
                print()
                sleep(1)
                while True:
                    try:
                        resposta = menu_pos_login()
                        sleep(1)
                        if resposta == 1:  # [1] Realizar varredura de oportunidades
                            genero_musical_desejado = input("Digite o gênero musical desejado: ").upper().strip()
                            login_usuario_logado = login
                            varredura_de_oportunidades(genero_musical_desejado, login_usuario_logado)
                        elif resposta == 2:  # [2] Alterar dados Cadastrados
                            print(Fore.RED + "PROVISÓRIO")
                            print(Fore.RED + "Alterando cadastros...\n")
                        elif resposta == 3:  # [3] Logout
                            break
                        else:
                            print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
                    except :
                        print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')

            else:
                print(Fore.RED + 'Usuário ou senha incorretos!')
                sleep(2)
        elif opcao == 2:  # Cadastro
            login, senha = fazer_login()
            user = buscar_usuario(login, senha)
            if login == "" or senha == "":
                print(Fore.RED + 'Usuário ou senha incorretos!\nCertifique-se de digitar um usuario e uma senha.')
                sleep(2)
                
            elif user == True:
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
                            emprego = "Artista"
                            nome_da_banda = input(Fore.YELLOW + 'Qual o nome da sua banda ?\t').title()

                            genero_musical = input(Fore.YELLOW + 'Qual genero musical sua banda toca?'+Fore.RED+'\nUtilize apenas vírgula(,) para listar os generos se for mais de um.\n\t').upper().strip().split(",")

                            integrantes_da_banda = input(Fore.YELLOW + 'Defina os integrantes da banda incluindo você:\t').title()

                            bio = input(Fore.YELLOW + 'Deixe uma breve biografia:\t')

                            link = input(Fore.YELLOW + 'Deixe um link com uma demo dos seus talentos:\t')

                            adicionar_dados_artista(login, emprego, nome_da_banda, integrantes_da_banda, genero_musical,bio, link)
                            break
                        elif emprego == "C":
                            emprego = "Contratante"
                            nome_do_contratante = input(Fore.YELLOW + 'Qual o seu nome ?\t').title()

                            nome_do_estabelecimento = input(
                                Fore.YELLOW + 'Qual o nome do seu estabelecimento ?\t').title()

                            genero_musical = input(
                                Fore.YELLOW + 'Qual o genero musical que você está procurando para o seu estabelecimento ?'+Fore.RED+'\nUtilize apenas vírgula(,) para listar os generos se for mais de um.\n\t').upper().strip().split(",")

                            endereco = input(Fore.YELLOW + 'Informe seu endereço:\t').title()

                            adicionar_dados_contratante(login, nome_do_estabelecimento, nome_do_contratante, emprego,genero_musical, endereco)
                            break
                        else:
                            print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [A] ou [C]''')

                    print(Fore.CYAN + 'Cadastro aprovado!')
                    sleep(1)

        elif opcao == 3:  # Sair
            print((Fore.BLUE + "Tas indo pra onde?\n\nJá tô com saudade..."))
            saida = input(Fore.BLUE + "Digite [S] para sim e [N] para  não:\t").upper()
            if saida == "N":
                pass
            elif saida == "S":
                print(Fore.GREEN + '''======================================================================
                Obrigado por usar o PATOLA!
    ======================================================================''')
                break
            else:
                print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [S] ou [N]''')
        else:
            print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
    except:
        print(Fore.RED + '''ATENÇÃO!\nFavor verificar o que foi digitado, só são aceitas as seguintes respostas: [1], [2] ou [3]''')
