import socket

port = int(input("РџРѕСЂС‚:"))
sock = socket.socket()
try:
    sock.bind(('', port))
except OSError:
    sock.bind(('', 8080))

conn, addr = sock.accept()
print("Connected", addr)
data = conn.recv(8192)
msg = data.decode()
name = msg.split()[1][1:]
if name == "" : name = "1.html"
resp = f"""HTTP/1.1 200 OK
    Connection: close
    
    """
with open(name, "r") as f:
    resp += f.read()
conn.send(resp.encode())
conn.close()
