class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        # Pass 1: left products
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        # Pass 2: multiply by right products
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result