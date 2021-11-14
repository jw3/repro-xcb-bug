import os
import threading
import time


class MyThread(threading.Thread):

    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.stop_now = False
        self.callback = callback

    def run(self):
        while not self.stop_now:
            time.sleep(1)
            self.callback(True)

    def stop(self):
        self.stop_now = True