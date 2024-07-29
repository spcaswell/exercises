"""
common functions used to handle leet code input data
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LeetCodeUtils:
    @staticmethod
    def clean_input(items: list):
        """
        Makes 'null' strings in a list None, and turns numeric string into ints.
        :param items: The input to be cleaned
        :return:
        """
        cleaned = []
        for x in items:
            if isinstance(x, str):
                if x == 'null':
                    cleaned.append(None)
                else:
                    cleaned.append(int(x))
            else:
                cleaned.append(x)
        return cleaned

    @staticmethod
    def remove_list_duplicates(items: List):
        return list(set(items))

    @staticmethod
    def list_to_bt(items: List):
        """
        Create Binary Tree from a list of values
        :param items: The list of values starting with the root value to create a tree from
        :return: A node to the root of the tree or None
        """

        def inner(index: int = 0):
            """
            Closure function used to build the tree recursively
            :param index: The current position in the list we're looking at.
            :return: A Node or None.
            """
            if len(items) <= index:
                # We're looking out of bounds
                return None
            if items[index] is None:
                # No value for this node -> this child does not exist so skip it
                items.insert(2*index+1, None)
                items.insert(2*index+2, None)
                return None

            node = TreeNode(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()








