"""Exercício 2 — Validador de Senha com Regras: Crie um programa
que parte uma senha ao usuário repetidamente (usando while) 
 até que ela atenda TODOS os critérios: mínimo 8 caracteres,
  pelo menos 1 letra secreta, pelo menos 1 letra minúscula, 
pelo menos 1 número e pelo menos 1 caractere especial 
 ( !@#$%&*). A cada tentativa inválida, informe quais critérios
  não foram atendidos. Use breakpara sair quando a senha for
  válida."""

especiais = "!@#$%&*"
 
 
def validar_senha(senha):
    problemas = []
    if len(senha) < 8:
        problemas.append("Falta mínimo de 8 caracteres")
    tem_maiuscula = False
    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
    if not tem_maiuscula:
        problemas.append("Falta pelo menos 1 letra maiúscula")
    tem_minuscula = False
    for letra in senha:
        if letra.islower():
            tem_minuscula = True
    if not tem_minuscula:
        problemas.append("Falta pelo menos 1 letra minúscula")
    tem_numero = False
    for letra in senha:
        if letra.isdigit():
            tem_numero = True
    if not tem_numero:
        problemas.append("Falta pelo menos 1 número")
    tem_especial = False
    for letra in senha:
        if letra in especiais:
            tem_especial = True
    if not tem_especial:
        problemas.append("Falta pelo menos 1 caractere especial (!@#$%&*)")
    return problemas
 
 
def main():
    print("========== Exercício 2 — Validador de Senha ==========")
    while True:
        senha = input("Digite uma senha: ")
        problemas = validar_senha(senha)
        if len(problemas) == 0:
            print("Senha válida! Acesso liberado.")
            break
        else:
            print("Senha inválida! Problemas encontrados:")
            for problema in problemas:
                print(f"  - {problema}")
            print("Digite outra senha:\n")
 
 
main()