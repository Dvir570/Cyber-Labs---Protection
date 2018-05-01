import time
import contextlib
import watchdog.observers

PAUSED = False


class PausingObserver(watchdog.observers.Observer):
    def dispatch_events(self, *args, **kwargs):
        if not getattr(self, '_is_paused', False):
            super(PausingObserver, self).dispatch_events(*args, **kwargs)

    def pause(self):
        global PAUSED
        PAUSED = True

    def resume(self):
        time.sleep(self.timeout)  # allow interim events to be queued
        self.event_queue.queue.clear()
        global PAUSED
        PAUSED = False

    @contextlib.contextmanager
    def ignore_events(self):
        self.pause()
        yield
        self.resume()
