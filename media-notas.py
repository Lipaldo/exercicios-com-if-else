
# cada comando input pede para o usuário digitar uma nota e armazena isso na sua respectiva variável
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda Nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

m = (n1 + n2 + n3 + n4) / 4

print(f"A média deste aluno é{m: .2f}")

if m>= 7:
    print("Aprovado!")
else:
    print("Reprovado!")