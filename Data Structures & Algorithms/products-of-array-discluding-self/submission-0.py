class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        product = 1
        zeros = nums.count(0)

        if zeros > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                product = product*num
            else:
                continue

        for i in range(len(nums)):
            if zeros == 1:
                op.append(product if nums[i] == 0 else 0)
            else:
                op.append(int(product/nums[i]))

        return op