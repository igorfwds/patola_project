# Manual do Usuário - PATOLA

Bem-vindo ao Manual do Usuário do PATOLA! - Sistema de Oportunidades Musicais

Este manual fornecerá instruções detalhadas sobre como usar o aplicativo PATOLA para aproveitar ao máximo suas funcionalidades. Siga as etapas abaixo para começar.

## Índice

1. [Visão Geral](#visão-geral)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Uso](#uso)
   - [Login](#login)
   - [Cadastro](#cadastro)
   - [Varredura de Oportunidades](#varredura-de-oportunidades)
   - [Alterar Dados Cadastrados](#alterar-dados-cadastrados)
   - [Logout](#logout)
5. [Participantes do projeto](#Participantes-do-projeto)


## Visão Geral

O PATOLA é um aplicativo desenvolvido para artistas e contratantes no setor musical. 

Ele permite que os artistas se cadastrem e encontrem oportunidades musicais com base em seus gêneros musicais preferidos.

Os contratantes podem se cadastrar e buscar por artistas de diferentes gêneros para contratação em seus estabelecimentos. 

O aplicativo oferece uma interface fácil de usar com opções claras e orientações passo a passo.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `colorama`
- Biblioteca `stdiomask`

## Instalação

1. Certifique-se de ter o Python 3 instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/patola.git
   ```

3. Acesse o diretório do projeto:

   ```bash
   cd patola
   ```

4. Crie e ative um ambiente virtual (opcional):

   ```bash
   python -m venv env        # criar ambiente virtual
   source env/bin/activate  # ativar ambiente virtual (Linux/Mac)
   env\Scripts\activate     # ativar ambiente virtual (Windows)
   ```

5. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Login

1. Após a instalação, execute o arquivo `patola.py`:

   ```bash
   python patola.py
   ```

2. No menu principal, escolha a opção `1 - Login`.

3. Digite seu nome de usuário e senha quando solicitado.

4. Se as credenciais estiverem corretas, você será autenticado com sucesso e entrará no menu pós-login.

### Cadastro

1. No menu principal, escolha a opção `2 - Cadastro`.

2. Digite um nome de usuário e senha para criar sua conta.

3. Siga as instruções fornecidas para preencher os detalhes do seu perfil. As informações solicitadas podem variar dependendo se você é um artista ou um contratante.

### Varredura de Oportunidades

1. Após o login, no menu pós-login, escolha a opção `1 - Realizar varredura de oportunidades`.

2. Você será solicitado a escolher um gênero musical entre as opções disponíveis.

3. Digite

 o número correspondente ao gênero musical desejado.

4. O aplicativo realizará uma varredura e exibirá as oportunidades disponíveis para o gênero selecionado.

### Alterar Dados Cadastrados

1. Após o login, no menu pós-login, escolha a opção `2 - Alterar dados cadastrados`.

2. Siga as instruções fornecidas para alterar os detalhes do seu perfil, como gêneros musicais, biografia, link da demo, etc.

### Logout

1. Após o login, no menu pós-login, escolha a opção `3 - Logout`.

2. Você será desconectado do aplicativo e retornará ao menu principal.

## Participantes do projeto


- Ana Beatriz Miccuci
- Clara B. Sobral
- Guilherme Cardozo
- Henrique Magalhães
- Igor "Mata" Wanderley
- João Victor Ferraz
- Júlia Falcão
- Lara Vasconcelos
- Maria Luiza "Lulis" Nunes
- Rodrigo Bezerra
