class MotorBike:

    total_call = 0

    def __init__(self):
        pass
    
    def go(self):
        print("ride on land")
        MotorBike.total_call += 1
        return MotorBike.total_call