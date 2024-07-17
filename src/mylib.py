from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import umath

class MyRobot:
    hub: PrimeHub = PrimeHub()
    m_left: Motor = Motor(Port.C)
    m_right: Motor = Motor(Port.D)
    arm: Motor = Motor(Port.E)
    eyes: UltrasonicSensor = UltrasonicSensor(Port.F)
    color_sensor: ColorSensor = ColorSensor(Port.B)
    force_sensor: ForceSensor = ForceSensor(Port.A) 

    force_prev: float = 0

    def __init__(self):
        self.music = MusicPlayer(self.hub)
    
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
    
    def set_vel(self,vel:float)->MyRobot:
        vel = vel / 160 * 360
        self.m_left.run(-vel)
        self.m_right.run(vel)
        return self

    def go(self,x:float,y:float)->MyRobot:
        direction = umath.atan(y/x)
        distance = umath.sqrt()
    
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
    
    def force_pressed(self, thre:float = 3)->bool:
        force_curr = self.force_sensor.force()
        prev_pressed = self.force_prev >= thre
        curr_pressed = force_curr >= thre
        self.force_prev = force_curr
        if prev_pressed and not curr_pressed:
            return True
        else:
            return False

class MusicPlayer:
    note: list[str] = []
    watch: StopWatch = StopWatch()
    playing: bool = False

    def __init__(self, ref_hub: PrimeHub):
        self.ref_hub = ref_hub
    
    def update(self, note):
        self.note = [note for note in note]
    
    def start(self):
        self.playing = True
        self.watch.reset()
    
    def stop(self):
        self.playing = False
    
    def tick(self):
        if self.playing and self.watch.time() > 200:
            self.watch.reset()
            note = self.note.pop(0)
            self.note.append(note)
            self.ref_hub.speaker.play_notes([note])


class PIDUtil:
    def __init__(self,k_p:float,k_i:float,k_d:float,err,out):
        self.k_p=k_p
        self.k_i=k_i
        self.k_d=k_d
        self.err=err
        self.out=out
