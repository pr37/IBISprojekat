from Komponente.Dam import Dam
import time

class ScadaSimulator:
    def __init__(self):
        self.Dam1 = Dam("1")
        self.Dam2 = Dam("2")
        self.Dam3 = Dam("3")
        self.Dam4 = Dam("4")

    def simulate_startup(self):
        self.Dam1.open_gate()
        self.Dam1.water_flow_sensor.flow_rate = 10

        self.Dam2.open_gate()
        self.Dam2.water_flow_sensor.flow_rate = 10

        self.Dam3.open_gate()
        self.Dam3.water_flow_sensor.flow_rate = 10

        self.Dam4.open_gate()
        self.Dam4.water_flow_sensor.flow_rate = 10

        self.simulate_all_sensors()
        self.simulate_all_actuators()

    #sva ocitavanja se rade na 2 sekunde tako da sve moze ovde
    def simulate_all_sensors(self):
        #ovde treba neku logiku dodati za zavisnost od pumpe
        if (self.Dam1.water_flow_sensor.flow_rate < self.Dam1.water_flow_sensor.max_flow):
            self.Dam1.water_flow_sensor.flow_rate += 5
        else:
            self.Dam1.water_flow_sensor.flow_rate = 0
        time.sleep(2)

    def simulate_all_actuators(self):
        pass