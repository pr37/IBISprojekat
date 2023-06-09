import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
class WaterTemperatureSensor:
    def __init__(self):
        self.temp = 5
        self.max_temp = 40
        self.min_temp = -20

    def set_temp(self, value):
        self.temp = value

    def get_temp(self):
        return self.temp

    def reset(self):
        self.temp = 5

