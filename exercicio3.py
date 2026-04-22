"""Exercício 3 — Gerenciador de Lista de IPs: Crie um programa 
com menu interativo (usando while True) que gera uma lista de 
endereços IP. O menu deve ter as opções: [1] Adicionar IP, 
[2] Remover IP, [3] Listar todos, [4] Buscar IP, [5] Sair. 
Não permita IPs duplicados na lista. Na busca, informe se o IP 
foi encontrado e em qual posição. Use breakpara sair do loop
 quando o usuário escolher a opção 5."""

def adicionar_ip(ips, ip):
    if ip in ips:
        print("IP já existe na lista!")
    else:
        ips.append(ip)
        print("IP adicionado!")
 
 
def remover_ip(ips, ip):
    if ip in ips:
        ips.remove(ip)
        print("IP removido!")
    else:
        print("IP não encontrado na lista!")
 
 
def listar_ips(ips):
    if len(ips) == 0:
        print("Nenhum IP cadastrado.")
    else:
        print("--- Lista de IPs ---")
        for i in range(len(ips)):
            print(f"  {i + 1}. {ips[i]}")
        input("\nPressione ENTER para continuar...")
 
 
def buscar_ip(ips, ip):
    if ip in ips:
        posicao = ips.index(ip) + 1
        print(f"IP encontrado na posição {posicao}")
    else:
        print("IP não encontrado")
 
 
def main():
    print("========== Exercício 3 — Gerenciador de IPs ==========")
    ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]
    while True:
        print("\n=== Gerenciador de IPs ===")
        print("[1] Adicionar IP")
        print("[2] Remover IP")
        print("[3] Listar todos")
        print("[4] Buscar IP")
        print("[5] Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            ip = input("Digite o IP a adicionar: ")
            adicionar_ip(ips, ip)
        elif opcao == "2":
            ip = input("Digite o IP a remover: ")
            remover_ip(ips, ip)
        elif opcao == "3":
            listar_ips(ips)
        elif opcao == "4":
            ip = input("Digite o IP a buscar: ")
            buscar_ip(ips, ip)
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")
 
 
main()