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
            text = self.data.decode().split(",")


            if self.data.startswith(b'GET FLOW_SENSOR ALL'):
                self.get_flow
            elif self.data.startswith(b'GET TEMPERATURE ALL'):
                self.get_temp()
            elif self.data.startswith(b'GET STRESS ALL'):
                self.get_stress()
            elif self.data.startswith(b'GET LEVEL_SENSOR ALL'):
                self.get_levels()
            elif self.data.startswith(b'GET PRESSURE_SENSOR ALL'):
                self.get_pressures()
            elif self.data.startswith(b'SHUTDOWN'):
                self.set_dam_off(self.data)
            elif self.data.startswith(text[0].encode() =="SEND DAM ID"):
                self.get_dam_id(text[1])
            elif self.data.startswith(text[0].encode() =="SEND DAM ID FOR PRESSURE"):
                self.get_dam_id1(text[1])
            else:
                response = "Invalid request"

            #send_data = response.encode()
            #self.request.sendall(send_data)

        except Exception as e:
            print('Exception occurred in handle:')
            traceback.print_exc()

    def get_flows(self):
        response = self.Scada_Simulator.get_all_flow_sensors()
        print(response)
        self.send_response(response)

    def get_temp(self):
        response = self.Scada_Simulator.get_all_temperatures()
        print(response)
        self.send_response(response)

    def get_levels(self):
        response = self.Scada_Simulator.get_all_level_sensors()
        print(response)
        self.send_response(response)
    def get_dam_id(self,id_dam):
        response = self.Scada_Simulator.get_specific_level_sensor(id_dam)
        print(response)
        self.send_response(response)
    def get_dam_id1(self,id_dam1):
        response = self.Scada_Simulator.get_specific_pressure_sensor(id_dam1)
        print(response)
        self.send_response(response)

    def get_pressures(self):
        response = self.Scada_Simulator.get_all_pressure_sensors()
        print(response)
        self.send_response(response)

    def get_stress(self):
        response = self.Scada_Simulator.get_all_stresses()
        print(response)
        self.send_response(response)

    def set_dam_off(self,dam_id):
        if (dam_id == "SHUTDOWN Dam 1"):
            self.Scada_Simulator.Dam1.close_gate()
        elif (dam_id == "SHUTDOWN Dam 2"):
            self.Scada_Simulator.Dam2.close_gate()
        elif (dam_id == "SHUTDOWN Dam 3"):
            self.Scada_Simulator.Dam3.close_gate()
        elif (dam_id == "SHUTDOWN Dam 4"):
            self.Scada_Simulator.Dam4.close_gate()
        print(dam_id)

    def send_response(self, response):
        send_data = response.encode()
        self.request.sendall(send_data)

       
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:

        server.serve_forever()
        
        