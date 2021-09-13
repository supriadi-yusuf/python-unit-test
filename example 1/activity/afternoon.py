from vehicles.plane import Plane

def fly():
    plane = Plane()
    try:
       plane.go()
    except Exception as e:
       return "error"

    return "success"