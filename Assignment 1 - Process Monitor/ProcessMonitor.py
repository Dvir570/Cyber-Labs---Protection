import psutil
import time
import zipfile
import WriteProcessListFile as plist
import WriteProcessLogFile as plog

class ProcessMonitor:
    """
    This class contain the main functional of the process monitor.
    """
    __delay = 0
    __prev_pids = []

    def __init__(self, delay):
        self.__delay = delay

    def start_monitor(self):
        zipf = zipfile.ZipFile('zipfile', 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))
        zipf.close()
        while 1:
            current_time = time.ctime()
            current_psutil = psutil
            current_pids = current_psutil.pids()
            plist.write_process_list(current_psutil, current_time)
            self.__prev_pids = plog.write_process_log(current_pids, self.__prev_pids, current_time)
            #pyminizip.compress_multiple(['processList.txt', 'Status_Log.txt'], "file.zip", "1233", 4)
            time.sleep(self.__delay)

pm = ProcessMonitor(10)
pm.start_monitor()
