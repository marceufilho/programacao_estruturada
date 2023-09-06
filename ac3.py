"""
AC3 Programação Estruturada
Marceu Filho
"""
# 1
def exibe_salarios (salario, aumento, novo_salario):
    print("O salario era:", salario) 
    print("o percentual de aumento foi:", (aumento/salario) * 100, "%")
    print("o Aumento foi de:", aumento )
    print("o novo salario é: ", novo_salario)

def aumento_salario (salario):
    if salario <= 280:
        aumento = salario * 0.2
        novo_salario = salario * 1.2
        exibe_salarios (salario, aumento, novo_salario)
    elif 280 < salario <= 700:
        aumento = salario * 0.15
        novo_salario = salario * 1.15
        exibe_salarios (salario, aumento, novo_salario)
    elif 700 < salario <= 1500:
        aumento = salario * 0.1
        novo_salario = salario * 1.1
        exibe_salarios (salario, aumento, novo_salario)
    else:
        aumento = salario * 0.05
        novo_salario = salario * 1.05
        exibe_salarios(salario, aumento, novo_salario)

#2

def dia_da_semana(dia):
    if dia == 1:
        return "domingo"
    elif dia == 2:
        return "segunda"
    elif dia == 3:
        return "terça"
    elif dia == 4:
        return "quarta"
    elif dia == 5:
        return "quinta"
    elif dia == 6:
        return "sexta"
    elif dia == 7:
        return "sabado"
    return "valor invalido"   

#3
     
def resolucao_eq2(a,b,c):
    if a == 0:
        return print("a equação não é de segundo grau")
    if (b ** 2 - 4 * a * c) < 0:
        return print("A equação não tem raizes reais")
    if (b ** 2 - 4 * a * c) == 0:
        x = -b/(2*a)
        return print("A equação só tem uma raiz que é", x)
    x1 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    return print ("O delta é positivo e x1 é:", x1, "e x2 é", x2)


