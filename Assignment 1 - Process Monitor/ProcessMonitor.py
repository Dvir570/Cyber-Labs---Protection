import os
import psutil
import time
import sys

class ProcessMonitor:
    """
    This class contain the main functional of the process monitor.
    """
    __delay = 0
    __processListFile = None
    __statusLogFile = None

    def __init__(self, delay):
        self.__delay = delay

    def start_monitor(self):
        while 1:
            self.__processListFile = open('processList.txt', 'a')
            processes = psutil.process_iter()
            self.__processListFile.write('-'*100 + '\n')
            self.__processListFile.write(time.ctime() + '\n\n')
            for proc in processes:
                name = str(proc.name)
                self.__processListFile.write(name + '\n')
            self.__processListFile.write('\n\n')
            self.__processListFile.close()
            time.sleep(self.__delay)

pm = ProcessMonitor(10)
pm.start_monitor()
