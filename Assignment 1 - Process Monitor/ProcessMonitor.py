import os
import psutil
import time
import sys

class ProcessMonitor:
    """
    This class contain the main functional for the process monitor.
    """
    __delay = 0
    __processListFile = None
    __statusLogFile = None

    def __init__(self, delay):
        self.__delay = delay

    def start_monitor(self):
        self.__processListFile = open('processList.txt', 'w')
        self.__statusLogFile = open('Status_Log.txt', 'w')
        prods = psutil.process_iter()
        for prodc in prods:
            print(prodc.name)

    def close(self):
        if not self.__processListFile:
            self.__processListFile.close()
        if not self.__statusLogFile:
            self.__statusLogFile.close()


pm = ProcessMonitor(1)
pm.start_monitor()
pm.close()
