import matplotlib.figure as mfig

import PyQt4.QtGui as gui, PyQt4.QtCore as core

import collections

import time

import random

import serial

ser = serial.Serial('/dev/tty.usbmodem1411', 57600)

start_byte = 'S'

end_byte = 'F'

refreshMillis = 50

N = 200

xs = collections.deque(maxlen=N)

ys = collections.deque(maxlen=N)

app = gui.QApplication([])

fig = mfig.Figure()

canvas = FigureCanvasQTAgg(fig)

ax = fig.add_subplot(111)

ax.set_ylim([0,5])

line2D, = ax.plot(xs,ys)

canvas.show()

def process_line():

line = ser.readline()

data = map(float,line.split(" "))

xs.append(data[0])

ys.append(data[1])

line2D.set_data(xs,ys)

print data

xmin, xmax = min(xs),max(xs)

if xmin == xmax:

ax.set_xlim([xmin,xmin+1])

else:

ax.set_xlim([xmin,xmax])

canvas.draw()

timer = core.QTimer()

timer.timeout.connect(process_line)

timer.start(refreshMillis)

app.exec_()

ser.flush()

ser.close()