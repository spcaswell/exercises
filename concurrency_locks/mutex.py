# Example of a Mutex Lock
# Python's threading module provides a Lock class which is a mutex.
import threading

mutex = threading.Lock()


def critical_section():
    with mutex:
        # Critical section code
        print("Mutex: Critical section")


thread1 = threading.Thread(target=critical_section)
thread2 = threading.Thread(target=critical_section)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
