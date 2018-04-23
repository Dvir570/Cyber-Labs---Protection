import psutil
import time
import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


def write_process_list(current_psutil, current_time):
    if os.path.isfile('processList.txt'):
        os.chmod('processList.txt', S_IWUSR | S_IREAD)
    process_list_file = open('processList.txt', 'a')

    process_list_file.write('-' * 100 + '\n')
    process_list_file.write(current_time + '\n\n')
    for proc in current_psutil.process_iter():
        process_list_file.write('pid: ' + str(proc.pid) + '\tname: ' + proc.name() + '\n')
    process_list_file.write('\n\n')
    process_list_file.close()
    os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)
