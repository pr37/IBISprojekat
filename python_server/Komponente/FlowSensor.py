
class WaterFlowSensor:
    def __init__(self):
        self.flow_rate = 0.0
        self.max_flow = 100 # 100 l po sekundi
        self.min_flow = 0 #zavrnuto

    def set_flow_rate(self, value):
        self.flow_rate = value

    def set_flow_rate(self):
        return self.flow_rate

    def reset(self):
        # Reset the flow rate to zero
        self.flow_rate = 0.0
