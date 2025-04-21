# EXERCÍCIO DE CALCULAR A MÉDIA  DIZER SE O ALUNOS ESTÁ APROVADO 

# APENAS UMA FUNÇÃO PARA SEPARAR SEÇÕES DO C[ODIGO]
def lin():
    print("-" * 30)

# cada comando input pede para o usuário digitar uma nota e armazena isso na sua respectiva variável 

n1 = float(input("Digite a nota da primeira avaliação: "))

n2 = float(input("Digite a nota da segunda avaliação: "))


n3 = float(input("Digite a nota da terceira avaliação: "))


n4 = float(input("Digite a nota da quarta avaliação: "))

# AQUI É O CÁLCULO DA MÉDIA PROPRIAMENTE DITO
m = (n1 + n2 + n3 + n4) / 4

print("A média deste aluno é", {m})

# ESSA PARTE DO CÓDIGO DIZ SE O ALUNO ATINGIU A MÉDIA PARA SER APROVADO OU NÃO
if m>= 6:
    print("Aluno Aprovado!")
else:
    print("Aluno reprovado!")

lin()