from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class MyRobot:
    def __init__(self):
        self.hub = PrimeHub()
        self.m_left = Motor(Port.C)
        self.m_right = Motor(Port.D)
        self.arm = Motor(Port.E)
        self.eyes = UltrasonicSensor(Port.F)
    
    def ultrasonic(self)->float:
        return self.eyes.distance()
    
    def brake(self)->MyRobot:
        self.m_left.brake()
        self.m_right.brake()
        wait(200)
        return self
    
    def stop(self)->MyRobot:
        self.m_left.stop()
        self.m_right.stop()
        wait(200)
        return self

    def go(self,vel:float)->MyRobot:
        self.m_left.run(-vel)
        self.m_right.run(vel)
        return self
    
    def go_for(self,vel:float,time:int)->MyRobot:
        self.go(vel)
        wait(time)
        return self
    
    def rot(self,deg:float):
        self.m_left.run(deg*4)
        self.m_right.run(deg*4)
        wait(500)
        return self
    
    def arm_up(self)->MyRobot:
        self.arm.run(200)
        wait(500)
        return self

    def arm_down(self)->MyRobot:
        self.arm.run(-200)
        wait(500)
        return self
