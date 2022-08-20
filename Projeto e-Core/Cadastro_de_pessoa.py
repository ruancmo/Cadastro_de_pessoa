def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar uma pessoa
    2. Listar pessoas cadastradas em ordem alfabetica
    3. Listar pessoas cadastradas em idade
    ''')

def cadastrar(pessoas):
    while True:
        classificacao = str()
        nome = str(input('Nome? '))
        idade = int(input('Idade? '))
        if 0 <= idade < 12:
            classificacao = 'crianca'
        elif 12 <= idade < 20:
            classificacao = 'adolescente'
        elif 20 <= idade < 65:
            classificacao = 'adulto'
        elif idade >= 65:
            classificacao = 'idoso'
        pessoas.append({'nome': nome, 'idade': idade,'classificacao': classificacao})
        resp = str(input('Quer continuar? [S/N] ')) #Permitir que as buscas continuem sem solicitar novamente o comando
        if resp in 'Ss':
            continue
        if resp in 'Nn':#Solicitar interrupcao do codigo
            break
        else:
            return

def ordem_alfabetica(pessoas): #Funcao para chamada das pessoas em ordem alfabetica
    pessoas_ordenado = sorted(pessoas, key=lambda obj: obj['nome']) #Foi utilizada uma key para buscar pelo nome para permitir ser de ordem alfabetica
    print('As pessoas cadastradas em ordem alfabetica são:')
    for pessoa in pessoas_ordenado:
        print(f"- {pessoa['nome']} tem {pessoa['idade']} anos.")

def idades(pessoas):
    idades_ordenado = sorted(pessoas, key=lambda obj: obj['idade']) #Mesma coisa do anterior só que para idade e sua posterior classificacao
    print('As pessoas cadastradas em ordem de idade são:')
    for pessoa in idades_ordenado:
        print(f"- {pessoa['nome']} tem {pessoa['idade']} anos e esta na faixa etaria de {pessoa['classificacao']}.")

def main():
    pessoas = []
    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            ordem_alfabetica(pessoas)
        elif opcao == 3:
            idades(pessoas)
        else:
            print('Opção inválida')

main()