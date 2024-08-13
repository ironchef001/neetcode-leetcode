class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

# visit to track course that all prereq have been solved
# cycle is to introduced to detect the cycle
#   dfs
#       if already in cycle, return False
#       then temporarily add it to cycle
#       walk over each prereq, 
#           if all pass, remove from cycle
#           if one prereq fails, 
#               it will never be removed from cycle
#               nex time, dfs will fail immediately