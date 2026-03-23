# Prática com Scapy - Captura e Análise de Pacotes de Rede

## Descrição

Este projeto tem como objetivo implementar um programa em Python utilizando a biblioteca Scapy para capturar e analisar pacotes de rede em tempo real.

O sistema captura pacotes da interface de rede, identifica as camadas do modelo TCP/IP e extrai informações relevantes, como endereços, protocolos, portas, flags TCP e presença de carga útil (payload).

---

## Objetivos

- Capturar pacotes da rede utilizando Python  
- Identificar as camadas do modelo TCP/IP: Enlace (Ethernet), Internet (IP), Transporte (TCP/UDP) e Aplicação  
- Extrair informações relevantes de cada pacote  
- Exibir os dados de forma organizada  
- Gerar um resumo final da captura  

---

## Estrutura do Projeto

```
pratica-scapy-redes/
├── README.md
├── requirements.txt
├── src/
│   └── atividade.py
└── exemplos/
    └── saida_esperada.md
```

---

## Requisitos

- Python 3.x  
- Biblioteca Scapy  

Instalação das dependências:

```bash
pip install -r requirements.txt
```

Ou diretamente:

```bash
pip install scapy
```

---

## Como Executar

### Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/pratica-scapy-redes.git
cd pratica-scapy-redes
```

---

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

### Executar o programa

#### Linux ou WSL

```bash
sudo python src/atividade.py
```

#### Windows

- Execute o terminal como Administrador  
- Certifique-se de que o Npcap está instalado  

```bash
python src/atividade.py
```

---

## Escolha da Interface

Ao executar, o programa solicitará:

```
Interface (ENTER para padrão):
```

Você pode informar o nome da interface de rede, por exemplo:

- `eth0` — rede cabeada (Linux)  
- `wlan0` — rede Wi-Fi (Linux)  
- `Wi-Fi` — rede sem fio (Windows)  
- `Ethernet` — rede cabeada (Windows)  

Ou pressionar ENTER para utilizar a interface padrão do sistema.

---

## Funcionamento do Programa

O programa realiza as seguintes etapas:

1. Solicita ao usuário a interface de rede (opcional)  
2. Captura 10 pacotes da rede  
3. Para cada pacote:
   - Identifica a camada de enlace (Ethernet)  
   - Identifica a camada de internet (IP)  
   - Verifica o protocolo de transporte (TCP/UDP)  
   - Extrai portas de origem e destino  
   - Exibe flags TCP (com interpretação)  
   - Verifica a presença de carga útil (payload)  
   - Exibe o tamanho do payload  
4. Exibe os dados formatados no terminal  
5. Apresenta um resumo com a quantidade de pacotes por tipo  

---

## Exemplo de Saída

Consulte:

```
exemplos/saida_esperada.md
```

---

## Observações Importantes

- A execução pode exigir privilégios de administrador ou root  
- No Windows, é necessário instalar o driver Npcap  
- Os dados exibidos variam conforme a rede utilizada  
- O programa captura apenas 10 pacotes por execução  
- Utilize apenas em redes autorizadas  

---

## Tecnologias Utilizadas

- Python  
- Scapy  
