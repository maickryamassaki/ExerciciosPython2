"""Exercício 6 — Blacklist de IPs com Sets: Crie um programa 
que compare dois sets: um com IPs que acessam o servidor e outro
 com uma blacklist de IPs maliciosos. Usando operações de 
 conjuntos, descubra e exiba: quais IPs maliciosos foram 
 detectados (interseção), quais IPs são seguros (diferença),
   quais IPs da blacklist não apareceram (diferença inversa) e 
   o total de IPs únicos considerando ambas as listas (união). 
   Exiba os resultados formatados."""

# Dados de entrada
acessos = {
    "192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
    "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"
}

blacklist = {
    "185.220.101.1", "45.33.32.156", "91.240.118.172",
    "23.94.5.100", "104.244.72.115"
}

maliciosos_detectados = acessos.intersection(blacklist)
ips_seguros = acessos.difference(blacklist)
blacklist_nao_detectados = blacklist.difference(acessos)
total_unicos = acessos.union(blacklist)

print("=== Relatório de Segurança ===")

print(f"IPs maliciosos detectados ({len(maliciosos_detectados)}):")
for ip in maliciosos_detectados:
    print(f"  - {ip}")

print(f"\nIPs seguros ({len(ips_seguros)}):")
for ip in ips_seguros:
    print(f"  - {ip}")

print(f"\nIPs da blacklist não detectados ({len(blacklist_nao_detectados)}):")
for ip in blacklist_nao_detectados:
    print(f"  - {ip}")

print(f"\nTotal de IPs únicos: {len(total_unicos)}")