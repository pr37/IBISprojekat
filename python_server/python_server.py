import datetime
import socketserver
from ScadaSimulator import ScadaSimulator
import traceback
import time

Scada_Simulator = ScadaSimulator()

class MyTCPHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        #self.Scada_Simulator = ScadaSimulator() # Create an instance of CustomClass
        super().__init__(request, client_address, server)

    def handle(self):
        # self.request is the TCP socket connected to the client
        has_error = False
        try:
            self.data = self.request.recv(1024).strip()
            self.data = bytes(self.data)
            print(datetime.datetime.now(), " - {} wrote:".format(self.client_address[0]))
            print(' data: ', str(self.data))
            text = self.data.decode().split(" ")


            if self.data.startswith(b'GET FLOW_SENSOR ALL'):
                self.get_flows()
            elif self.data.startswith(b'GET TEMPERATURE ALL'):
                self.get_temp()
            elif self.data.startswith(b'GET STRESS ALL'):
                self.get_stress()
            elif self.data.startswith(b'GET LEVEL_SENSOR ALL'):
                self.get_levels()
            elif self.data.startswith(b'GET PRESSURE_SENSOR ALL'):
                self.get_pressures()
            elif self.data.startswith(b'GET DAM STATE'):
                self.get_dam_state()
            elif self.data.startswith(b'GET VALVE_STATE ALL'):
                self.get_valve_states()
            elif self.data.startswith(b'GET PUMP_STATE ALL'):
                self.get_pump_states()
            elif self.data.startswith(b'CHANGE VALVE STATE BY ID'):
                self.set_valve_state(text[5], text[6])
            elif self.data.startswith(b'CHANGE PUMP STATE BY ID'):
                self.set_pump_state(text[5], text[6])
            elif self.data.startswith(b'SHUTDOWN'):
                self.set_dam_off()
            elif (text[0] == "SEND DAM ID FOR WATER LEVEL"):
                self.get_dam_id(text[1])
            elif (text[0] =="SEND DAM ID FOR PRESSURE"):
                self.get_dam_id1(text[1])
            elif (text[0] =="SEND DAM ID VALVE STATE"):
                self.get_valve_state(text[1])
            else:
                response = "Invalid request"

            #send_data = response.encode()
            #self.request.sendall(send_data)

        except Exception as e:
            print('Exception occurred in handle:')
            traceback.print_exc()

    def get_flows(self):
        response = Scada_Simulator.get_all_flow_sensors()
        print(response)
        self.send_response(response)

    def get_pump_states(self):
        response = Scada_Simulator.get_all_pumps()
        print(response)
        self.send_response(response)

    def get_temp(self):
        response = Scada_Simulator.get_all_temperatures()
        print(response)
        self.send_response(response)

    def get_dam_state(self):
        response = ""
        for i in range(4):
            indx = i+1
            response += Scada_Simulator.get_dam_state(indx) + " "
        print(response)
        self.send_response(response)

    def get_levels(self):
        response = Scada_Simulator.get_all_level_sensors()
        print(response)
        self.send_response(response)
    def get_dam_id(self,id_dam):
        response = Scada_Simulator.get_specific_level_sensor(id_dam)
        print(response)
        self.send_response(response)
    def get_dam_id1(self,id_dam):
        response = Scada_Simulator.get_specific_pressure_sensor(id_dam)
        print(response)
        self.send_response(response)

    def get_valve_state(self, id_dam):
        response = Scada_Simulator.get_specific_valve_state(id_dam)
        print(response)
        self.send_response(response)

    def get_valve_states(self):
        response = Scada_Simulator.get_all_valve_states()
        print(response)
        self.send_response(response)

    def get_pressures(self):
        response = Scada_Simulator.get_all_pressure_sensors()
        print(response)
        self.send_response(response)

    def set_valve_state(self, id_dam, valve_state):
        Scada_Simulator.set_valve_state(id_dam, valve_state)
        print("OK...." + id_dam + " " + valve_state)

    def set_pump_state(self, id_dam, pump_state):
        Scada_Simulator.set_pump_state(id_dam, pump_state)
        print("OK....")

    def get_stress(self):
        response = Scada_Simulator.get_all_stresses()
        print(response)
        self.send_response(response)

    def set_dam_off(self):
        Scada_Simulator.shut_down()

    def send_response(self, response):
        send_data = response.encode()
        self.request.sendall(send_data)

       
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:

        server.serve_forever()
        
        