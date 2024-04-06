#exercício 16
area = int(input("tamanho em metros quadrados da área a ser pintada: "))

litros = area/3
latas = litros/18
preco_total = latas * 80
print(f"a quantidade em litros é de {litros}")
print(f"o número de latas é de {latas}")
print(f"o valor total é de {preco_total}")

#exercício 17
area = float(input("tamanho em metros quadrados da área a ser pintada: "))

litros = area/6
latas = litros/18
somente_preco_latas = latas * 80
galoes = litros/3.6
somente_preco_galoes = galoes * 25
latas_misto = litros//18
galoes_misto = ((litros + (litros * 0.1))-(latas_misto*18))//3.6
preco_galoes_misto = galoes_misto * 25
preco_total = somente_preco_latas + preco_galoes_misto
print(f"a quantidade em litros é de {litros}")
print(f"o número de somente latas é de {latas}")
print(f"o preço de somente latas é de {somente_preco_latas}")
print(f"o número de somente galões é de {galoes}")
print(f"o preço de somente latas é de {somente_preco_galoes}")
print(f"o número de latas é de {latas_misto} mais {galoes_misto} galões")
print(f"o valor total é de {preco_total}")

#exercício 3
def soma(num1, num2, num3):
    return num1 + num2 + num3

print(f"a soma é de {soma(5,5,5)}")
