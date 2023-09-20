# I have compiled solutions for all the 6 classic backtracking problems, you can practise them together for better understanding. Good luck with your preparation/interviews!
from typing import List
from collections import Counter

# 78. Subsets
# -----------
# take, leave
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        def solve(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return 
            # take nums[i]   
            subset.append(nums[i])
            solve(i+1)
            # leave nums[i]
            subset.pop()
            solve(i+1)
            
        solve(0)
        return ans

# 39. Combination Sum
# -------------------
# same as above, but with target
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, curr = [], []
        def solve(i, s):
            if s == target:
                ans.append(curr.copy())
                return
            if i >= len(candidates) or s > target:
                return
            
            curr.append(candidates[i])
            solve(i, s+candidates[i])

            curr.pop()
            solve(i+1, s)
        solve(0, 0)
        return ans
    
# 46. Permutations
# ------------------
# for each list excluding current number, we just add the currnt number to all its possible perms
# as example [1, 2, 3] and we are currently at 2, then we can add 2 to all the perms of [1, 3] which is [1, 3] and [3, 1] 
# so we get [1, 3, 2] and [3, 1, 2] 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        perms = []
        for i in range(len(nums)):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                perms.append(perm + [nums[i]])
        return perms
    
# 90. Subsets II
# ---------------
# same as version 1, but added sorting and duplicate check 
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to avoid duplicates
        ans, subset = [], []
        def solve(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return 
            # take nums[i]   
            subset.append(nums[i])
            solve(i+1)
            # leave nums[i]
            subset.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]: # to avoid duplicates ===> if currently we took [1, 2] and the next number is also 2, then we can just skip it
                i+=1
            solve(i+1)
            
        solve(0)
        return ans
    
# 40. Combination Sum II
# ----------------------
# same as version 1, but added sorting and duplicate check
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # to avoid duplicates
        ans, curr = [], []
        def solve(i, s):
            if s == target:
                ans.append(curr.copy())
                return
            if i >= len(candidates) or s > target:
                return
            
            curr.append(candidates[i])
            solve(i+1, s+candidates[i])

            curr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]: # to avoid duplicates
                i+=1
            solve(i+1, s)
        solve(0, 0)
        return ans

# 47. Permutations II
# -------------------
# same as version 1, but perms are stored in a set to avoid duplicates
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(nums):
            if len(nums) == 1:
                return [nums]
            perms = set()
            for i in range(len(nums)):
                for perm in permute(nums[:i] + nums[i+1:]):
                    perms.add(tuple(perm + [nums[i]])) # because we are using set, we need to convert list to tuple to make it hashable
            return [list(perm_tuple) for perm_tuple in perms] # convert back to list

        return permute(nums)

# ----------------------------------------------
# More good backtracking problems for practice #
# ----------------------------------------------
# 79. Word Search
# ---------------
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def can(i, j):
            return 0<=i<n and 0<=j<m
        
        def solve(i, j, wrd):
            if len(wrd) == 0:
                return True
            if not can(i, j):
                return False
            
            if board[i][j] == wrd[0]:
                board[i][j] = "5"
                if solve(i+1, j, wrd[1:]) or solve(i-1, j, wrd[1:]) or solve(i, j+1, wrd[1:]) or solve(i, j-1, wrd[1:]):
                    return True
                board[i][j] = wrd[0]
            return False

        for i in range(n):
            for j in range(m):
                if solve(i, j, word):
                    return True
        return False 
    
          
# 131. Palindrome Partitioning
# 784. Lettercase Permutation
# 1087. Brace Expansion
# 93. Restore IP addresses
# 17. Letter Combinations of a Phone Number
# 51. N-Queens
