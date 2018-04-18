import psutil
import time
import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


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
            if os.path.isfile('processList.txt'):
                os.chmod('processList.txt', S_IWUSR | S_IREAD)
            process_list_file = open('processList.txt', 'a')
            current_psutil = psutil
            current_pids = current_psutil.pids()
            process_list_file.write('-'*100 + '\n')
            process_list_file.write(current_time + '\n\n')
            for proc in current_psutil.process_iter():
                process_list_file.write(str(proc.name) + '\n')
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
            os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)
            self.__prevPids = current_pids
            if os.path.isfile('Status_Log.txt'):
                os.chmod('Status_Log.txt', S_IWUSR | S_IREAD)
            status_log_file = open('Status_Log.txt', 'a')
            status_log_file.write('-' * 100 + '\n')
            status_log_file.write(current_time + '\n\n')
            print('New running processes:' + '\n')
            status_log_file.write('New running processes:' + '\n')
            for pid in new_processes:
                print(str(pid))
                status_log_file.write(str(pid) + '\n')
            print('\n' + 'Killed processes:' + '\n')
            status_log_file.write('\n' + 'Killed processes:' + '\n')
            for pid in killed_processes:
                print(str(pid))
                status_log_file.write(str(pid) + '\n')
            print('\n\n')
            status_log_file.write('\n\n')
            status_log_file.close()
            os.chmod('Status_Log.txt', S_IREAD | S_IRGRP | S_IROTH)
            time.sleep(self.__delay)


pm = ProcessMonitor(10)
pm.start_monitor()
