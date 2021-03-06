# feature 3 - mean normalized x-accel

import math
import sys

WINDOW_LENGTH = 2.0

window_data = []
window_total = 0.0

def push_data(time, xaccel):
  global window_data, window_total
  window_data.append({ 'time': time, 'xaccel': xaccel })
  window_total += xaccel

def pop_data():
  global window_data, window_total
  head = window_data.pop(0)
  window_total -= head['xaccel']

def expire_data(window_end):
  global window_data, window_total
  window_begin = window_end - WINDOW_LENGTH
  while 1:
    head = window_data[0]
    if (head['time'] > window_begin):
      break
    pop_data()


def run_feature3(data):
  output = []
  for row in data:
    time = row[0]
    accel = [row[1], row[2], row[3]]
    accel_len = math.sqrt(accel[0]*accel[0] + accel[1]*accel[1] + accel[2]*accel[2])
    accel_normalized = [accel[0] / accel_len, accel[1] / accel_len, accel[2] / accel_len]

    # push new data to the window
    push_data(time, accel_normalized[0])

    # expire old data from the window
    expire_data(time)

    mean_zaccel = window_total / len(window_data)
    output.append([time, mean_zaccel])
  return output

# for training data, runs if called from terminal
# if __name__ == '__main__':
#   in_data = []
#   for line in sys.stdin:
#     #might need to make subarray?
#     in_data.append([line])
#   print(run_feature3(in_data))
