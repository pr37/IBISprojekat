import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))


class WaterPump:
    def __init__(self, pump_id, max_flow_rate):
        self.pump_id = pump_id
        self.max_flow_rate = max_flow_rate
        self.current_flow_rate = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.current_flow_rate = 5
            print(f"Water pump {self.pump_id} started.")
        else:
            print(f"Water pump {self.pump_id} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.current_flow_rate = 0
            print(f"Water pump {self.pump_id} stopped.")
        else:
            print(f"Water pump {self.pump_id} is already stopped.")



    def set_max_flow_rate(self, max_flow_rate):
        self.max_flow_rate = max_flow_rate
        print(f"Max flow rate for water pump {self.pump_id} set to {self.max_flow_rate}.")

    def set_current_flow_rate(self,val):
        self.current_flow_rate = val


