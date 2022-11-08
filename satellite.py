from os import remove
import socket
import threading
from time import sleep
import new

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.29.112", 9999))
s.listen()
nodes_list=[]
def get_new_nodes(s):
    while True:
        global nodes_list
        conn, addr = s.accept()
        nodes_list.append(conn)
        print (addr[0] + str(addr[1]) + " connected")

def send_rpc():
    global active
    for node in nodes_list:
        try:
            node.send(b'Active?')
        except:
            if node in active:
                active.remove(node)
            continue
        threading.Thread(target=recieve_rpc,args=(node,active)).start()
    print(active)
        
def recieve_rpc(node,active):
    x=node.recv(1024).decode()
    if x=="Active":
        if node not in active:
            active.append(node)
        return active

threading.Thread(target=get_new_nodes,args=(s,)).start()

active=[]
while True:
    send_rpc()
    sleep(5)
    if len(active) >=5:
        x=new.TestErasureCoder()
        x.setUp()
        r=x.encode('ph0-02.jpg',active)
        x.decode(r,active)