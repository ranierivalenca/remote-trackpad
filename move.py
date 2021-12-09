import mouse
# import socket

# socket.

# while True:
#   x, y = input().split(',')
#   mouse.move(int(x), int(y), absolute=False)

#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('listening..')
while True:
  conn, addr = s.accept()
  print('Connected by', addr)
  print('Conn: ', conn)
  while True:
    data = conn.recv(1024)
    if not data:
        break

    try:
        x, y = str(data, 'ascii').split(',')
        mouse.move(int(x), int(y), absolute=False, duration=0.01)
    except:
        pass
    #   conn.sendall(data)
  print('finished\n')