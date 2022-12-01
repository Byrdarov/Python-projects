import socket
import threading

HOST='127.0.0.1'
PORT=1234          #RANGE OF PORT IS FORM 0 to 65535
LISTENER_LIMIT = 5
active_clients=[] #list of all connected users
#function to send any new message to all the clients that are currently conncected to the server!
#listen for any upcoming messages
def listen_for_messages(client,username):

    while 1:
        message=client.recv(2048).decode('utf-8')
        if message!='':

            final_msg=username +'~'+ message
            send_messages_to_all(final_msg)
        else:
            print(f"The message from client {username} is empty")
#function to send message to single client

def send_message_to_client(client,message):
    client.sendall(message.encode())


def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)



#function to handle clients:
def client_handler(client):
    #server will listen for client messages that contains the user's username
    while 1:
        username=client.recv(2048).decode('utf-8')
        if username!='':
            prompt_message="SERVER~"+f"{username} entered the chat"
            send_messages_to_all(prompt_message)
            active_clients.append((username,client))
            break

        else:
            print("Client username is empty")
    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


#main function
def main():
    #af net:we are going to use IPv4dresses
    #sock_stream: we are using the TCP packets for communication
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        #provide the server with an adress in the form of host and port
        server.bind((HOST,PORT))
        print("Running the server")
    except:
        print(f"Unable to bind to host{HOST} and port{PORT}")

    #set server limit:
    server.listen(LISTENER_LIMIT)

    #this will keep listening for client conncetions:
    while 1:

        client,adress=server.accept()

        print(f"Successfully connected to client {adress[0]} {adress[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()


if __name__=='__main__':
    main()

