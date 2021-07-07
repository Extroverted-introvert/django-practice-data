from socket import *

def createServer():
    serversocket = socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost',9001))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split('\n')
            if (len(pieces) > 0) : print(pieces[0])

            print("Move along, nothing to see here...\n")

            data = "HTTP/1.1 302 OK\r\n"
            data += "Location: https://www.dj4e.com/\r\n"
            data += "\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()

print('Access http://localhost:9001')
createServer()
