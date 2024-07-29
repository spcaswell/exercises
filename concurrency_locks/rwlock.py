# Example of a Read-Write Lock
# Python does not have a built-in read-write lock, but you can implement one using a combination of threading.Lock and threading.Condition.
import threading


class ReadWriteLock:
    def __init__(self):
        self.lock = threading.Lock()
        self.read_ready = threading.Condition(self.lock)
        self.readers = 0

    def acquire_read(self):
        with self.lock:
            self.readers += 1

    def release_read(self):
        with self.lock:
            self.readers -= 1
            if self.readers == 0:
                self.read_ready.notify_all()

    def acquire_write(self):
        self.lock.acquire()
        while self.readers > 0:
            self.read_ready.wait()

    def release_write(self):
        self.lock.release()


if __name__ == '__main__':
    rwlock = ReadWriteLock()


    def read_section():
        rwlock.acquire_read()
        try:
            # Read-only critical section
            print("Read-Write Lock: Read section")
        finally:
            rwlock.release_read()


    def write_section():
        rwlock.acquire_write()
        try:
            # Write critical section
            print("Read-Write Lock: Write section")
        finally:
            rwlock.release_write()


    reader1 = threading.Thread(target=read_section)
    reader2 = threading.Thread(target=read_section)
    writer = threading.Thread(target=write_section)

    reader1.start()
    reader2.start()
    writer.start()

    reader1.join()
    reader2.join()
    writer.join()
