#Created by CHCreations and ChadHendrixs
#Not to be sold; This software is free to use
#If you've paid for this software, or see it being sold anywhere,
#Please contact us at once.

import os
import psutil
from time import sleep
from playsound import playsound


global check
check = psutil.sensors_battery()

def loop():
    while True:
        sleep(2)
        value = psutil.sensors_battery()
        try:
            check = new_check
        except Exception as e:
            print(e)
        update_check(value, check)

def update_check(value, check):
    if value.percent < 30:
        if value.power_plugged == False:
            playsound('sounds\\low_battery.mp3')
    if value.percent == 100:
        if value.power_plugged:
            playsound('sounds\\low_battery.mp3')
    if value == check:
        pass
    else:
        update_status(check)
        check = psutil.sensors_battery()
        return

def calculate_length(num):
     x = num
     y = 0
     while True:
         if x == 0:
                 return(y)
                 break
         else:
                 y = y+1
                 x = x-5

def play_sounds(status, value):
    if status:
        if value:
            playsound('sounds\\plugged_in.mp3')
        else:
            playsound('sounds\\unplugged.mp3')
    else:
        pass

def update_status(check):
    os.system('cls||clear')
    sleep(3)
    x = check.percent
    for y in range(5):
        if (x-y) % 5 == 0:
            calc = x-y
            bar_value = calculate_length(calc)
        else:
            pass
    bar_print = '('
    
    for x in range(bar_value):
        bar_print = bar_print + '='
    
    bar_calc = len(bar_print)
    for x in range(abs(bar_calc-20)):
        bar_print = bar_print+' '

    bar_print = bar_print+")"
    
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged==False:
        plugged="Not Plugged In"
    elif plugged:
        plugged="Plugged In"

    print("Battery:", percent+"%", bar_print, "\nCharger:", plugged)
    
    noti_value = check.power_plugged
    value = battery.power_plugged
    if noti_value == value:
        noti_status = False
    else:
        noti_status = True

    play_sounds(noti_status, value)
    
    global new_check
    new_check = psutil.sensors_battery()
    return

update_status(check)
loop()