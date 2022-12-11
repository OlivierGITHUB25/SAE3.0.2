import sys
import socket
import psutil
import os
import platform

host = "0.0.0.0"
port = 7777

def Serveur():
    while True:
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        msg = ""
        while msg != "kill" and msg != "reset":
            print("En attente du client")
            conn, address = server_socket.accept()
            print(f"Client connecté {address}")

            msg = ""
            while msg != "kill" and msg != "disconect" and msg != "reset":
                msg = conn.recv(1024).decode()
                print(msg)
                resultat = msg.split(":", 1)
                try :
                    msgt = resultat[1]
                    mode = resultat[0]
                except:
                    msgt = msg

                if msgt == "ram":
                    reply = str(f"ram:{psutil.virtual_memory().percent}%")
                    conn.send(reply.encode())

                elif msgt == "cpu":
                    reply = str(f"cpu:{psutil.cpu_percent()}%")
                    conn.send(reply.encode())

                elif msgt == "os":
                    reply = str(platform.system())
                    conn.send(reply.encode())

                elif msgt == "ip":
                    reply = str(socket.gethostbyname(socket.gethostname()))
                    conn.send(reply.encode())

                elif mode == "powershell":
                    ostest  = str(platform.system())
                    if ostest == "Windows":
                        rep = os.popen(f"powershell {msgt}")
                        reply = rep.read()
                        if reply == "":
                            reply = "erreur syntaxe"
                            conn.send(reply.encode())
                        else:
                            conn.send(reply.encode())
                    else:
                        reply = "cette os n'est pas compatible avec powershell !!!"
                        conn.send(reply.encode())

                elif mode == "linux":
                    ostest  = str(platform.system())
                    if ostest == "Linux":
                        rep = os.popen(f"{msgt}")
                        reply = rep.read()
                        if reply == "":
                            reply = "erreur syntaxe"
                            conn.send(reply.encode())
                        else:
                            conn.send(reply.encode())
                    else:
                        reply = "cette os n'est pas linux !!!"
                        conn.send(reply.encode())

                elif mode == "windows":
                    ostest = str(platform.system())
                    if ostest == "Windows":
                        rep = os.popen(f"{msgt}")
                        reply = rep.read()
                        if reply == "":
                            reply = "erreur syntaxe"
                            conn.send(reply.encode())
                        else:
                            conn.send(reply.encode())
                    else:
                        reply = "cette os n'est pas windows !!!"
                        conn.send(reply.encode())

                else:
                    rep = os.popen(msgt)
                    reply = rep.read()
                    if reply == "":
                        reply = "erreur syntaxe"
                        conn.send(reply.encode())
                    else:
                        conn.send(reply.encode())

            conn.close()
            print("fermeture de la connexion")

        server_socket.close()
        print("fermeture du serveur")
        if msg == "kill":
            exit()

if __name__ == '__main__':
    sys.exit(Serveur())