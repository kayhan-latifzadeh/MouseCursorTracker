#!/usr/bin/env python3
# coding: utf-8

'''
Mouse cursor tracking

Dependencies:
- pyautogui

Authors:
- Kayhan Latifzadeh <name.surname@uni.lu>
- Luis Leiva <name.surname@uni.lu>
'''


# Load std libs.
import time
import argparse
import os

parser = argparse.ArgumentParser(description='Record mouse cursor position in real-time',
  formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--sampling_rate', default=60, type=int, help='sampling rate to record cursor position')


args = parser.parse_args()

# Load 3rd party libs.
import pyautogui

# timestamp of the start of recording is a part of the filename
ts = time.time()
file_name = "LOG_" + str(ts) + ".csv"
f = open(file_name, 'w')

# writing the header row
f.write('time_stamp\tx\ty\n')

try:
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        ts = time.time()
        sample = "{ts}\t{x}\t{y}\n".format(ts = ts, x = currentMouseX, y = currentMouseY)
        f.write(sample)
        time.sleep(1/args.sampling_rate)
except KeyboardInterrupt:
    f.close()
    print("\nThe data has been saved, path to the file:", os.path.realpath(f.name))
    exit(0)
    