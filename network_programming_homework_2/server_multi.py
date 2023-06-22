import socket 
import threading
import json

def handle_client(sock, addr):
    sock.send("insert user name : ".encode())
    user_name = sock.recv(1024).decode()
    print(f'''[+] accepting connection
          address = {addr}
          name = {user_name}''')
    grade = 0
    for i in range(1,21):
        question = questions[str(i)][0]
        answer = questions[str(i)][1]
        try : 
            sock.send(f"question {i}: {question}".encode())
            student_answer = sock.recv(1024).decode()
            if answer == student_answer : 
                grade += 1
        except :
            print("Socket Error")
    sock.send("end".encode())
    sock.send(f"the deserved grade is {grade} !".encode())
    print(f"[-] tcp connection for {user_name} is closed")
    sock.close()
    try:
        with open("grades.json","a") as grades:
            grades.write(f"{user_name} : {grade}")
    except:
        with open("grades.json","w") as grades:
            grades.write(f"{user_name} : {grade}")


with open("questions.json","r") as file:
    questions = json.load(file)
user_name, host, port ="", "127.0.0.1","54321" 

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try : 
    server_sock.bind(('127.0.0.1',54321))
except socket.error as err_msg:
    print ("error : ",err_msg)
    sys.exit(1)
server_sock.listen()
while True:
    print(f"[+] tcp quiz sever running")
    client_sock, client_addr = server_sock.accept()
    thread = threading.Thread(target=handle_client,args=(client_sock, client_addr))
    thread.start()
    print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')
server_sock.close()
        