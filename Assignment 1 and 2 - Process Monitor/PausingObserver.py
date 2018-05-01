import time
import watchdog.observers

PAUSED = False


class PausingObserver(watchdog.observers.Observer):
    def pause(self):
        global PAUSED
        PAUSED = True

    def resume(self):
        time.sleep(self.timeout)  # allow interim events to be queued
        self.event_queue.queue.clear()
        global PAUSED
        PAUSED = False
