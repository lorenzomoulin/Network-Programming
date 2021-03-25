import socket
from sys import argv
import time
import statistics

ip_port = (argv[1], int(argv[2]))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1)
n_packets = 10

msg = ""
nome = "Lorenzo Guimaraes Moulinaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dtgrams = []
timestamps = []

ini = time.time()
for i in range(1, n_packets + 1):
    tmp = time.time()
    ts = int(tmp*1000) % 10000
    timestamps += [tmp*1000]
    msg = str(i).zfill(5) + "0" + str(ts).zfill(4) + nome.zfill(30)[:30]
    s.sendto(msg.encode("utf-8"), ip_port)
    try:
        data, address = s.recvfrom(1024)
        dtgrams += [time.time()*1000 - timestamps[i-1]]
        print(f'{i}:{dtgrams[-1]}')
    except socket.timeout as e:
        print(e)
total_time = (time.time() - ini)*1000
print (f'{n_packets} packets transmitted, ' + \
    f'{len(dtgrams)} received, ' + \
    f'{100*(n_packets - len(dtgrams))/n_packets}% packet loss, ' + \
    f'time {int(total_time)}ms\n')

print(f'rtt min/avg/max/mdev = {min(dtgrams)}/{sum(dtgrams)/len(dtgrams)}/{max(dtgrams)}/{statistics.pstdev(dtgrams)}')

s.close()