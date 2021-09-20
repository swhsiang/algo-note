class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.h, self.w = len(heights), len(heights[0])
        p_arr = []
        a_arr = []
        for i in range(self.w):
            p_arr.append((0, i))
            a_arr.append((self.h - 1, i))

        for i in range(self.h):
            p_arr.append((i, 0))
            a_arr.append((i, self.w-1))

        p_reachable = set(p_arr)
        a_reachable = set(a_arr)

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while p_arr:
            x,y = p_arr.pop()
            # stack = [(x,y)]
            # while stack:
            for i, j in directions:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < self.h and 0 <= new_y < self.w and heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in p_reachable:
                    p_reachable.add((new_x, new_y))
                    p_arr.append((new_x, new_y))

        while a_arr:
            x,y = a_arr.pop()
            # stack = [(x,y)]
            # while a_arr:
            for i, j in directions:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < self.h and 0 <= new_y < self.w and heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in a_reachable:
                    a_reachable.add((new_x, new_y))
                    a_arr.append((new_x, new_y))

        return list(p_reachable.intersection(a_reachable))
