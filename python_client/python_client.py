import socket
import os

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    #HOST, PORT = "192.168.10.10", 9999

    #LIST OF API CALLS
    get_flow = bytes("GET FLOW_SENSOR ALL").encode()
    get_temp = bytes("GET TEMPERATURE ALL").encode()
    get_stress = bytes("GET STRESS ALL").encode()

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))

        sock.sendall(get_flow)
        # Receive data from the server and shut down
        received = sock.recv(1024)
        print(received)

