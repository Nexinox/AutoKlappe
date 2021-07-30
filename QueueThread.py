from threading import Thread
import queue as Queue


class QueueThread(Thread):

    queue: Queue.Queue = None

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        pass

    def writeToQueue(self, data):
        self.queue.put(data)

    def readFromQueue(self):
        return self.queue.get()
