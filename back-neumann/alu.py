def ALU(acc, r_ent):
    num1 = int(acc, 2)
    num2 = int(r_ent, 2)
    suma = num1 + num2
    return format(suma, '08b')