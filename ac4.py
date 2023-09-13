def e_primo(num, i = 2):
    if num == 0 or num == 1:
        return False
    
    if num == i:
        return True
    
    if num % i == 0:
        print("1", end = " ")
        for div in range (i, num, 1):
            if num % div == 0:
                print (div, end = " ")
        print(num)
        return False
    return e_primo(num, i + 1)

if e_primo(35):
    print ("é primo")

def parcelamento_divida(divida):
    juros = 10
    print (" Valor dos juros", "Valor total ", "Quantidade de Parcelas", "Valor da Parcela")
    print (0, divida, 1, divida )

    for count in range (3, 13, 3):
        print (juros,"%", divida * (1 + (juros / 100)) , count , (divida * (1 + (juros / 100))) / count)
        juros += 5


def intervalo ():
    num = int(input("escreva um numero"))
    intervalo_0_25 = 0
    intervalo_26_50 = 0
    intervalo_51_75 = 0
    intervalo_76_100 = 0
    while (num > 0):
        if num <= 25:
            intervalo_0_25 += 1
        if num > 25 and num <= 50:
            intervalo_26_50 += 1
        if num > 50 and num <= 75:
            intervalo_51_75 += 1
        if num > 75 and num <= 100:
            intervalo_76_100 += 1
        num = int(input("escreva um novo numero:"))
    print("o primeiro intervalo teve:", intervalo_0_25,)
    print("O segundo intervalo teve:", intervalo_26_50)
    print("o terceiro intervalo teve:", intervalo_51_75)
    print("o quarto intervalo teve:", intervalo_76_100)


    

        
    


