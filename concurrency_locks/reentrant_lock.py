# Reentrant Lock (Recursive Lock)
# Python's threading module provides a RLock class which is a reentrant lock.

import threading

reentrant_lock = threading.RLock()


def recursive_function(depth):
    reentrant_lock.acquire()
    try:
        print(f"Reentrant Lock: Depth {depth}")
        if depth > 0:
            recursive_function(depth - 1)
    finally:
        reentrant_lock.release()


thread = threading.Thread(target=recursive_function, args=(3,))
thread.start()
thread.join()
