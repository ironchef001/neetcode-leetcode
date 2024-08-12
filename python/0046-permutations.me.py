class Solution:
    def recursive_neetcode_github(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

    def recursive_neetcode_youtube(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):  # may insert to tail: +1
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res

    def non_recursive(self, nums: List[int]) -> List[List[int]]: 
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        
        return perms


    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = self.recursive_neetcode_github(nums)
        # res = self.recursive_neetcode_youtube(nums)
        res = self.non_recursive(nums)

        return res