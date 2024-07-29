# An example of a thread-safe queue
#
# Other Considerations
# Blocking Operations:
# If you need blocking behavior (where dequeue waits until an item is available), you can use threading.Condition instead of a simple lock.
#
# Timeouts:
# You can add timeout mechanisms to dequeue and enqueue methods to handle cases where the operation should not block indefinitely.
#
# Performance:
# For high-performance applications, consider using more advanced synchronization mechanisms or concurrent data structures provided by libraries such as concurrent.futures.


import threading
import time
from collections import deque


class ThreadSafeQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, item):
        with self.lock:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    def dequeue(self):
        with self.lock:
            if len(self.queue) == 0:
                return None
            item = self.queue.popleft()
            print(f"Dequeued: {item}")
            return item

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0

    def size(self):
        with self.lock:
            return len(self.queue)


# Example usage
if __name__ == '__main__':
    queue = ThreadSafeQueue()


    def producer(q):
        for i in range(5):
            q.enqueue(i)
            time.sleep(0.1)


    def consumer(q):
        while True:
            item = q.dequeue()
            if item is None:
                break
            time.sleep(0.15)


    producer_thread = threading.Thread(target=producer, args=(queue,))
    consumer_thread = threading.Thread(target=consumer, args=(queue,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
