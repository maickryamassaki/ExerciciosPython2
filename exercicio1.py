""" Exercício 1 — Contador de Vogais e Consoantes: Crie um programa que parte uma frase ao usuário e use um laço for 
para percorrer cada caractere, contando quantos vogais e quantas consoantes existem. Ignore números, espaços e 
caracteres especiais. Exiba o total de cada um ao final.  """

vogais = "aeiouAEIOU"
 
 
def contar_vogais_consoantes(frase):
    contador_vogais = 0
    contador_consoantes = 0
    for letra in frase:
        if letra in vogais:
            contador_vogais += 1
        elif letra.isalpha():
            contador_consoantes += 1
    return contador_vogais, contador_consoantes
 
 
def main():
    print("========== Exercício 1 — Contador de Vogais e Consoantes ==========")
    frase = input("Digite uma frase: ")
    total_vogais, total_consoantes = contar_vogais_consoantes(frase)
    print(f'\nFrase: "{frase}"')
    print(f"Vogais: {total_vogais}")
    print(f"Consoantes: {total_consoantes}")
 
 
main()
