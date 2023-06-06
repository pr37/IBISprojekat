import datetime
import socketserver
from Komponente
import time

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        has_error = False
        try:
            self.data = self.request.recv(1024).strip()
            self.data = bytes(self.data)
            print(datetime.datetime.now(), " - {} wrote:".format(self.client_address[0]))
            print(' data: ', str(self.data))
            
            server_hello = "Python Server is up and running."
            send_data = server_hello.to_bytes()
            self.request.sendall(send_data)
        except:
            print('Exception occurred in handle.')
       
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
        
        