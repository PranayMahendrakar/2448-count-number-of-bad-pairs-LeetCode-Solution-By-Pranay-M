class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        
        # Count pairs where nums[i] - i == nums[j] - j (good pairs)
        count = defaultdict(int)
        good_pairs = 0
        
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += count[diff]
            count[diff] += 1
        
        return total_pairs - good_pairs