import socket
import struct

MCAST_GRP = '239.255.0.1'
MCAST_PORT = 5000

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa à porta multicast
sock.bind(('', MCAST_PORT))

# Entra no grupo multicast
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"🟢 Escutando grupo multicast {MCAST_GRP}:{MCAST_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"📨 Mensagem recebida de {addr}: {data.decode('utf-8')}")
