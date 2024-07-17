from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from mylib import MyRobot

bot = MyRobot()

notes = ["C4/4","D4/4","E4/4","F4/4","G4/4"]
bot.music.update(notes)
bot.music.start()

state = "go_ahead"

def go_ahead():
    global bot, state
    bot.set_vel(100)
    bot.music.tick()
    if bot.color_sensor.color(True) == Color.WHITE:
        bot.hub.speaker.beep()
    if bot.force_pressed(3):
        bot.music.stop()
        state = "stopped"

def stopped():
    global bot, state
    bot.stop()
    bot.music.tick()
    if bot.force_pressed(3):
        bot.music.start()
        state = "go_ahead"


while True:
    handler = {
        "go_ahead": go_ahead,
        "stopped": stopped
    }
    handler[state]()
    wait(20)
    
