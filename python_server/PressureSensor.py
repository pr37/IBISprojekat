import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
class WaterPressureSensor:
    def __init__(self):
        self.pressure = 0.0
        self.max_pressure = 200
        self.min_pressure = 0 #

    def set_presssure(self, value):
        self.pressure = value

    def get_pressure(self):
        return self.pressure

    def reset(self):
        # Reset the flow rate to zero
        self.pressure = 0.0