materia = str(input("Matéria: "))
nome = str(input("Nome do aluno(a): "))

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
media = (n1 + n2 + n3) / 3

print("A a media do aluno(a) {} é {:.1f} na matéria de {}.".format(nome, media, materia))