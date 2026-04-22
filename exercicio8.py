"""Exercício 8 — Inventário de Ativos com CRUD: Crie um programa
 que gere um inventário de ativos de rede usando uma lista de
 dicionários. Cada ativo tem: nome, tipo (servidor/estação/switch
 /roteador), IP e status (ativo/inativo). O programa deve ter
 menu com: [1] Cadastrar ativo, [2] Listar ativos, [3] Buscar por
 IP, [4] Alterar status, [5] Remover ativo, [6] Sair. 
 Trate com sugestões inválidas (ex: IP duplicado, ativo não
 encontrado). Use for para buscas e listas."""

ativos = [
    {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
    {"nome": "PC-RH03",   "tipo": "estacao",  "ip": "192.168.1.45", "status": "ativo"},
    {"nome": "SW-CORE01", "tipo": "switch",   "ip": "192.168.1.1",  "status": "inativo"},
]
 
 
def ip_existe(ip):
    for ativo in ativos:
        if ativo["ip"] == ip:
            return True
    return False
 
 
def cadastrar_ativo():
    nome = input("Nome do ativo: ")
    tipo = input("Tipo (servidor/estacao/switch/roteador): ")
    ip = input("IP: ")
    if ip_existe(ip):
        print("Erro: IP já cadastrado!")
        return
    ativos.append({"nome": nome, "tipo": tipo, "ip": ip, "status": "ativo"})
    print(f"Ativo '{nome}' cadastrado com sucesso!")
 
 
def listar_ativos():
    if len(ativos) == 0:
        print("Nenhum ativo cadastrado.")
        return
    print(f"\n{'#':<4} {'Nome':<12} {'Tipo':<10} {'IP':<16} {'Status'}")
    print("-" * 55)
    for i in range(len(ativos)):
        a = ativos[i]
        print(f"{i+1:<4} {a['nome']:<12} {a['tipo']:<10} {a['ip']:<16} {a['status']}")
 
 
def buscar_por_ip(ip):
    for ativo in ativos:
        if ativo["ip"] == ip:
            print(f"  Nome:   {ativo['nome']}")
            print(f"  Tipo:   {ativo['tipo']}")
            print(f"  IP:     {ativo['ip']}")
            print(f"  Status: {ativo['status']}")
            return
    print("Ativo não encontrado.")
 
 
def alterar_status(ip):
    for ativo in ativos:
        if ativo["ip"] == ip:
            novo_status = input("Novo status (ativo/inativo): ")
            ativo["status"] = novo_status
            print("Status atualizado!")
            return
    print("Ativo não encontrado.")
 
 
def remover_ativo(ip):
    for ativo in ativos:
        if ativo["ip"] == ip:
            ativos.remove(ativo)
            print("Ativo removido!")
            return
    print("Ativo não encontrado.")
 
 
def main():
    print("========== Exercício 8 — Inventário de Ativos ==========")
    while True:
        print("\n=== Inventário de Ativos ===")
        print("[1] Cadastrar ativo")
        print("[2] Listar ativos")
        print("[3] Buscar por IP")
        print("[4] Alterar status")
        print("[5] Remover ativo")
        print("[6] Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_ativo()
        elif opcao == "2":
            listar_ativos()
        elif opcao == "3":
            ip = input("Digite o IP a buscar: ")
            buscar_por_ip(ip)
        elif opcao == "4":
            ip = input("Digite o IP do ativo: ")
            alterar_status(ip)
        elif opcao == "5":
            ip = input("Digite o IP do ativo a remover: ")
            remover_ativo(ip)
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")
 
 
main()