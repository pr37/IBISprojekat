import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
class WaterFlowSensor:
    def __init__(self):
        self.flow_rate = 0.0
        self.max_flow = 100 # 100 l po sekundi
        self.min_flow = 0 #zavrnuto

    def set_flow_rate(self, value):
        self.flow_rate = value

    def get_flow_rate(self):
        return self.flow_rate

    def reset(self):
        # Reset the flow rate to zero
        self.flow_rate = 0.0
