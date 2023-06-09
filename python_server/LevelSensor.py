import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the my_modules directory to sys.path
my_modules_path = os.path.join(current_dir, 'Komponente')
sys.path.append(my_modules_path)
class WaterLevelSensor:
    def __init__(self):
        self.level = 0
        self.max_level = 100
        self.min_level = 0

    def set_level(self, value):
        self.level = value

    def get_level(self):
        return self.level

    def reset(self):
        # Reset the flow rate to zero
        self.level = 0.0