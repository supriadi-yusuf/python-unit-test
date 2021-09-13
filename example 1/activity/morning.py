
from vehicles.bike import MotorBike

def refreshing():
   myBike = MotorBike()
   riding=myBike.go() 
   return riding

def refreshing2():
   myBike = MotorBike()
   myBike.go()

   myBike2 = MotorBike()
   riding = myBike2.go()  

   return riding