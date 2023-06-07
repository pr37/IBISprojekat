import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
sys.path.append(current_dir)
from Dam import Dam
import time


class ScadaSimulator:
    def __init__(self):
        self.Dam1 = Dam("1")
        self.Dam2 = Dam("2")
        self.Dam3 = Dam("3")
        self.Dam4 = Dam("4")
        self.simulate_startup()

    def simulate_startup(self):
        self.Dam1.open_gate()
        self.Dam1.water_flow_sensor.flow_rate = 10

        self.Dam2.open_gate()
        self.Dam2.water_flow_sensor.flow_rate = 10

        self.Dam3.open_gate()
        self.Dam3.water_flow_sensor.flow_rate = 10

        self.Dam4.open_gate()
        self.Dam4.water_flow_sensor.flow_rate = 10


    #sva ocitavanja se rade na 2 sekunde tako da sve moze ovde
    def simulate_all_sensors(self):
        #ovde treba neku logiku dodati za zavisnost od pumpe
        if (self.Dam1.water_flow_sensor.flow_rate < self.Dam1.water_flow_sensor.max_flow):
            self.Dam1.water_flow_sensor.flow_rate += 5
        else:
            self.Dam1.water_flow_sensor.flow_rate = 0

    def get_all_flow_sensors(self):
        strret = "DAM1 FLOW SENSOR: " + str(self.Dam1.get_water_flow()) + "\n" + \
                 "DAM2 FLOW SENSOR: " + str(self.Dam2.get_water_flow()) + "\n" + \
                 "DAM3 FLOW SENSOR: " + str(self.Dam3.get_water_flow()) + "\n" +  \
                 "DAM4 FLOW SENSOR: " + str(self.Dam4.get_water_flow()) + "\n"
        return  strret

    def get_all_temperatures(self):
        strret = "DAM1 WATER TEMPERATURE: " + str(self.Dam1.get_water_temperature()) + "\n" + \
                 "DAM2 WATER TEMPERATURE: " + str(self.Dam2.get_water_temperature()) + "\n" + \
                 "DAM3 WATER TEMPERATURE: " + str(self.Dam3.get_water_temperature()) + "\n" + \
                 "DAM4 WATER TEMPERATURE: " + str(self.Dam4.get_water_temperature()) + "\n"
        return strret

    def simulate_all_actuators(self):
        pass

    def manual_change_pump(self,dam_id,value):
        pass