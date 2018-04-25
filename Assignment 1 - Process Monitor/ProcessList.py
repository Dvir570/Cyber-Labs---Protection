import os
import datetime
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


class ProcessList:
    __last_modified = None

    def get_file_name(self):
        return 'processList.txt'

    def write_process_list(self, current_psutil, current_time):
        if os.path.isfile(self.get_file_name()):
            if self.__last_modified != os.stat(self.get_file_name()).st_mtime:
                print(self.get_file_name() + ' modified at ' + str(datetime.datetime.fromtimestamp(os.path.getmtime(self.get_file_name()))))
            os.chmod(self.get_file_name(), S_IWUSR | S_IREAD)
        process_list_file = open(self.get_file_name(), 'a')

        process_list_file.write('-' * 100 + '\n')
        process_list_file.write(current_time + '\n\n')
        for proc in current_psutil.process_iter():
            process_list_file.write('pid: ' + str(proc.pid) + '\tname: ' + proc.name() + '\n')
        process_list_file.write('\n\n')
        process_list_file.close()
        os.chmod(self.get_file_name(), S_IREAD | S_IRGRP | S_IROTH)
        self.__last_modified = os.stat(self.get_file_name()).st_mtime
