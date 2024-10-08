"""
Game Scoring
Imagine a game where the player can score 1, 2, or 3 points depending on the move they make. Write a function or
functions, that for a given final score computes every combination of points that a player could score to achieve the
specified score in the game.

Signature
int[][] gameScoring(int score)

Input
Integer score representing the desired score

Output
Array of sorted integer arrays demonstrating the combinations of points that can sum to the target score

Example 1:
Input:
score = 4
Output:
[ [ 1, 1, 1, 1 ], [ 1, 1, 2 ], [ 1, 2, 1 ], [ 1, 3 ], [ 2, 1, 1 ], [ 2, 2 ], [ 3, 1 ] ]

Example 2:
Input:
score = 5
Output:
[ [ 1, 1, 1, 1, 1 ], [1, 1, 1, 2 ], [ 1, 1, 2, 1 ], [ 1, 1, 3 ], [ 1, 2, 1, 1 ], [ 1, 2, 2 ], [ 1, 3, 1 ],
[ 2, 1, 1, 1 ], [ 2, 1, 2 ], [ 2, 2, 1 ], [ 2, 3 ], [ 3, 1, 1 ], [ 3, 2 ] ]
"""


def gameScoring(score):
    res = []

    def dfs(cur, total):
        if total == score:
            res.append(cur.copy())
        if total > score:
            return

        # Try adding 1
        cur.append(1)
        dfs(cur, total+1)
        cur.pop()

        # Try adding 2
        cur.append(2)
        dfs(cur, total+2)
        cur.pop()

        # Try adding 3
        cur.append(3)
        dfs(cur, total+3)
        cur.pop()

    dfs([], 0)
    return res


if __name__ == "__main__":
    print(gameScoring(1))
    print(gameScoring(2))
    print(gameScoring(3))
    print(gameScoring(4))
    print(gameScoring(5))

