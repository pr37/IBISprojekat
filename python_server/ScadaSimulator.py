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
        # self.simulate_startup()
        self.simulate_all_sensors()
        self.simulate_all_actuators()

    def simulate_startup(self):
        self.Dam1.open_gate()
        self.Dam1.water_flow_sensor.flow_rate = 10
        self.Dam1.water_level_sensor.level = 20;
        self.Dam1.water_pressure_sensor.pressure = 30;
        self.Dam1.valve_state = "open"

        self.Dam2.open_gate()
        self.Dam2.water_flow_sensor.flow_rate = 10
        self.Dam2.water_level_sensor.level = 20;
        self.Dam2.water_pressure_sensor.pressure = 30;
        self.Dam2.valve_state = "open"

        self.Dam3.open_gate()
        self.Dam3.water_flow_sensor.flow_rate = 10
        self.Dam3.water_level_sensor.level = 20;
        self.Dam3.water_pressure_sensor.pressure = 30;
        self.Dam3.valve_state = "open"

        self.Dam4.open_gate()
        self.Dam4.water_flow_sensor.flow_rate = 10
        self.Dam4.water_level_sensor.level = 20;
        self.Dam4.water_pressure_sensor.pressure = 30;
        self.Dam4.valve_state = "open"


    #sva ocitavanja se rade na 2 sekunde tako da sve moze ovde
    def simulate_all_sensors(self):
        self.Dam1.water_flow_sensor.flow_rate = self.Dam1.pump.current_flow_rate
        self.Dam2.water_flow_sensor.flow_rate = self.Dam2.pump.current_flow_rate
        self.Dam3.water_flow_sensor.flow_rate = self.Dam3.pump.current_flow_rate
        self.Dam4.water_flow_sensor.flow_rate = self.Dam4.pump.current_flow_rate

        if (self.Dam1.valve_state == "closed" and self.Dam1.pump.is_running == False):
            if (self.Dam1.water_level_sensor.level <= self.Dam1.water_level_sensor.max_level):
                self.Dam1.water_level_sensor.level += 20
                self.Dam1.water_pressure_sensor.pressure += 20
        elif(self.Dam1.valve_state == "open"):
            if (self.Dam1.pump.is_running):
                self.Dam1.water_level_sensor.level += 5
                self.Dam1.water_pressure_sensor.pressure += 5
            elif(self.Dam1.pump.is_running == False):
                self.Dam1.water_level_sensor.level -= 5
                self.Dam1.water_pressure_sensor.pressure -= 5
        if (self.Dam2.valve_state == "closed" and self.Dam2.pump.is_running == False):
            if (self.Dam2.water_level_sensor.level <= self.Dam2.water_level_sensor.max_level):
                self.Dam2.water_level_sensor.level += 20
                self.Dam2.water_pressure_sensor.pressure += 20
        elif(self.Dam2.valve_state == "open"):
            if (self.Dam2.pump.is_running):
                self.Dam2.water_level_sensor.level += 5
                self.Dam2.water_pressure_sensor.pressure += 5
            elif(self.Dam2.pump.is_running == False):
                self.Dam2.water_level_sensor.level -= 5
                self.Dam2.water_pressure_sensor.pressure -= 5
        if (self.Dam3.valve_state == "closed" and self.Dam3.pump.is_running == False):
            if (self.Dam3.water_level_sensor.level <= self.Dam3.water_level_sensor.max_level):
                self.Dam3.water_level_sensor.level += 20
                self.Dam3.water_pressure_sensor.pressure += 20
        elif(self.Dam3.valve_state == "open"):
            if (self.Dam3.pump.is_running):
                self.Dam3.water_level_sensor.level += 5
                self.Dam3.water_pressure_sensor.pressure += 5
            elif(self.Dam3.pump.is_running == False):
                self.Dam3.water_level_sensor.level -= 5
                self.Dam3.water_pressure_sensor.pressure -= 5
        if (self.Dam4.valve_state == "closed" and self.Dam4.pump.is_running == False):
            if (self.Dam4.water_level_sensor.level <= self.Dam4.water_level_sensor.max_level):
                self.Dam4.water_level_sensor.level += 20
                self.Dam4.water_pressure_sensor.pressure += 20
        elif(self.Dam4.valve_state == "open"):
            if (self.Dam4.pump.is_running):
                self.Dam4.water_level_sensor.level += 5
                self.Dam4.water_pressure_sensor.pressure += 5
            elif(self.Dam4.pump.is_running == False):
                self.Dam4.water_level_sensor.level -= 5
                self.Dam4.water_pressure_sensor.pressure -= 5


    def get_stress_values(self, waterTemperature, waterPressure, waterLevel):
        if waterTemperature < 0:
            return " is stressed"
        elif waterTemperature > 0:
            return "is not stressed"
        if waterPressure > 30:
            return "is stressed"
        elif waterPressure < 30:
            return "is not stressed"
        if waterLevel > 30:
            return "is stressed"
        elif waterLevel < 30:
            return "is not stressed"


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

    def get_all_valve_states(self):
        strret = "DAM1 VALVE STATE: " + str(self.Dam1.get_valve_state()) + "\n"
        strret += "DAM2 VALVE STATE: " + str(self.Dam2.get_valve_state()) + "\n"
        strret += "DAM3 VALVE STATE: " + str(self.Dam3.get_valve_state()) + "\n"
        strret += "DAM4 VALVE STATE: " + str(self.Dam4.get_valve_state()) + "\n"
        return strret

    def get_all_pumps(self):
        strret = "DAM1 PUMP STATE: " + str(self.Dam1.get_pump_state_str()) + "\n"
        strret += "DAM2 PUMP STATE: " + str(self.Dam2.get_pump_state_str()) + "\n"
        strret += "DAM3 PUMP STATE: " + str(self.Dam3.get_pump_state_str()) + "\n"
        strret += "DAM4 PUMP STATE: " + str(self.Dam4.get_pump_state_str()) + "\n"
        return strret

    def set_valve_state(self, id_dam, valve_state):
        if (id_dam == "Dam1"):
            self.Dam1.set_valve_state(valve_state)
        elif (id_dam == "Dam2"):
            self.Dam2.set_valve_state(valve_state)
        elif (id_dam == "Dam3"):
            self.Dam3.set_valve_state(valve_state)
        elif (id_dam == "Dam4"):
            self.Dam4.set_valve_state(valve_state)

    def set_pump_state(self, id_dam, pump_state):
        if (id_dam == "Dam1"):
            if (pump_state == "run"):
                self.Dam1.pump.start()
            else:
                self.Dam1.pump.stop()
        elif (id_dam == "Dam2"):
            if (pump_state == "run"):
                self.Dam2.pump.start()
            else:
                self.Dam2.pump.stop()
        elif (id_dam == "Dam3"):
            if (pump_state == "run"):
                self.Dam3.pump.start()
            else:
                self.Dam3.pump.stop()
        elif (id_dam == "Dam4"):
            if (pump_state == "run"):
                self.Dam4.pump.start()
            else:
                self.Dam4.pump.stop()


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
        strret = "DAM1 STRESS: " + str(self.get_stress_values(self.Dam1.get_water_temperature(),
                                                              self.Dam1.get_water_pressure(),
                                                              self.Dam1.get_water_level())) + "\n" + \
                 "DAM2 STRESS: " + str(self.get_stress_values(self.Dam2.get_water_temperature(),
                                                              self.Dam2.get_water_pressure(),
                                                              self.Dam2.get_water_level())) + "\n" + \
                 "DAM3 STRESS: " + str(self.get_stress_values(self.Dam3.get_water_temperature(),
                                                              self.Dam3.get_water_pressure(),
                                                              self.Dam3.get_water_level()
                                                              )) + "\n" + \
                 "DAM4 STRESS: " + str(self.get_stress_values(self.Dam4.get_water_temperature(),
                                                              self.Dam4.get_water_pressure(),
                                                              self.Dam4.get_water_level()
                                                              )) + "\n"
        return strret
    def simulate_all_actuators(self):
        pass

    def manual_change_pump(self,dam_id,value):
        if (dam_id == 1):
            self.Dam1.pump.is_running = value
        elif (dam_id == 2):
            self.Dam2.pump.is_running = value
        elif (dam_id == 3):
            self.Dam3.pump.is_running = value
        elif (dam_id == 4):
            self.Dam4.pump.is_running = value

    def manual_change_valve(self,dam_id,value):
        if (dam_id == 1):
            self.Dam1.valve_state = value
        elif (dam_id == 2):
            self.Dam2.valve_state = value
        elif (dam_id == 3):
            self.Dam3.valve_state = value
        elif (dam_id == 4):
            self.Dam4.valve_state = value


    def get_dam_state(self,id_dam):
        self.Dam1.update_dam_state()
        self.Dam2.update_dam_state()
        self.Dam3.update_dam_state()
        self.Dam4.update_dam_state()
        if (id_dam == 1):
            return self.Dam1.state
        elif (id_dam == 2):
            return self.Dam2.state
        elif (id_dam == 3):
            return self.Dam3.state
        elif (id_dam == 4):
            return self.Dam4.state
        else:
            strret = "Uneli ste pogresan id"

    def shut_down(self):
        self.Dam1.massive_shut_down()
        self.Dam2.massive_shut_down()
        self.Dam3.massive_shut_down()
        self.Dam4.massive_shut_down()
