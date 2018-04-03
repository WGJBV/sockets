import socket
import datetime as dt
from datetime import datetime

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

address = ('127.0.0.1', 8888)
print('--- Starting Server on port ', address[1], ' at [', dt.datetime.today(), '] ---')
sock.bind(address)
sock.listen(1)
conn, addr = sock.accept()
buffer_length = 1024
message_complete = False
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
response = '[' + dt.datetime.today() + '] Echoed: \'' + part.decode('utf8') + '\''
conn.sendall(response.encode('utf8'))
conn.close()
sock.close()