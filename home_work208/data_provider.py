from random import randint

def get_temperature(sensor):
    if sensor:
        return randint(-60,0)
    else:
        return randint(0, 50)

def get_pressure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)

def get_wind_speed(sensor):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)   