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

def cadastrar_senha():
    servico = input("Nome do serviço: ").strip().lower()
    if not servico:
        print("Erro: Nome do serviço não pode ser vazio!")
        return
    if servico in senhas:
        print("Erro: Serviço já cadastrado!")
        return

    senha = input("Senha: ")
    if not senha:
        print("Erro: Senha não pode ser vazia!")
        return

    senhas[servico] = senha
    print(f"Cadastrado! Força: {avaliar_forca(senha)}")

def listar_servicos():
    if not senhas:
        print("Nenhum serviço cadastrado.")
        return
    print("\n=== Serviços Cadastrados ===")
    for i, servico in enumerate(senhas, 1):
        print(f" {i}. {servico}")

def buscar_senha():
    servico = input("Nome do serviço: ").strip().lower()
    if servico in senhas:
        print(f"\nServiço: {servico}\nSenha: {senhas[servico]}\nForça: {avaliar_forca(senhas[servico])}")
    else:
        print("Serviço não encontrado.")

def gerar_senha():
    try:
        tamanho = int(input("Tamanho da senha: "))
        if tamanho < 4:
            print("Erro: Tamanho mínimo é 4.")
            return
        
        senha_gerada = "".join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Senha gerada: {senha_gerada} (Força: {avaliar_forca(senha_gerada)})")
        
        if input("Deseja salvar? (s/n): ").lower() == 's':
            servico = input("Nome do serviço: ").strip().lower()
            if servico in senhas: print("Erro: Serviço já cadastrado!")
            else: senhas[servico] = senha_gerada; print("Salvo!")
    except ValueError:
        print("Erro: Digite um número inteiro.")

def avaliar_todas():
    if not senhas:
        print("Nenhuma senha cadastrada.")
        return
    print("\n=== Avaliação de Força ===")
    for servico, senha in senhas.items():
        print(f" {servico:<20} → {avaliar_forca(senha)}")

def exportar_relatorio():
    try:
        with open("senhas_relatorio.txt", "w", encoding="utf-8") as f:
            f.write("=== Relatório de Senhas ===\n\n")
            for servico, senha in senhas.items():
                f.write(f"Serviço: {servico} | Senha: {senha} | Força: {avaliar_forca(senha)}\n")
        print("Relatório exportado com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar: {e}")

def main():
    print("========== Gerenciador de Senhas ==========")
    while True:
        print("\n[1] Cadastrar | [2] Listar | [3] Buscar | [4] Gerar | [5] Avaliar todas | [6] Exportar | [7] Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1": cadastrar_senha()
        elif opcao == "2": listar_servicos()
        elif opcao == "3": buscar_senha()
        elif opcao == "4": gerar_senha()
        elif opcao == "5": avaliar_todas()
        elif opcao == "6": exportar_relatorio()
        elif opcao == "7": print("Encerrando..."); break
        else: print("Opção inválida!")

if __name__ == "__main__":
    main()
 
