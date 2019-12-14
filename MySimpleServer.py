import socket
import argparse



def SimpleServer(HOST,PORT):
    socketlistener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketlistener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    socketlistener.bind((HOST, PORT))
    socketlistener.listen(1)
    print("listening to the Port {0} ",PORT)
    while True:
        clientConnection, clientAddress = socketlistener.accept()
        requestData = clientConnection.recv(1024)
        print(requestData.decode('utf-8'))

        httpResponse = """\
        HTTP/1.1 200 OK    My First Server!
        """
        clientConnection.sendall(bytes(httpResponse, 'utf-8'))
        clientConnection.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--PORT",default=8000, type=str, help="Port Number")
    parser.add_argument("--HOST",default='', type=str, help="Port Number")
    args = parser.parse_args()
    PORT = args.PORT
    HOST = args.HOST
    SimpleServer(HOST,PORT)
    

    
    
    