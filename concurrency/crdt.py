# Example implementations of Conflict-Free Replicated Data Types (CRDTs)
# You will need to extend these implementations to handle more complex scenarios, such as handling concurrent updates or adding additional operations.

import time


class CounterCRDT:
    def __init__(self):
        self.counter = 0

    def increment(self, delta=1):
        self.counter += delta

    def merge(self, other):
        self.counter = max(self.counter, other.counter)

    def value(self):
        return self.counter


class SetCRDT:
    def __init__(self):
        self.added_elements = set()
        self.removed_elements = set()

    def add(self, element):
        self.added_elements.add(element)

    def remove(self, element):
        if element in self.added_elements:
            self.added_elements.remove(element)
            self.removed_elements.add(element)

    def merge(self, other):
        self.added_elements.update(other.added_elements)
        self.removed_elements.update(other.removed_elements)

    def elements(self):
        return self.added_elements - self.removed_elements


class LWWRegisterCRDT:
    def __init__(self):
        self.value = None
        self.timestamp = 0

    def write(self, value):
        current_time = time.time()
        if current_time > self.timestamp:
            self.value = value
            self.timestamp = current_time

    def merge(self, other):
        if other.timestamp > self.timestamp:
            self.value = other.val
            self.timestamp = other.timestamp

    def read(self):
        return self.value

if __name__ == '__main__':
    # Example usage of Counter CRDT
    counter1 = CounterCRDT()
    counter2 = CounterCRDT()

    counter1.increment(3)
    counter2.increment(5)

    counter1.merge(counter2)
    print("Merged counter value:", counter1.value())  # Output: Merged counter value: 5

    # Example usage of Set CRDT
    set1 = SetCRDT()
    set2 = SetCRDT()

    set1.add("apple")
    set2.add("banana")
    set1.remove("apple")

    set1.merge(set2)
    print("Merged set elements:", set1.elements())  # Output: Merged set elements: {'banana'}

    # Example usage of LWW-Register CRDT
    register1 = LWWRegisterCRDT()
    register2 = LWWRegisterCRDT()

    register1.write("value1")
    time.sleep(1)  # To simulate different timestamps
    register2.write("value2")

    register1.merge(register2)
    print("Merged register value:", register1.read())  # Output: Merged register value: value2

