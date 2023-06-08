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
        self.Dam1.water_level_sensor.level = 20;
        self.Dam1.water_pressure_sensor.pressure = 30;

        self.Dam2.open_gate()
        self.Dam2.water_flow_sensor.flow_rate = 10
        self.Dam2.water_level_sensor.level = 20;
        self.Dam2.water_pressure_sensor.pressure = 30;
        self.Dam2.valve_state = "open"

        self.Dam3.open_gate()
        self.Dam3.water_flow_sensor.flow_rate = 10
        self.Dam3.water_level_sensor.level = 20;
        self.Dam3.water_pressure_sensor.pressure = 30;

        self.Dam4.open_gate()
        self.Dam4.water_flow_sensor.flow_rate = 10
        self.Dam4.water_level_sensor.level = 20;
        self.Dam4.water_pressure_sensor.pressure = 30;


    #sva ocitavanja se rade na 2 sekunde tako da sve moze ovde
    def simulate_all_sensors(self):
        #ovde treba neku logiku dodati za zavisnost od pumpe
        if (self.Dam1.water_flow_sensor.flow_rate < self.Dam1.water_flow_sensor.max_flow):
            self.Dam1.water_flow_sensor.flow_rate += 5
        else:
            self.Dam1.water_flow_sensor.flow_rate = 0

    def get_stress_values(self, dam):
        if dam < 0:
            return "Water Stress is 10"
        elif dam > 0:
            return "Water Stress is 25"


    def get_all_flow_sensors(self):
        strret = "DAM1 FLOW SENSOR: " + str(self.Dam1.get_water_flow()) + "\n" + \
                 "DAM2 FLOW SENSOR: " + str(self.Dam2.get_water_flow()) + "\n" + \
                 "DAM3 FLOW SENSOR: " + str(self.Dam3.get_water_flow()) + "\n" +  \
                 "DAM4 FLOW SENSOR: " + str(self.Dam4.get_water_flow()) + "\n"
        return  strret
    def get_all_level_sensors(self):
        strret  = "DAM1 LEVEL SENSOR: " + str(self.Dam1.get_water_level()) + "\n" + \
                 "DAM2 LEVEL SENSOR: " + str(self.Dam2.get_water_level()) + "\n" + \
                 "DAM3 LEVEL SENSOR: " + str(self.Dam3.get_water_level()) + "\n" +  \
                 "DAM4 LEVEL SENSOR: " + str(self.Dam4.get_water_level()) + "\n"
        return strret

    def get_specific_level_sensor(self, id_dam):
            if(id_dam =="1"):
                strret  = "DAM1 LEVEL SENSOR: " + str(self.Dam1.get_water_level()) + "\n"
            elif(id_dam =="2"):
                strret = "DAM2 LEVEL SENSOR: " + str(self.Dam2.get_water_level()) + "\n"
            elif(id_dam == "3"):
                strret = "DAM3 LEVEL SENSOR: " + str(self.Dam3.get_water_level()) + "\n"
            elif(id_dam == "4"):
                strret = "DAM4 LEVEL SENSOR: " + str(self.Dam4.get_water_level()) + "\n"
            else:
                strret = "Uneli ste pogresan id"

            return strret
    def get_specific_pressure_sensor(self, id_dam1):
            if(id_dam1 =="1"):
                strret  = "DAM1 PRESSURE SENSOR: " + str(self.Dam1.get_water_pressure()) + "\n"
            elif(id_dam1 =="2"):
                strret = "DAM2 PRESSURE SENSOR: " + str(self.Dam2.get_water_pressure()) + "\n"
            elif(id_dam1 == "3"):
                strret = "DAM3 PRESSURE SENSOR: " + str(self.Dam3.get_water_pressure()) + "\n"
            elif(id_dam1 == "4"):
                strret = "DAM4 PRESSURE SENSOR: " + str(self.Dam4.get_water_pressure()) + "\n"
            else:
                strret = "Uneli ste pogresan id"

            return strret

    def get_specific_valve_state(self, id_dam):
        if (id_dam == "1"):
            strret = "DAM1 VALVE STATE: " + str(self.Dam1.get_valve_state()) + "\n"
        elif (id_dam == "2"):
            strret = "DAM2 VALVE STATE: " + str(self.Dam2.get_valve_state()) + "\n"
        elif (id_dam == "3"):
            strret = "DAM3 VALVE STATE: " + str(self.Dam3.get_valve_state()) + "\n"
        elif (id_dam == "4"):
            strret = "DAM4 VALVE STATE: " + str(self.Dam4.get_valve_state()) + "\n"
        else:
            strret = "Uneli ste pogresan id"

        return strret

    def set_valve_state(self, id_dam, valve_state):
        if (id_dam == "1"):
            self.Dam1.set_valve_state(valve_state)
            strret = "DAM1 VALVE STATE: " + str(self.Dam1.get_valve_state()) + "\n"
        elif (id_dam == "2"):
            self.Dam2.set_valve_state(valve_state)
            strret = "DAM2 VALVE STATE: " + str(self.Dam2.get_valve_state()) + "\n"
        elif (id_dam == "3"):
            self.Dam3.set_valve_state(valve_state)
            strret = "DAM3 VALVE STATE: " + str(self.Dam3.get_valve_state()) + "\n"
        elif (id_dam == "4"):
            self.Dam4.set_valve_state(valve_state)
            strret = "DAM4 VALVE STATE: " + str(self.Dam4.get_valve_state()) + "\n"
        else:
            strret = "Uneli ste pogresan id"

        return strret

    def get_all_pressure_sensors(self):
        strret = "DAM1 PRESSURE SENSOR: " + str(self.Dam1.get_water_pressure()) + "\n" + \
                 "DAM2 PRESSURE SENSOR: " + str(self.Dam2.get_water_pressure()) + "\n" + \
                 "DAM3 PRESSURE SENSOR: " + str(self.Dam3.get_water_pressure()) + "\n" +  \
                 "DAM4 PRESSURE SENSOR: " + str(self.Dam4.get_water_pressure()) + "\n"
        return strret

    def get_all_temperatures(self):
        strret = "DAM1 WATER TEMPERATURE: " + str(self.Dam1.get_water_temperature()) + "\n" + \
                 "DAM2 WATER TEMPERATURE: " + str(self.Dam2.get_water_temperature()) + "\n" + \
                 "DAM3 WATER TEMPERATURE: " + str(self.Dam3.get_water_temperature()) + "\n" + \
                 "DAM4 WATER TEMPERATURE: " + str(self.Dam4.get_water_temperature()) + "\n"
        return strret

    def get_all_stresses(self):
        strret = "DAM1 STRESS: " + str(self.get_stress_values(self.Dam1.get_water_temperature())) + "\n" + \
                 "DAM2 STRESS: " + str(self.get_stress_values(self.Dam2.get_water_temperature())) + "\n" + \
                 "DAM3 STRESS: " + str(self.get_stress_values(self.Dam3.get_water_temperature())) + "\n" + \
                 "DAM4 STRESS: " + str(self.get_stress_values(self.Dam4.get_water_temperature())) + "\n"
        return strret
    def simulate_all_actuators(self):
        pass

    def manual_change_pump(self,dam_id,value):
        pass