import os
import datetime
import psutil
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


class StatusLog:
    __prev_pids = []

    def get_file_name(self):
        return 'Status_Log.txt'

    def get_new_running_process(self, pids_before, pids_after):
        new_processes = []
        for pid in pids_after:
            if pid not in pids_before:
                new_processes.append(pid)
        return new_processes

    def get_killed_process(self, pids_before, pids_after):
        killed_processes = []
        for pid in pids_before:
            if pid not in pids_after:
                killed_processes.append(pid)
        return killed_processes

    def write_status_log(self, current_psutil, current_time):
        current_pids = current_psutil.pids()
        killed_processes = self.get_killed_process(self.__prev_pids, current_pids)
        new_processes = self.get_new_running_process(self.__prev_pids, current_pids)
        self.__prev_pids = current_pids
        if os.path.isfile(self.get_file_name()):
            os.chmod(self.get_file_name(), S_IWUSR | S_IREAD)
        status_log_file = open(self.get_file_name(), 'a')
        status_log_file.write('-' * 100 + '\n')
        status_log_file.write(current_time + '\n\n')
        status_log_file.write('New running processes:' + '\n')
        for pid in new_processes:
            status_log_file.write(str(pid) + '\n')
        status_log_file.write('\n' + 'Killed processes:' + '\n')
        for pid in killed_processes:
            status_log_file.write(str(pid) + '\n')
        status_log_file.write('\n\n')
        status_log_file.close()
        os.chmod(self.get_file_name(), S_IREAD | S_IRGRP | S_IROTH)
