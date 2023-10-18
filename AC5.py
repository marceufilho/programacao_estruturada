def serie (n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print("")

def qntd_digitos(numero):
    print(len(str(numero)))

def divisao():
    try:
        numero_um = int(input("Digite um numero inteiro: "))
        numero_dois = int(input("digite o segundo numero inteiro para divisão: "))
        divide = numero_um / numero_dois
    except ValueError:
        print("Você não digitou um inteiro...") 
        divide = ""
    except ZeroDivisionError:
        print("o segundo numero da divisão é zero e divisão por zero não é definido.")
        divide = ""
    finally:
        print(divide)


