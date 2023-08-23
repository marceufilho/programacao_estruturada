a = float(input("Escreva o A da equação de segundo grau: Formato: ax^2 + bx + c\n"))
b = float(input("escreva o B:\n"))
c = float(input("escreva o C:\n"))
x_um = (-b + (4 * a * c) ** (1/2))/ (2 * a)
x_dois = (-b - (4 * a * c) ** (1/2))/ (2 * a)
print ("x1 =", x_um)
print("x2 = ", x_dois)

print("-" * 30)

ano = int(input("digite um ano:\n"))
bissesto = ((not(ano % 100)) and (not(ano % 400))) or (not(ano % 4))
print(bissesto)