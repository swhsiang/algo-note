"""
Leetcode 510
"""

def getAns(inp: list):
    if len(inp) < 2:
        return inp[0]

    val = inp[0]
