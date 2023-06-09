import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
from FlowSensor import WaterFlowSensor
import random
from LevelSensor import WaterLevelSensor
from PressureSensor import WaterPressureSensor
from Pump import WaterPump
from WaterTemperatureSensor import WaterTemperatureSensor

class Dam:
    def __init__(self, id):
        self.id = id
        self.water_flow_sensor = WaterFlowSensor()
        self.water_level_sensor = WaterLevelSensor()
        self.water_pressure_sensor = WaterPressureSensor()
        self.state = "inactive" #inactive, damaged, running
        self.valve_state = "closed" #opened, closed
        self.pump_state = "stop" #run, stop
        self.pump = WaterPump(id,random.randint(70, 100))
        self.water_temperature = WaterTemperatureSensor()


    def open_gate(self):
        if (self.state != "damaged"):
            self.state = "running"

    def close_gate(self):
        if (self.state != "damaged"):
            self.state = "inactive"

    def start_pump(self):
        if (self.state != "emergency shut down"):
            self.pump.start()
            self.pump_state = "run"

    def stop_pump(self):
        if (self.water_level_sensor.level >= 90):
            self.pump.start()
            self.pump_state = "run"
        elif (self.water_level_sensor <= 10):
            self.pump.stop()
            self.pump_state = "stop"

    def get_pump_state(self):
        return self.pump.is_running

    def get_pump_state_str(self):
        if (self.pump.is_running):
            return " is running"
        else:
            return " not running"

    def set_pump_rate(self, value):
        self.pump.set_current_flow_rate(value)

    def get_water_flow(self):
        return self.water_flow_sensor.get_flow_rate()
        # if (self.state != "emergency shut down" or self.state != "damaged" or self.state != "inactive"):
        #     # Define the range around the previous number
        #     min_value = max(self.pum - 5, 0)
        #     max_value = min(self.water_flow_sensor.flow_rate + 5, 50)
        #
        #     # Generate a random number within the defined range
        #     new_number = random.randint(min_value, max_value)
        #
        #     # Update the previous number with the new number
        #     self.self.water_flow_sensor.flow_rate = new_number
        #     return self.self.water_flow_sensor.flow_rate

    def get_water_level(self):
        # return self.water_level_sensor.get_level()
        if (self.state != "emergency shut down" or self.state != "damaged" or self.state != "inactive"):
            # Define the range around the previous number
            min_value = max(self.water_level_sensor.level - 5, 0)
            max_value = min(self.water_level_sensor.level + 5, 100)

            # Generate a random number within the defined range
            new_number = random.randint(min_value, max_value)

            # Update the previous number with the new number
            self.water_level_sensor.level = new_number
            return self.water_level_sensor.level

    def get_water_pressure(self):
        if (self.state != "emergency shut down" or self.state != "damaged" or self.state != "inactive"):
            # Define the range around the previous number
            min_value = max(self.water_pressure_sensor.pressure - 5, 0)
            max_value = min(self.water_pressure_sensor.pressure + 5, 100)

            # Generate a random number within the defined range
            new_number = random.randint(min_value, max_value)

            # Update the previous number with the new number
            self.water_pressure_sensor.pressure = new_number
            return self.water_pressure_sensor.pressure

    def reset_water_level(self):
        self.water_flow_sensor.reset()

    def get_water_temperature(self):
        if (self.state != "emergency shut down" or self.state != "damaged" or self.state != "inactive"):
            # Define the range around the previous number
            min_value = max(self.water_temperature.temp - 5, -20)
            max_value = min(self.water_temperature.temp + 5, 40)

            # Generate a random number within the defined range
            new_number = random.randint(min_value, max_value)

            # Update the previous number with the new number
            self.water_temperature.temp = new_number
            return self.water_temperature.temp

    def get_valve_state(self):
        return self.valve_state

    def set_valve_state(self, new_valve_state):
        self.valve_state = new_valve_state

    def update_dam_state(self):
        if (self.state == "damaged"):
            return
        if (self.valve_state == "closed" and self.pump.is_running == False):
            self.state = "inactive"
        if (self.water_level_sensor.level > 90 or self.water_level_sensor.level < 10):
            self.state = "inactive"
        if (self.get_water_temperature() < 0):
            self.state = "damaged"

    def massive_shut_down(self):
        self.state = "emergency shut down"
        self.pump.stop()
        self.valve_state = "closed"


