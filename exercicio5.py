"""Exercício 5 — Contador de Palavras com Dicionário: Crie um 
programa que receba um texto do usuário e conte quantas vezes 
cada palavra aparece, armazenando em um dicionário 
(palavra como chave, contagem como valor). Converta tudo para
 minúsculos antes de contar. Ao final, exiba as palavras 
 ordenadas pela frequência (da mais frequente para a menos 
 frequente) e destaque a palavra mais usada."""

def contar_palavras(texto):
    texto = texto.lower()
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem
 
 
def exibir_relatorio(contagem):
    palavras_ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
    print("\n=== Contagem de Palavras ===")
    for palavra, quantidade in palavras_ordenadas:
        if quantidade == 1:
            print(f'"{palavra}" → {quantidade} vez')
        else:
            print(f'"{palavra}" → {quantidade} vezes')
    palavra_top = palavras_ordenadas[0][0]
    quantidade_top = palavras_ordenadas[0][1]
    print(f'\nPalavra mais frequente: "{palavra_top}" ({quantidade_top} vezes)')
    print(f"Total de palavras únicas: {len(contagem)}")
 
 
def main():
    print("========== Exercício 5 — Contador de Palavras ==========")
    texto = input("Digite um texto: ")
    if len(texto.strip()) == 0:
        print("Texto vazio!")
        return
    contagem = contar_palavras(texto)
    exibir_relatorio(contagem)
 
 
main()

