__author__ = 'Ranjith'
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print "Received connection from", addr
    c.send("buhahaha...gotcha")
    print c.recv(1024)
    c.close()