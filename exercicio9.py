"""Exercício 9 — Analisador de Logs de Segurança: Crie um 
programa que analisa uma lista de logs (strings), extraindo 
informações com manipulação de strings e armazenando em 
dicionários. Para cada log: extraia o nível 
(INFO/WARNING/ERROR), o IP de origem e a mensagem. 
Conte os eventos por nível, identifique o IP com mais erros e 
gere um relatório. Use for, dicionários e try/exceptpara tratar
 logs malformados."""

def processar_log(linha):

    if "]" not in linha or "IP: " not in linha:
        raise ValueError("Log malformado")

    inicio_nivel = linha.find("[", 20) + 1 
    fim_nivel = linha.find("]", inicio_nivel)
    nivel = linha[inicio_nivel:fim_nivel]


    ip = linha.split("IP: ")[1].strip()

    return nivel, ip

def analisar_logs(logs):
    contagens = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    contagem_malformados = 0
    erros_por_ip = {}

    for linha in logs:
        try:
            nivel, ip = processar_log(linha)
            if nivel in contagens:
                contagens[nivel] += 1
                if nivel == "ERROR":
                    erros_por_ip[ip] = erros_por_ip.get(ip, 0) + 1
            else:
                # Caso encontre um nível não esperado
                contagem_malformados += 1
        except Exception:
            contagem_malformados += 1
            
    return contagens, contagem_malformados, erros_por_ip

def exibir_relatorio(contagens, malformados, erros_por_ip):
    print("=== Relatório de Logs ===")
    print(f"INFO:    {contagens['INFO']} eventos")
    print(f"WARNING: {contagens['WARNING']} eventos")
    print(f"ERROR:   {contagens['ERROR']} eventos")
    print(f"Logs malformados: {malformados}")

    if erros_por_ip:
        ip_top = max(erros_por_ip, key=erros_por_ip.get)
        print(f"\nIP com mais erros: {ip_top} ({erros_por_ip[ip_top]} erros)")
        
        print("\nDetalhamento de erros:")
        # Ordena do maior para o menor
        for ip, qtd in sorted(erros_por_ip.items(), key=lambda item: item[1], reverse=True):
            print(f"  {ip:<15} → {qtd} erro{'s' if qtd > 1 else ''}")


logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

contagens, malformados, erros_por_ip = analisar_logs(logs)
exibir_relatorio(contagens, malformados, erros_por_ip)