import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


def write_process_log(current_pids, prev_pids, current_time):
    new_processes = []
    killed_processes = []
    for pid in prev_pids:
        if pid not in current_pids:
            killed_processes.append(pid)
    for pid in current_pids:
        if pid not in prev_pids:
            new_processes.append(pid)
    prev_pids = current_pids
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
    return prev_pids
