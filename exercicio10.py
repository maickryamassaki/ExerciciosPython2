"""Exercício 10 (Desafio) — Sistema Completo de Gerenciamento de Senhas: Crie um programa 
que combine todos os conceitos das aulas 6-8 em um sistema de gerenciamento de senhas.
 O programa deve usar um while Truecom menu: [1] Cadastrar senha (serviço + senha), 
 [2] Listar serviços, [3] Buscar senha por serviço, [4] Gerar senha solicitada, 
 [5] Avaliar força de todas as senhas, [6] Exportar relatório, [7] Sair."""

import random
 
especiais = "!@#$%&*"
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
 
senhas = {}
 
 
def avaliar_forca(senha):
    tem_maiuscula = any(letra.isupper() for letra in senha)
    tem_minuscula = any(letra.islower() for letra in senha)
    tem_numero = any(letra.isdigit() for letra in senha)
    tem_especial = any(letra in especiais for letra in senha)
    requisitos_atendidos = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])
    if len(senha) >= 12 and requisitos_atendidos >= 3:
        return "Forte"
    elif len(senha) >= 8 and requisitos_atendidos >= 2:
        return "Média"
    else:
        return "Fraca"
 
 
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
 
    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        elif letra.islower():
            tem_minuscula = True
        elif letra.isdigit():
            tem_numero = True
        elif letra in especiais:
            tem_especial = True
 
    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return "Forte"
    elif (tem_maiuscula or tem_minuscula) and tem_numero:
        return "Média"
    else:
        return "Fraca"
 
 
def cadastrar_senha():
    servico = input("Nome do serviço: ").strip().lower()
 
    if servico == "":
        print("Erro: Nome do serviço não pode ser vazio!")
        return
 
    if servico in senhas:
        print("Erro: Serviço já cadastrado!")
        return
 
    senha = input("Senha: ")
 
    if senha == "":
        print("Erro: Senha não pode ser vazia!")
        return
 
    forca = avaliar_forca(senha)
    senhas[servico] = senha
    print(f"Cadastrado! Força: {forca}")
 
 
def listar_servicos():
    if len(senhas) == 0:
        print("Nenhum serviço cadastrado.")
        return
 
    print("\n=== Serviços Cadastrados ===")
    for i, servico in enumerate(senhas):
        print(f"  {i + 1}. {servico}")
 
 
def buscar_senha():
    servico = input("Nome do serviço: ").strip().lower()
 
    if servico in senhas:
        print(f"Serviço: {servico}")
        print(f"Senha:   {senhas[servico]}")
        print(f"Força:   {avaliar_forca(senhas[servico])}")
    else:
        print("Serviço não encontrado.")
        input("\nPressione ENTER para voltar ao menu...")
 
 
def gerar_senha():
    try:
        tamanho = int(input("Tamanho da senha: "))
 
        if tamanho < 4:
            print("Erro: Tamanho mínimo é 4 caracteres.")
            return
 
        senha_gerada = ""
        for i in range(tamanho):
            senha_gerada += random.choice(caracteres)
 
        print(f"Senha gerada: {senha_gerada}")
        print(f"Força: {avaliar_forca(senha_gerada)}")
 
        salvar = input("Deseja salvar essa senha? (s/n): ").strip().lower()
        if salvar == "s":
            servico = input("Nome do serviço: ").strip().lower()
            if servico in senhas:
                print("Erro: Serviço já cadastrado!")
            else:
                senhas[servico] = senha_gerada
                print("Senha salva com sucesso!")
 
    except ValueError:
        print("Erro: Digite um número inteiro para o tamanho!")
 
 
def avaliar_todas():
    if len(senhas) == 0:
        print("Nenhuma senha cadastrada.")
        return
 
    print("\n=== Avaliação de Força das Senhas ===")
    for servico in senhas:
        forca = avaliar_forca(senhas[servico])
        print(f"  {servico:<20} → {forca}")
        input("\nPressione ENTER para voltar ao menu...")
 
 
def exportar_relatorio():
    try:
        nome_arquivo = "senhas_relatorio.txt"
 
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== Relatório de Senhas ===\n\n")
 
            for servico in senhas:
                forca = avaliar_forca(senhas[servico])
                arquivo.write(f"Serviço: {servico}\n")
                arquivo.write(f"Senha:   {senhas[servico]}\n")
                arquivo.write(f"Força:   {forca}\n")
                arquivo.write("-" * 30 + "\n")
 
            arquivo.write(f"\nTotal de serviços: {len(senhas)}\n")
 
        print(f"Relatório exportado com sucesso! Arquivo: {nome_arquivo}")
 
    except Exception as erro:
        print(f"Erro ao exportar: {erro}")
 
 
def main():
    print("========== Exercício 10 — Gerenciador de Senhas ==========\n")
 
    while True:
        print("\n=== Menu ===")
        print("[1] Cadastrar senha")
        print("[2] Listar serviços")
        print("[3] Buscar senha por serviço")
        print("[4] Gerar senha aleatória")
        print("[5] Avaliar força de todas as senhas")
        print("[6] Exportar relatório")
        print("[7] Sair")
 
        try:
            opcao = input("\nEscolha uma opção: ").strip()
 
            if opcao == "1":
                cadastrar_senha()
            elif opcao == "2":
                listar_servicos()
            elif opcao == "3":
                buscar_senha()
            elif opcao == "4":
                gerar_senha()
            elif opcao == "5":
                avaliar_todas()
            elif opcao == "6":
                exportar_relatorio()
            elif opcao == "7":
                print("Encerrando...")
                break
            else:
                print("Opção inválida! Digite um número de 1 a 7.")
 
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break
 
 
main()