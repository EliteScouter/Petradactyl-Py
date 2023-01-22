#Listen on X port when connection is established execute a command
import socket
import subprocess

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 25555              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
    if data == 'exit':
        conn.close()
        break
    else:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        conn.send(stdout_value)
conn.close()