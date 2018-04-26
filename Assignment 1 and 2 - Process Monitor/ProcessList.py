import os
import datetime
import csv
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


class ProcessList:
    __last_modified = None

    def get_file_name(self):
        return 'processList.csv'

    def write_process_list(self, current_psutil, current_time):
        if os.path.isfile(self.get_file_name()):
            if self.__last_modified != os.stat(self.get_file_name()).st_mtime:
                print(self.get_file_name() + ' modified at ' + str(datetime.datetime.fromtimestamp(os.path.getmtime(self.get_file_name()))))
            os.chmod(self.get_file_name(), S_IWUSR | S_IREAD)

        with open(self.get_file_name(), 'ab') as process_list_file:
            writer = csv.writer(process_list_file, delimiter=',')
            for proc in current_psutil.process_iter():
                writer.writerow([current_time, proc.pid, proc.name()])

        os.chmod(self.get_file_name(), S_IREAD | S_IRGRP | S_IROTH)
        self.__last_modified = os.stat(self.get_file_name()).st_mtime
