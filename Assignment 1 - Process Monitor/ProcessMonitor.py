import psutil
import time
from copy import deepcopy
import sys

class ProcessMonitor:
    """
    This class contain the main functional of the process monitor.
    """
    __delay = 0
    __prevSample = []
    __prevPids = []

    def __init__(self, delay):
        self.__delay = delay

    def start_monitor(self):
        while 1:
            current_time = time.ctime()
            process_list_file = open('processList.txt', 'a')
            current_psutil = psutil
            current_pids = current_psutil.pids()
            process_list_file.write('-'*100 + '\n')
            process_list_file.write(current_time + '\n\n')
            for proc in current_psutil.process_iter():
                process_list_file.write(str(proc.name) + '\n')
            #gone, alive = psutil.wait_procs(processes, timeout=10, callback=None)
            new_processes = []
            killed_processes = []
            for pid in self.__prevPids:
                if pid not in current_pids:
                    killed_processes.append(pid)
            for pid in current_pids:
                if pid not in self.__prevPids:
                    new_processes.append(pid)

            process_list_file.write('\n\n')
            process_list_file.close()
            self.__prevPids = current_pids
            status_log_file = open('Status_Log.txt', 'a')
            status_log_file.write('-' * 100 + '\n')
            status_log_file.write(current_time + '\n\n')
            print('New running processes:' + '\n')
            status_log_file.write('New running processes:' + '\n')
            for pid in new_processes:
                print(str(pid) + '\n')
                status_log_file.write(str(pid) + '\n')
            print('\n' + 'Killed processes:' + '\n')
            status_log_file.write('\n' + 'Killed processes:' + '\n')
            for pid in killed_processes:
                print(str(pid) + '\n')
                status_log_file.write(str(pid) + '\n')
            print('\n\n')
            status_log_file.write('\n\n')
            status_log_file.close()
            time.sleep(self.__delay)


pm = ProcessMonitor(10)
pm.start_monitor()
