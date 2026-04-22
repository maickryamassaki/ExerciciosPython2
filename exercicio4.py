"""Exercício 4 — Análise de Notas com Tuplas: Crie um programa que 
receba as notas de 5 alunos (nome e nota) e armazene cada par 
como uma tupla dentro de uma lista. Depois, usando laços, 
calcule e exiba: a nota maior e o nome do aluno, a menor nota e
o nome do aluno, a média da turma, e quais 
alunos estão acima da média. Use forpara percorrer a lista."""

def encontrar_maior(alunos):
    nome_maior = alunos[0][0]
    nota_maior = alunos[0][1]
    for aluno in alunos:
        if aluno[1] > nota_maior:
            nota_maior = aluno[1]
            nome_maior = aluno[0]
    return nome_maior, nota_maior
 
 
def encontrar_menor(alunos):
    nome_menor = alunos[0][0]
    nota_menor = alunos[0][1]
    for aluno in alunos:
        if aluno[1] < nota_menor:
            nota_menor = aluno[1]
            nome_menor = aluno[0]
    return nome_menor, nota_menor
 
 
def calcular_media(alunos):
    soma = 0
    for aluno in alunos:
        soma += aluno[1]
    return soma / len(alunos)
 
 
def main():
    print("========== Exercício 4 — Análise de Notas com Tuplas ==========")
    alunos = []
    for i in range(5):
        nome = input(f"Nome do aluno {i + 1}: ")
        nota = float(input(f"Nota de {nome}: "))
        alunos.append((nome, nota))
 
    nome_maior, nota_maior = encontrar_maior(alunos)
    nome_menor, nota_menor = encontrar_menor(alunos)
    media = calcular_media(alunos)
 
    print("\n=== Relatório de Notas ===")
    print(f"Maior nota: {nome_maior} - {nota_maior}")
    print(f"Menor nota: {nome_menor} - {nota_menor}")
    print(f"Média da turma: {media:.1f}")
    print("\nAlunos acima da média:")
    for aluno in alunos:
        if aluno[1] > media:
            print(f"  - {aluno[0]}: {aluno[1]}")
 
 
main()
