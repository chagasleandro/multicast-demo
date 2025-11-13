import socket
import time

MCAST_GRP = '239.255.0.1'
MCAST_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# Define TTL = 1 (mensagem não sai da sub-rede local)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

while True:
    msg = f"Olá grupo multicast! {time.strftime('%H:%M:%S')}"
    sock.sendto(msg.encode('utf-8'), (MCAST_GRP, MCAST_PORT))
    print(f"📤 Mensagem enviada para {MCAST_GRP}:{MCAST_PORT}")
    time.sleep(3)
