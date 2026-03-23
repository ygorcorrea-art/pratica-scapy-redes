from scapy.all import *

# contador de pacotes
contador = 0

# contadores para resumo final
total_tcp = 0
total_udp = 0
total_outros = 0


# função que analisa cada pacote capturado
def analisar_pacote(pacote):
    global contador, total_tcp, total_udp, total_outros

    contador += 1  # incrementa número do pacote

    print(f"\n--- Pacote {contador} ---")

    # tamanho total do pacote
    print(f"Tamanho total: {len(pacote)} bytes")

    # -------------------------
    # CAMADA DE ENLACE (Ethernet)
    # -------------------------
    print("[Enlace]")
    if pacote.haslayer(Ether):
        eth = pacote[Ether]
        print(f"  MAC origem : {eth.src}")
        print(f"  MAC destino: {eth.dst}")
    else:
        print("  Sem dados Ethernet")

    # -------------------------
    # CAMADA DE INTERNET (IP)
    # -------------------------
    print("[Internet]")
    if pacote.haslayer(IP):
        ip = pacote[IP]
        print(f"  IP origem  : {ip.src}")
        print(f"  IP destino : {ip.dst}")

        # traduz protocolo (mais fácil de entender)
        if ip.proto == 6:
            protocolo_nome = "TCP"
        elif ip.proto == 17:
            protocolo_nome = "UDP"
        else:
            protocolo_nome = str(ip.proto)

        print(f"  Protocolo  : {protocolo_nome}")
    else:
        print("  Sem dados IP")

    # -------------------------
    # CAMADA DE TRANSPORTE
    # -------------------------
    if pacote.haslayer(TCP):
        print("[Transporte - TCP]")
        tcp = pacote[TCP]

        print(f"  Porta origem : {tcp.sport}")
        print(f"  Porta destino: {tcp.dport}")

        # FLAGS TCP COM TRADUÇÃO
        flags = str(tcp.flags)
        descricao = []

        if "S" in flags:
            descricao.append("SYN")
        if "A" in flags:
            descricao.append("ACK")
        if "F" in flags:
            descricao.append("FIN")
        if "P" in flags:
            descricao.append("PSH")

        print(f"  Flags        : {flags} ({', '.join(descricao)})")

        total_tcp += 1

        camada_transporte = tcp

    elif pacote.haslayer(UDP):
        print("[Transporte - UDP]")
        udp = pacote[UDP]

        print(f"  Porta origem : {udp.sport}")
        print(f"  Porta destino: {udp.dport}")

        total_udp += 1

        camada_transporte = udp

    else:
        print("[Transporte]")
        print("  Não é TCP nem UDP")

        total_outros += 1

        camada_transporte = None

    # -------------------------
    # CAMADA DE APLICAÇÃO (CORRIGIDA)
    # -------------------------
    print("[Aplicação]")

    # verifica payload corretamente (não depende só de Raw)
    if camada_transporte and camada_transporte.payload:
        tamanho_payload = len(bytes(camada_transporte.payload))
        print("  Payload presente: sim")
    else:
        tamanho_payload = 0
        print("  Payload presente: não")

    print(f"  Tamanho payload : {tamanho_payload} bytes")

    # separador visual
    print("-" * 30)


# função principal
def capturar():
    print("Iniciando captura...")

    # usuário escolhe interface
    interface = input("Interface (ENTER para padrão): ")

    if interface == "":
        interface = None

    print(f"Interface: {interface if interface else 'padrão'}")
    print("Quantidade de pacotes: 10")

    # captura os pacotes
    sniff(
        iface=interface,
        count=10,
        prn=analisar_pacote
    )

    # -------------------------
    # RESUMO FINAL
    # -------------------------
    print("\n===== RESUMO =====")
    print(f"Total de pacotes: {contador}")
    print(f"TCP: {total_tcp}")
    print(f"UDP: {total_udp}")
    print(f"Outros: {total_outros}")


# executa o programa
if __name__ == "__main__":
    capturar()
