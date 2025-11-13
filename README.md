# 📡 IPv4 Multicast Communication – Node.js & Python

![Multicast Banner](https://user-images.githubusercontent.com/00000000/multicast-banner.png)

> 💡 Comunicação em grupo (um-para-muitos) via UDP Multicast — um projeto prático com Node.js e Python, ideal para aplicações de IoT, telemetria e sistemas distribuídos.

---

## 🚀 Sobre o Projeto

Este projeto demonstra como realizar **comunicação multicast IPv4** usando **UDP (User Datagram Protocol)** em **Node.js** e **Python**.

Um **emissor (sender)** envia pacotes UDP para um **grupo multicast**, e múltiplos **receptores (listeners)** conectados à mesma rede recebem as mensagens **simultaneamente** — sem precisar de conexões diretas entre os dispositivos.

📍 **Endereço Multicast usado:** `239.255.0.1`  
📍 **Porta:** `5000`

---

## 🧠 Objetivo

Explorar de forma prática como funciona o **protocolo multicast IPv4**, aplicável em:
- Sistemas de **IoT** e **telemetria**
- **Monitoramento de equipamentos**
- **Streaming de dados** em tempo real
- **Alertas e notificações distribuídas**

---

## 🧩 Estrutura do Projeto

multicast-demo/
<br/>├── nodejs/
<br/>│ ├── sender.js # Envia mensagens multicast (Node.js)
<br/>│ └── listener.js # Recebe mensagens multicast (Node.js)
<br/>└── python/
<br/>├── sender.py # Envia mensagens multicast (Python)
<br/>└── listener.py # Recebe mensagens multicast (Python)
<br/>

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Ferramenta / Tecnologia |
|------------|------------------------|
| Linguagens | 🟩 Node.js, 🐍 Python |
| Protocolo  | IPv4 UDP Multicast |
| Rede | Sockets, TTL, UDP Datagrams |
| Conceitos Praticados | Comunicação um-para-muitos, grupos multicast, redes locais |

---

## 💻 Como Executar o Projeto

### 🟢 Node.js

1. Acesse a pasta `nodejs/`
2. Instale dependências (se necessário):
   ```bash
   npm init -y
Execute o listener (receptor):

node listener.js


Em outro terminal, execute o sender (emissor):

node sender.js

🐍 Python

Acesse a pasta python/

Execute o listener:

python listener.py


Em outro terminal, execute o sender:

python sender.py


🟡 Mensagens serão transmitidas a cada 3 segundos e exibidas nos receptores que fizerem parte do grupo multicast.

🌐 Funcionamento do Multicast
   <br/>Sender (UDP)      
   <br/>239.255.0.1:5000 
      <br/>Sender (UDP)      
         <br/>239.255.0.1:5000 
          <br/>Listener #1    ││  Listener #2   │
       <br/>│ Recebe mensagens││ Recebe mensagens
      

🔬 Conceitos Aplicados

Criação de sockets UDP

Adesão a grupos multicast (IGMP)

Configuração de TTL (Time To Live)

Diferença entre unicast, broadcast e multicast

Comunicação sem estado e de baixa latência

📘 Aprendizados

Prática de redes e comunicação em tempo real

Integração entre Node.js e Python via UDP

Fundamentos de infraestrutura distribuída

Simulação de cenários de IoT e telemetria

🧑‍💻 Autor

Leandro Chagas
Especialista em Suporte Técnico e Infraestrutura | IoT | Redes | DevOps
📧 leandrosrs2012@gmail.com

🔗 GitHub: chagasleandro

🔗 LinkedIn: leandro-chagas-
