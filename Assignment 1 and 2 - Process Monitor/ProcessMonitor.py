import time
import thread
import psutil
import ProcessList
import StatusLog
import FilesHandler


class ProcessMonitor:
    """
    This class contain the main functional of the process monitor.
    """
    __delay = 0
    __plist = None
    __plog = None
    __prev_pids = []

    def __init__(self, delay):
        self.__delay = delay
        self.__plist = ProcessList.ProcessList()
        self.__plog = StatusLog.StatusLog()

    def start_monitor(self):
        observer = FilesHandler.Observer()
        observer.schedule(FilesHandler.MyHandler(), '.')
        observer.start()
        while 1:
            current_time = time.ctime()
            current_psutil = psutil
            self.__plist.write_process_list(current_psutil, current_time)
            self.__plog.write_status_log(current_psutil, current_time)
            time.sleep(self.__delay)


delay = input('Enter a time in seconds to sleep after samling: ')
pm = ProcessMonitor(delay)
thread.start_new_thread(pm.start_monitor())
thread.join()
