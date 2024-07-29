import random

"""
Example for a single draw:
print(draw_weighted_probability(split_weights(some_dict, precision=0.001)))

For multiple draws from a single probability distribution:
num_draws = 1000000
representation = split_weights(some_dict)
while x < num_draws:
    print(draw_weighted_probability(representation)
"""


def split_weights(weights: list, precision: float = 0.00001):
    """
    Split and sort a list of tuples of weights and their values.  A custom precision value can be provided to limit floating
    point precision errors.  A second probability value will only be added to a split if there is enough room leftover
    after adding the first probability value and only if the second probability value is greater than the precision.
    (1 / number of discrete probabilities) - first probability value >= precision.  The default value for precision
    is 0.00001.  Run-time complexity O(n log n); Memory Complexity n

    :param weights: A list of tuples of weights to values of a normal probability distribution (i.e. the sum of the probabilities is 1
    [(0.2, 'orange'), (0.8, 'purple')] )
    :param precision: A guard value for floating point precision errors.
    :return: A list providing constant time cost for 'draw' actions on the provided probability distribution.
    """

    to_return = []
    num_weights = len(weights)

    weights.sort(key=lambda a: a[0])  # O(n log n)
    for i in range(num_weights):
        smallest_probability, smallest_value = weights.pop(0)  # pop first item O(log n)
        remainder = (1 / num_weights) - smallest_probability
        if remainder > precision:
            largest_probability, largest_value = weights.pop(-1)  # pop last item O(log n)
            largest_probability -= remainder
            if largest_probability >= precision:  # remaining probability is still significant enough; add it back in
                weights.append((largest_probability, largest_value))
                weights.sort(key=lambda a: a[0])  # resort the list O(n log n)
            to_return.append((smallest_probability, smallest_value, largest_value))
        else:
            to_return.append((smallest_probability, smallest_value, None))
    return to_return


def draw_weighted_probability(probability_split: list):
    """
    Draw a value from a list of weighted probabilities

    :param probability_split:  A probability distribution represented by a list of three-tuples containing a
    probability <1 and up to two values ie. [(0.8, 'purple', 'orange'), (0.2, 'orange', None)]
    :return: A value from the probability distribution represented by probability_split
    """
    num_values = len(probability_split)
    probability, value1, value2 = probability_split[random.randint(0, num_values - 1)]
    if random.random() / num_values <= probability:
        return value1
    else:
        return value2


if __name__ == "__main__":
    weights_dist = [(4.0 / 8.0, "common"), (2.0 / 8.0, "rare"), (1.5 / 8.0, "epic"), (0.49999 / 8.0, "legendary"), (0.00001/8.0, "mythical")]

    partition = split_weights(weights_dist)

    counts = {"common": 0, "rare": 0, "epic": 0, "legendary": 0, "mythical": 0}
    for x in range(1000000):
        counts[draw_weighted_probability(partition)] += 1

    print(counts)
