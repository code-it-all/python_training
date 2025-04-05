class SmartHome:
    def __init__(self):
        self.lights_on = False
        self.fan_on = False

    def check_sensors(self, temperature, humidity, motion_detected):
        # Check temperature
        if temperature > 75:
            self.turn_on_fan()
        else:
            self.turn_off_fan()

        # Check humidity
        if humidity > 60:
            self.turn_on_dehumidifier()
        else:
            self.turn_off_dehumidifier()

        # Check motion
        if motion_detected:
            self.turn_on_lights()
        else:
            self.turn_off_lights()

    def turn_on_lights(self):
        if not self.lights_on:
            self.lights_on = True
            print("Lights are now ON.")
        else:
            print("Lights are already ON.")

    def turn_off_lights(self):
        if self.lights_on:
            self.lights_on = False
            print("Lights are now OFF.")
        else:
            print("Lights are already OFF.")

    def turn_on_fan(self):
        if not self.fan_on:
            self.fan_on = True
            print("Fan is now ON.")
        else:
            print("Fan is already ON.")

    def turn_off_fan(self):
        if self.fan_on:
            self.fan_on = False
            print("Fan is now OFF.")
        else:
            print("Fan is already OFF.")

    def turn_on_dehumidifier(self):
        print("Dehumidifier is now ON.")

    def turn_off_dehumidifier(self):
        print("Dehumidifier is now OFF.")