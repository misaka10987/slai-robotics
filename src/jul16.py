from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

from mylib import MyRobot

bot = MyRobot()

tar = 43

l_base, r_base = -50, 50

k_p,k_i,k_d = 2.0, 0.0, 2000.0

sum_err = 0
prev_err = 0

# Run the program indefinitely
while True:
    pass
    bot.hub.display.number(bot.color_sensor.reflection())
    err = bot.color_sensor.reflection() - tar
    sum_err += err
    diff = err - prev_err
    prev_err = err
    output = k_p * err + k_i * sum_err + k_d * diff
    
    l_out = l_base + output
    r_out = r_base + output
    
    bot.m_left.dc(l_out)
    bot.m_right.dc(r_out)

    wait(1)

