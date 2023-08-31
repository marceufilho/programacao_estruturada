def salario (valor_hora, num_horas):
    return valor_hora * num_horas
def operacoes (num_um, num_dois, num_tres):
    print((2 * num_um) * (num_dois / 2), "\n",(3 * num_um) + num_tres, "\n", num_tres ** 2)
def operacoes_dois (num_um, num_dois, num_tres):
    return (2 * num_um) * (num_dois / 2),(3 * num_um) + num_tres, num_tres ** 2 
def bissesto (ano):
   return (ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0)


