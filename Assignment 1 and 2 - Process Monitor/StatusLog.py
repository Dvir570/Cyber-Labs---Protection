import os
import datetime
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


class StatusLog:
    __last_modified = None
    __prev_pids = []

    def get_file_name(self):
        return 'Status_Log.txt'

    def write_status_log(self, current_psutil, current_time):
        new_processes = []
        killed_processes = []
        current_pids = current_psutil.pids()
        for pid in self.__prev_pids:
            if pid not in current_pids:
                killed_processes.append(pid)
        for pid in current_pids:
            if pid not in self.__prev_pids:
                new_processes.append(pid)
        self.__prev_pids = current_pids
        if os.path.isfile(self.get_file_name()):
            if self.__last_modified != os.stat(self.get_file_name()).st_mtime:
                print(self.get_file_name() + ' modified at ' + str(datetime.datetime.fromtimestamp(os.path.getmtime(self.get_file_name()))))
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
        self.__last_modified = os.stat(self.get_file_name()).st_mtime
