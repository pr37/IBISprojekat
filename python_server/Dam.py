import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
from FlowSensor import WaterFlowSensor
import random
from LevelSensor import WaterLevelSensor
from PressureSensor import WaterPressureSensor


class Dam:
    def __init__(self, id):
        self.id = id
        self.water_flow_sensor = WaterFlowSensor()
        self.water_level_sensor = WaterLevelSensor()
        self.water_pressure_sensor = WaterPressureSensor()
        self.state = "inactive" #inactive, damaged, running
        self.valve_state = "closed" #opened, closed

    def open_gate(self):
        self.state = "running"

    def close_gate(self):
        self.state = "inactive"

    def get_water_flow(self):
        return self.water_flow_sensor.get_flow_rate()

    def get_water_level(self):
        return self.water_level_sensor.get_level()

    def get_water_pressure(self):
        return self.water_pressure_sensor.get_pressure()

    def reset_water_level(self):
        self.water_flow_sensor.reset()

    def get_water_temperature(self):
        return random.randint(-10, 30)

    def get_valve_state(self):
        return self.valve_state
