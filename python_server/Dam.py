import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
from FlowSensor import WaterFlowSensor


class Dam:
    def __init__(self, id):
        self.id = id
        self.water_flow_sensor = WaterFlowSensor()
        self.state = "inactive" #inactive, damaged, running

    def open_gate(self):
        self.state = "running"

    def close_gate(self):
        self.state = "inactive"

    def get_water_flow(self):
        return self.water_flow_sensor.get_flow_rate()

    def reset_water_level(self):
        self.water_flow_sensor.reset()