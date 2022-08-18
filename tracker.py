import pyautogui
import time


# timestamp of the start of recording is a part of the filename
ts = time.time()
file_name = "LOG_" + str(ts) + ".csv"
f = open(file_name, 'w')

f.write('time_stamp\tx\ty\n')

while True:
    currentMouseX, currentMouseY = pyautogui.position()
    ts = time.time()
    f.write("{ts}\t{x}\t{y}\n".format(ts = ts, x = currentMouseX, y = currentMouseY))