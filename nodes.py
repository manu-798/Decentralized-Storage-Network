import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.29.112", 9999))
a="Active"
b="Done"
a_enc=a.encode()
b_enc=b.encode()
while True:
    x=s.recv(1024).decode()
    if x=="Active?":
        s.send(a_enc)
    elif x=="Give":
        name=s.recv(1024).decode('utf-32')
        with open(f"{name}","rb") as f:
            packet=f.read()
            s.send(packet)
    else:
        # size=int(s.recv(1024))
        name=s.recv(1024).decode()
        packet=s.recv(1000000000)
        print("packet recieved")
        with open(f"{name}","wb") as f:
            f.write(packet)
            #s.send(b_enc)
