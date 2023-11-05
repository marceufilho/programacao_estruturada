import random 
import json
from datetime import datetime as dp
import locale

def lanca_dado():
    return random.randint(1, 6)


def armazena_dados_lançdos(lado, arrLados):
    arrLados[lado - 1] += 1
    return arrLados


def qntd_lancado(qntd_lancamentos):
    dado = 0
    arrLados = [0] * 6
    for i in range (qntd_lancamentos):
        dado = lanca_dado()
        armazena_dados_lançdos(dado, arrLados)
    return arrLados


def mostrador(arrLados):
    print(f"Após lancar o dado {sum(arrLados)} vezes, tivemos resultados")
    for i in range (1,7):
        print(f"Foram lançados {arrLados[i - 1]} vezes de lado {i}")


def lancamento_de_dados():
    arrLados = qntd_lancado(100)
    mostrador(arrLados)


def read_dados_alunos():
    dados_alunos = {}
    matricula = 1
    while(matricula != ""):
        matricula = input("Digite a matricula do aluno(para sair do prgram aperte enter):")
        if matricula == "": break
        nome = input("Digite o nome do aluno:")
        email = input("Digite o email do aluno:")
        dados_alunos.update({matricula : {}})
        dados_alunos[matricula].update({"nome": nome,"Email" : email})
    return dados_alunos


def writes_json_file():
    dados_alunos = read_dados_alunos()
    with open("alunos_dados.json", "w") as file:
        json.dump(dados_alunos, file, indent = 4)


def testa_formato(data, formato_data):
    booleano = True
    try:
        dp.strptime(data,formato_data)
    except ValueError:
        booleano = False
    return booleano


def reads_date(data):
    locale.setlocale(locale.LC_ALL, 'pt_BR')
    formato_data = "%d/%m/%y"
    while testa_formato(data, formato_data) != True:
       data = input("Escreva uma nova data com formato dd/mm/aa:")
    data_formatada = dp.strptime(data, formato_data)
    print(data_formatada.strftime("%d de %B de %Y"))
    








    


