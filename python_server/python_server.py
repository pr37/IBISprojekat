import datetime
import socketserver
from ScadaSimulator import ScadaSimulator
import traceback
import time


class MyTCPHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.Scada_Simulator = ScadaSimulator() # Create an instance of CustomClass
        super().__init__(request, client_address, server)

    def handle(self):
        # self.request is the TCP socket connected to the client
        has_error = False
        try:
            self.data = self.request.recv(1024).strip()
            self.data = bytes(self.data)
            print(datetime.datetime.now(), " - {} wrote:".format(self.client_address[0]))
            print(' data: ', str(self.data))

            if self.data.startswith(b'GET FLOW_SENSOR ALL'):
                self.get_flows()
            else:
                response = "Invalid request"

            send_data = response.encode()
            self.request.sendall(send_data)

        except Exception as e:
            print('Exception occurred in handle:')
            traceback.print_exc()

    def get_flows(self):
        response = self.Scada_Simulator.get_all_flow_sensors()
        print(response)
        self.send_response(response)

    def send_response(self, response):
        send_data = response.encode()
        self.request.sendall(send_data)

       
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:

        server.serve_forever()
        
        