# Semaphore
# Python's threading module provides a Semaphore class.

import threading

semaphore = threading.Semaphore(2)


def limited_resource():
    with semaphore:
        # Critical section code
        print("Semaphore: Critical section")


threads = [threading.Thread(target=limited_resource) for _ in range(4)]

for t in threads:
    t.start()

for t in threads:
    t.join()
