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