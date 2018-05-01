import os
import datetime
import csv
import psutil
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


class ProcessList:

    def get_file_name(self):
        return 'processList.csv'

    def write_process_list(self, current_psutil, current_time):
        if os.path.isfile(self.get_file_name()):
            os.chmod(self.get_file_name(), S_IWUSR | S_IREAD)

        with open(self.get_file_name(), 'ab') as process_list_file:
            writer = csv.writer(process_list_file, delimiter=',')
            for proc in current_psutil.process_iter():
                writer.writerow([current_time, proc.pid, proc.name()])

        os.chmod(self.get_file_name(), S_IREAD | S_IRGRP | S_IROTH)

    def get_sample_by_date(self, date):
        sample = []
        with open(self.get_file_name(), 'rb') as f:
            mycsv = csv.reader(f)
            mycsv = list(mycsv)
            for row in mycsv:
                if row[0] == date:
                    sample.append(row[1])
        return sample
