import socket

csock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
csock.settimeout(5)
try:
    csock.connect(('127.0.0.1',54321))
    while True:
        servermsg = csock.recv(1024).decode()
        if servermsg == "end":
            break
        print(servermsg)
        csock.sendall(input("").encode())
except socket.error as err_msg:
    print("error msg :",err_msg)

finally:
    grade = csock.recv(1024).decode()
    print(grade)
    csock.close()