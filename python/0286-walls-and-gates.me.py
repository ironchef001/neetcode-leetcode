class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        q = []
        visited = set()

        def visit_room(r, c, dist):
            if (
                not r in range(ROWS) or
                not c in range(COLS) or 
                (r, c) in visited or
                rooms[r][c] == -1
            ):
                return
            
            visited.add((r,c))
            q.append((r, c))
            rooms[r][c] = dist
 
        # get all gates
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            qlength = len(q)
            dist += 1
            for _ in range(qlength):
                r, c = q.pop(0)
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    # visit each adjacent
                    visit_room(r+dr, c+dc, dist)