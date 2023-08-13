import socket
import threading
from urls import *
from mimeType import *

SERVER_HOST = 'localhost'
SERVER_PORT = 8080

def handle_client(client_socket):
    try:
        msg = client_socket.recv(1024).decode() #receive data from client
        method = msg.split(' ')[0] #get the method type from the request like GET, POST, etc.
        resource = msg.split(' ')[1] #get the resource like /index.html, /about.html, etc.

        resource = urls.get(resource, None) #get the resource from the urls.py file

        if method == 'POST':
            # as the message is in the form of a query string, we need to parse it to get the user value
            # the user value is the value of the user parameter so we need to find the index of the user parameter
            user_index = msg.find('user=')
            if user_index != -1:
                user_end_index = msg.find('&', user_index)
                if user_end_index == -1:
                    user_end_index = len(msg)
                user_value = msg[user_index + 5:user_end_index] 
            
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"

            if user_value:
                # as the user is like 'value+value+value' so we need to replace the + with a space
                decode_user = user_value.replace('+', ' ') 
                response_body = f"<h1>Posted Message:</h1><p>{decode_user}</p>"
            else:
                response_body = f"<h1>No User parameter found in the request</h1>"

            response = response_header + response_body
            client_socket.sendall(response.encode()) #send the response to the client

        elif method == 'GET' and resource is not None:
            # Determine the file extension
            file_extension = resource[resource.rfind('.'):].lower()

            # Retrieve the content type from the mime_types dictionary
            content_type = mime_types.get(file_extension, 'application/octet-stream')

            headers = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nConnection: close\r\n\r\n"

            # Open the requested resource file and read its data
            with open(resource, "rb") as f:
                data = f.read()

            response = headers.encode() + data 

            print(f"Length of response: {len(response)}")
            print(f"Length of response with header: {len(response)-len(headers)}")
            print(f"Method: {method}")
            client_socket.sendall(response)
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