Instruções:
Desenvolva uma aplicação em qualquer linguagem de programação, de acordo com os requisitos abaixo. 
Não é necessário interface gráfica, no entanto deve haver uma forma de entrada de dados e verificação das saídas 
correspondentes, que não envolva inserção manual de dados no código fonte.
Requisitos:
A funcionalidade do programa é o armazenamento de dados cadastrais de pessoas. 
Devem constar os seguintes dados no cadastro: 
Nome e idade.
Deve ser possível cadastrar / adicionar uma nova pessoa.
Deve ser possível exibir uma lista de pessoas cadastradas, ordenada por idade (menor para maior) e 
nome (alfabética crescente).
Deve ser possível categorizar as pessoas cadastradas por idade, de acordo com os critérios: 
0 a 12 anos => Criança, 12 até 19 anos => Adolescente, 20 até 65 => Adulto, 65 ou mais => Idoso.
------------------------------------------------------------------------------------------------
Passo a passo de como utilizar o código:

1 - Abra o arquivo cadastro_de_pessoas.py;
2 - Ao executar o código será exibido um menu com três opções: 
a) Cadastrar pessoas;
b) Listar pessoas cadastradas em ordem alfabética;
c) Listar pessoas cadastradas em idade.
3 - Escolhendo a opção 1 será solicitado o nome da pessoa a ser cadastrada em seguida a idade e por último a opção 
se deseja continuar com o cadastro de mais pessoas, caso a resposta seja sim, será solicitado novas entradas de nome
e idade, caso não será exibido o menu novamente;
4 - Selecionando a opção 2 será exibido a lista de pessoas cadastradas em ordem alfabética e sua respectiva idade;
5 - Selecionando a opção 3 será exibido a lista de pessoas cadastradas em ordem de idade (menor para maior) e sua
respectiva classificação de faixa etária.