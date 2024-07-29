"""
Step-By-Step Directions From a Binary Tree Node to Another
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n.
You are also given an integer startValue representing the value of the start node s, and a different integer
destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such
path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific
direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.



Example 1:

        5
       /\
      1  2
     /   /\
    3   6  4

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:
    2
   /
  1

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue

"""
from typing import List


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = value

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


# Leet code solution class
class Solution:
    @staticmethod
    def clean_input(self, items: list):
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
    def list_to_bt(self, items: list):
        """
        Create Binary Tree from a list of values
        :param items: The list of values starting with the root value to create a tree from
        :return: A node to the root of the tree or None
        """
        n = len(items)
        if n == 0:
            return None

        def inner(index: int = 0):
            """
            Closure function used to build the tree recursively
            :param index: The current position in the list we're looking at.
            :return: A Node or None.
            """
            if n <= index:
                # We're looking out of bounds
                return None
            if items[index] is None:
                # No value for this node -> this child does not exist so skip it
                return None

            node = TreeNode(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()

    def find_start(self, root: TreeNode, start_value: int):
        left_result = None
        if not root:
            return None
        if root.val == start_value:
            return root
        if root.left is not None:
            left_result = self.find_start(root.left, start_value)
        if left_result:
            return left_result
        else:
            return self.find_start(root.right, start_value)

    # This little bastard isn't needed for the best version, but is its own question to solve.
    def find_lca(self, root: TreeNode, n1: int, n2: int):
        if root is None:
            return None

        if root.val == n1 or root.val == n2:
            return root

        left_lca = self.find_lca(root.left, n1, n2)
        right_lca = self.find_lca(root.right, n1, n2)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca is not None else right_lca

    def _find_path(self, node: TreeNode, target: int, path: List[str]) -> bool:
        if node is None:
            return False

        if node.val == target:
            return True

        # Try left subtree
        path.append("L")
        if self._find_path(node.left, target, path):
            return True
        path.pop()  # Remove last character

        # Try right subtree
        path.append("R")
        if self._find_path(node.right, target, path):
            return True
        path.pop()  # Remove last character

        return False

    # function name required by leetcode
    def getDirections(self, root, start_value, dest_value):
        tree_root = self.clean_input(self, root)
        tree_root = self.list_to_bt(self, tree_root)

        start_path = []
        dest_path = []

        self._find_path(tree_root, start_value, start_path)
        self._find_path(tree_root, dest_value, dest_path)

        directions = []
        common_path_length = 0

        # Find common path length
        while (common_path_length < len(start_path)
               and common_path_length < len(dest_path)
               and start_path[common_path_length] == dest_path[common_path_length]):
            common_path_length += 1

        directions.extend("U" * (len(start_path) - common_path_length))

        directions.extend(dest_path[common_path_length:])

        return "".join(directions)


if __name__ == "__main__":
    s = Solution()
    print(s.getDirections([5, 1, 2, 3, None, 6, 4], 3, 6))
    print(s.getDirections([2,1], 2, 1))
