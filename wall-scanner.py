from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt
import matplotlib.pyplot as plt


def print_target(t):
    pos = '(%6.4f, %6.4f, %6.4f) cm' % (t.xPosCm, t.yPosCm, t.zPosCm)
    print('%s, strength = %f' % (pos, t.amplitude))

    if hasattr(t, 'angleDeg'):
        # how to get this?
        print('  width = %6.4f cm, type=%s, angle=%f deg' % (t.widthCm, t.type, t.angleDeg))


profiles = {
    'sensor': wlbt.PROF_SENSOR,
    'imaging': wlbt.PROF_SHORT_RANGE_IMAGING,
}

profile = 'imaging'


def main():
    wlbt.Init()  # load the WalabotSDK to the Python wrapper
    wlbt.SetSettingsFolder()  # set the path to the essetial database files
    wlbt.ConnectAny()  # establishes communication with the Walabot

    wlbt.SetProfile(profiles[profile])  # set scan profile out of the possibilities
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)  # specify filter to use

    # TODO: calibrate

    wlbt.Start()  # starts Walabot in preparation for scanning

    plt.ion()
    handles = []
    for n in range(5):
        h = plt.plot([], [], label='target %d' % n)
        handles.append(h[0])

    while True:
        wlbt.Trigger()  # initiates a scan and records signals
        if profile == 'sensor':
            targets = wlbt.GetSensorTargets()  # provides a list of identified targets
        elif profile == 'imaging':
            targets = wlbt.GetImagingTargets()  # only one target
        # raw_image = wlbt.GetRawImageSlice()[0] # is there anything else in this iterable?
        # dim = wlbt.getRawImageSliceDimensions()

        # update terminal
        system('cls' if platform == 'win32' else 'clear')  # clear the terminal
        for t in targets:
            print_target(t)

        # update plots
        for n, t in enumerate(targets):
            handles[n].set_xdata(t.xPosCm)
            handles[n].set_ydata(t.yPosCm)
            handles[n].set_marker('o')
            handles[n].set_color('k')
            handles[n].set_markersize(t.amplitude)

        plt.xlim(-150, 150)
        plt.ylim(-150, 150)
        plt.draw()
        plt.pause(0.01)

    wlbt.Stop()  # stops Walabot when finished scanning
    wlbt.Disconnect()  # stops communication with Walabot


main()
