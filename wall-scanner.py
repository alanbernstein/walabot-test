from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt
import matplotlib.pyplot as plt
import numpy as np


def print_target_short(t):
    print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(
        t.xPosCm, t.yPosCm, t.zPosCm))


def print_target(t):
    pos = '(%6.4f, %6.4f, %6.4f) cm' % (t.xPosCm, t.yPosCm, t.zPosCm)
    print('%s, width = %6.4f cm, strength = %f' % (pos, t.widthCm, t.amplitude))
    print('  type=%s, angle=%f deg' % (t.type, t.angleDeg))


def main():
    wlbt.Init()  # load the WalabotSDK to the Python wrapper
    wlbt.SetSettingsFolder()  # set the path to the essetial database files
    wlbt.ConnectAny()  # establishes communication with the Walabot

    wlbt.SetProfile(wlbt.PROF_SENSOR)  # set scan profile out of the possibilities
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)  # specify filter to use

    wlbt.Start()  # starts Walabot in preparation for scanning

    plt.ion()
    handles = []
    for n in range(5):
        handles.append(plt.plot([], [], label='target %d' % n))

    while True:
        wlbt.Trigger()  # initiates a scan and records signals
        targets = wlbt.GetSensorTargets()  # provides a list of identified targets

        # update terminal
        system('cls' if platform == 'win32' else 'clear')  # clear the terminal
        for t in targets:
            print_target(t)

        # update plots
        for n, t in enumerate(targets):
            handles[n].set_xdata(t.xPosCm)
            handles[n].set_ydata(t.yPosCm)
            handles[n].set_linestyle('ko')
            handles[n].set_markersize(t.amplitude

        plt.draw()
        plt.pause(0.01)
        



    wlbt.Stop()  # stops Walabot when finished scanning
    wlbt.Disconnect()  # stops communication with Walabot


main()
