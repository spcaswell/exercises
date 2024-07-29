"""
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.



Example 1:
    1
   /\
  2  3
   \
    4

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:
       1
       /\
      2   3
     / \  / \
    4  5  6 7

Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].


Constraints:

The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10
"""

from leet_code_utils import LeetCodeUtils, TreeNode
from typing import List


class Solution:

    @staticmethod
    def remove_list_duplicates(items: List):
        return list(set(items))

    # Fails on non-unique node values
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf_node_values = []
        good_leaf_pairs = 0
        self._find_leaf_nodes(root, leaf_node_values)
        for i in range(len(leaf_node_values)):
            j = i + 1
            while j < len(leaf_node_values):
                dist = len(self._get_directions(root, leaf_node_values[i], leaf_node_values[j]))
                # print(f"{leaf_node_values[i]},{leaf_node_values[j]} distance is {dist}")
                if dist <= distance:
                    # print(f"{leaf_node_values[i]},{leaf_node_values[j]} distance is {dist}")
                    good_leaf_pairs += 1
                j += 1
            i += 1
        return good_leaf_pairs

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

    def _get_directions(self, root, start_value, dest_value):

        start_path = []
        dest_path = []

        self._find_path(root, start_value, start_path)
        self._find_path(root, dest_value, dest_path)

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

    def _find_leaf_nodes(self, root: TreeNode, leaf_nodes: List = None, visited_nodes: List = None) -> List:
        if leaf_nodes is None:
            leaf_nodes = []
        if visited_nodes is None:
            visited_nodes = []
        if root.val not in visited_nodes and root.left is None and root.right is None:
            leaf_nodes.append(root.val)
            visited_nodes.append(root.val)
        if root.left:
            self._find_leaf_nodes(root.left, leaf_nodes, visited_nodes)
        if root.right:
            self._find_leaf_nodes(root.right, leaf_nodes, visited_nodes)
        return leaf_nodes


class Solution2:
    def _post_order(self, current_node, distance):
        if current_node is None:
            return [0] * 12
        elif current_node.left is None and current_node.right is None:
            current = [0] * 12
            # Leaf node's distance from itself is 0
            current[0] = 1
            return current

        # Leaf node count for a given distance i
        left = self._post_order(current_node.left, distance)
        right = self._post_order(current_node.right, distance)

        current = [0] * 12

        # Combine the counts from the left and right subtree and shift by
        # +1 distance
        for i in range(10):
            current[i + 1] += left[i] + right[i]

        # Initialize to total number of good leaf nodes pairs from left and right subtrees.
        current[11] = left[11] + right[11]

        # Count all good leaf node distance pairs
        prefix_sum = 0
        i = 0
        for d2 in range(distance - 2, -1, -1):
            prefix_sum += left[i]
            current[11] += prefix_sum * right[d2]
            i += 1

        return current

    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self._post_order(root, distance)[11]


if __name__ == "__main__":
    case1 = ([1,2,3,'null',4], 3)
    case2 = ([1,2,3,4,5,6,7], 3)
    case3 = ([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], 3)
    case4 = ([50,25,75,13,37,63,87,7,19,31,43,57,69,81,93,3,10,16,22,28,34,40,46,53,60,66,73,79,85,91,97,2,5,8,11,15,18,21,24,27,30,33,36,39,42,45,48,52,55,59,62,65,68,71,74,78,80,83,86,89,92,95,98,1,4,6,9,12,14,17,20,23,26,29,32,35,38,41,44,47,49,51,54,56,58,61,64,67,70,72,76,77,82,84,88,90,94,96,99,100,2,5,8,11,15,18,21,24,27,30,33,36,39,42,45,48,52,55,59,62,65,68,71,74,78,80,83,86,89,92,95,98,1,4,6,9,12,14,17,20,23,26,29,32,35,38,41,44,47,49,51,54,56,58,61,64,67,70,72,76,77,82,84,88,90,94,96,99,100,3,7,10,13,16,19,22,25,28,31,34,37,40,43,46,50,53,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99,4,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59,62,65,68,71,74,77,80,83,86,89,92,95,98,5,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99,6,10,13,16,19,22,25,28,31,34,37,40,43,46,50,53,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99], 1)
    case5 = ([1,1,1], 2)

    tree1 = LeetCodeUtils.clean_input(case1[0])
    tree1 = LeetCodeUtils.list_to_bt(tree1)

    tree2 = LeetCodeUtils.clean_input(case2[0])
    tree2 = LeetCodeUtils.list_to_bt(tree2)

    tree3 = LeetCodeUtils.clean_input(case3[0])
    tree3 = LeetCodeUtils.list_to_bt(tree3)

    tree4 = LeetCodeUtils.clean_input(case4[0])
    # tree4 = LeetCodeUtils.remove_list_duplicates(tree4)
    tree4 = LeetCodeUtils.list_to_bt(tree4)

    tree5 = LeetCodeUtils.clean_input(case5[0])
    tree5 = LeetCodeUtils.list_to_bt(tree5)

    tree_nodes = []

    s = Solution()
    s2 = Solution2()
    # print(s._find_leaf_nodes(tree1, []))
    # print(s.countPairs(tree1, case1[1]))
    #
    # print(s._find_leaf_nodes(tree2, []))
    # print(s.countPairs(tree2, case2[1]))
    #
    # print(s._find_leaf_nodes(tree3, []))
    # print(s.countPairs(tree3, case3[1]))
    #
    # print(s._find_leaf_nodes(tree4, []))
    # print(s.countPairs(tree4, case4[1]))

    # print(s._find_leaf_nodes(tree5, []))
    print(s2.countPairs(tree5, case5[1]))
