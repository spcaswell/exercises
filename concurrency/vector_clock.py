# An example of a vector clock data structure
# Vector clocks are used to track causality relationships in distributed systems, determining the partial ordering of events.
# They are implemented in distributed databases and version control systems to manage concurrent updates and conflict resolution.

from collections import defaultdict


class VectorClock:
    def __init__(self, node_id):
        self.node_id = node_id
        self.clock = defaultdict(int)

    def increment(self):
        self.clock[self.node_id] += 1

    def update(self, other_clock):
        for node, time in other_clock.items():
            self.clock[node] = max(self.clock[node], time)

    def get_time(self):
        return dict(self.clock)


# Example usage:
if __name__ == "__main__":
    # Create vector clocks for two nodes
    node1_clock = VectorClock("node1")
    node2_clock = VectorClock("node2")

    # Simulate events and updating clocks
    node1_clock.increment()
    node2_clock.increment()
    node2_clock.increment()

    # After communication or event synchronization, update clocks
    node1_clock.update(node2_clock.get_time())
    node2_clock.update(node1_clock.get_time())

    # Print the final vector clocks
    print(f"Node 1 clock: {node1_clock.get_time()}")
    print(f"Node 2 clock: {node2_clock.get_time()}")
