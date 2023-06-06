from FlowSensor import WaterFlowSensor


class Dam:
    def __init__(self, id):
        self.id = id
        self.water_flow_sensor = WaterFlowSensor()

    def open_gate(self):
        self.water_flow_sensor.start()

    def close_gate(self):
        # Implement the logic to close the gate and stop releasing water
        # For example, you can control a motor or valve to close the gate

        # Stop reading the water flow rate
        self.water_flow_sensor.stop()

    def get_water_level(self):
        # Implement the logic to get the current water level in the dam
        # You can replace this with your actual implementation
        # For example, you can use a water level sensor or calculate it based on the flow rate

        # Update the water level based on the flow rate
        self.water_flow_sensor.get_flow_rate()
        self.water_level += self.water_flow_sensor.flow_rate

    def reset_water_level(self):
        # Reset the water level to zero
        self.water_level = 0.0