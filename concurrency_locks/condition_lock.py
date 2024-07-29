# Condition Variable
# Python's threading module provides a Condition class.


import threading

condition = threading.Condition()
shared_data = []


def consumer():
    with condition:
        condition.wait()
        print(f"Condition Variable: Consumed {shared_data.pop(0)}")


def producer():
    with condition:
        shared_data.append("data")
        print("Condition Variable: Produced data")
        condition.notify()


consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()
