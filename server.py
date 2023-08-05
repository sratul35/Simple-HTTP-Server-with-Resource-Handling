import socket
import threading
from urls import *

SERVER_HOST = 'localhost'
SERVER_PORT = 8080

def handle_client(client_socket):
    try:
        msg = client_socket.recv(1024).decode()
        method = msg.split(' ')[0]
        resource = msg.split(' ')[1]

        print(f"Message: {method}")

        resource = urls.get(resource, None) # None is the default value if the key is not found

        print(f"Resource: {resource}")

        if method == 'POST':
            pass

        elif method == 'GET' and resource is not None:
            with open(f"{resource}", "rb") as f:
                # print(f"Resource: {resource}")
                headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"

                # Bonus
                if resource.endswith('.jpg'):
                    headers = "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n"
                if resource.endswith('.pdf'):
                    headers = "HTTP/1.1 200 OK\r\nContent-Type: application/pdf\r\nConnection: close\r\n\r\n"
                if resource.endswith('.mp4'):
                    headers = "HTTP/1.1 200 OK\r\nContent-Type: video/mp4\r\nConnection: close\r\n\r\n"
                if resource.endswith('.ico'):
                    headers = "HTTP/1.1 200 OK\r\nContent-Type: image/x-icon\r\nConnection: close\r\n\r\n"

                data = f.read()
                # headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"

                response = headers
                print(f'Length of response: {len(response)}')
                # print(f'Method: {method}')
                print(response)
                client_socket.sendall(response.encode()+data)
        else:
            headers = "HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n"
            response = headers + "<h1>404 Not Found</h1>"
            client_socket.sendall(response.encode())
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))

def start():
    server.listen()
    print(f"Listening on port {SERVER_PORT} ...")
    while True:
        client_socket, client_address = server.accept()
        print(f"Client socket: {client_socket}")
        print(f"Client address: {client_address}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
        thread.join()
        print(f"Thread name: {thread.name}")
        print(f"Thread ident: {thread.ident}")

start()