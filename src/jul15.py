from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Icon

hub = PrimeHub()

m_left = Motor(Port.C)
m_right = Motor(Port.D)

# Initialize the sensor.
eyes = UltrasonicSensor(Port.F)

def stop():
    m_left.run(0)
    m_right.run(0)
    # To make sure motor stops
    wait(100)

def go(vel:float):
    m_left.run(-vel)
    m_right.run(vel)

def go_for(vel:float,ms:int):
    go(vel)
    wait(ms)

def rot(deg:float):
    m_left.run(deg*4)
    m_right.run(deg*4)
    wait(500)

def measure()->float:
    assert eyes.distance() > 1000
    init_pos, final_pos = 0, 0
    while eyes.distance() > 1000:
        go(100)
    init_pos = m_left.angle()
    while eyes.distance() < 1000:
        go(100)
    final_pos = m_left.angle()
    return float(abs(final_pos-init_pos))/360*160

length = measure()
go_for(100,5000)
stop()
rot(-90)
go_for(-100,1000)
width = measure()
print(f"(length, width) = ({length}mm, {width}mm)")
