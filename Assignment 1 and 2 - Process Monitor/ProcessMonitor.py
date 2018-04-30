import datetime
import time
import thread
import psutil
import ProcessList
import StatusLog
import FilesHandler
import PausingObserver


class ProcessMonitor:
    """
    This class contain the main functional of the process monitor.
    """
    __plist = None
    __plog = None

    def __init__(self):
        self.__plist = ProcessList.ProcessList()
        self.__plog = StatusLog.StatusLog()

    def start_monitor(self, delay):
        observer = PausingObserver.PausingObserver()
        observer.schedule(FilesHandler.MyHandler(), './')
        observer.start()
        while 1:
            current_time = datetime.datetime.now().strftime("%y-%m-%d %H-%M")
            current_psutil = psutil
            observer.pause()
            self.__plist.write_process_list(current_psutil, current_time)
            self.__plog.write_status_log(current_psutil, current_time)
            observer.resume()
            time.sleep(delay)

    def samples_diff(self):
        isValid = False
        prior_date = None
        after_date = None
        while not isValid:
            prior_date = raw_input("Type Date of the prior sample (yy-mm-dd hh-mm): ")
            try:  # strptime throws an exception if the input doesn't match the pattern
                datetime.datetime.strptime(prior_date, "%y-%m-%d %H-%M")
                isValid = True
            except:
                print "Input doesn't match the pattern, try again!\n"
        isValid = False
        while not isValid:
            after_date = raw_input("Type Date of the after sample (yy-mm-dd hh-mm): ")
            try:  # strptime throws an exception if the input doesn't match the pattern
                datetime.datetime.strptime(after_date, "%y-%m-%d %H-%M")
                isValid = True
            except:
                print "Input doesn't match the pattern, try again!\n"
        prior_sample = self.__plist.get_sample_by_date(prior_date)
        after_sample = self.__plist.get_sample_by_date(after_date)
        print('New running process:')
        for pid in self.__plog.get_new_running_process(prior_sample, after_sample):
            print(str(pid))
        print('Killed process:')
        for pid in self.__plog.get_killed_process(prior_sample, after_sample):
            print(str(pid))
        print('\n')


again = True
while again:
    choose = input('press 1 to start monitor\npress 2 to see differences between two dates\n')
    if choose == 1:
        delay = input('Enter a time in seconds to sleep after samling: ')
        pm = ProcessMonitor()
        thread.start_new_thread(pm.start_monitor(delay))
        again = False
    elif choose == 2:
        pm = ProcessMonitor()
        pm.samples_diff()
