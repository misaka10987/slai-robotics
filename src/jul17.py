from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task

from mylib import MyRobot

bot = MyRobot()

go_ahead = True
play_music = True

music_note = ["C4/4","D4/4","E4/4","F4/4","G4/4"]

async def go_ahead():
    global bot, go_ahead
    while True:
        if go_ahead:
            bot.set_vel(100)
        else:
            bot.stop()
        await wait(20)


async def read_force():
    global bot, go_ahead
    while True:
        if await bot.force_pressed(3):
            go_ahead = not go_ahead
        await wait(20)


async def detect_paper():
    global bot, go_ahead, play_music
    while True:
        # bot.hub.display.number(await bot.color_sensor.reflection() % 100)
        if go_ahead and await bot.color_sensor.color(True) == Color.WHITE:
            play_music = False
            await bot.hub.speaker.beep()
        else:
            play_music = True
        await wait(20)

async def play_music():
    global bot, play_music, music_note
    while True:
        if play_music:
            note = music_note.pop(0)
            music_note.append(note)
            await bot.hub.speaker.play_notes([note])
        await wait(200)

async def main():
    await multitask(go_ahead(), read_force(), detect_paper(), play_music())

run_task(main())
