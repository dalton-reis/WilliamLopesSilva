import time
import py_qmc5883l

sensor = py_qmc5883l.QMC5883L()

while True:
    sensor.declination = -19.3
    sensor.get_data()
    print(sensor.get_bearing())
    if sensor.get_bearing() > 337.25 or sensor.get_bearing() < 22.5:
        print("Norte")
    elif sensor.get_bearing() > 292.5 and sensor.get_bearing() < 337.25:
        print("Norte-oeste")
    elif sensor.get_bearing() > 247.5 and sensor.get_bearing() < 292.5:
        print("Oeste")
    elif sensor.get_bearing() > 202.5 and sensor.get_bearing() < 247.5:
        print("Sul-oeste")
    elif sensor.get_bearing() > 157.5 and sensor.get_bearing() < 202.5:
        print("Sul")
    elif sensor.get_bearing() > 112.5 and sensor.get_bearing() < 157.5:
        print("Sul-leste")
    elif sensor.get_bearing() > 67.5 and sensor.get_bearing() < 112.5:
        print("Leste")
    elif sensor.get_bearing() > 22.5 and sensor.get_bearing() < 67.5:
        print("Norte-leste")
    time.sleep(0.1)
