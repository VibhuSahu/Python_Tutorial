class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []

        for x in nums:
            for y in nums:
                if x != y :
                    if x + y == target:
                        a = nums.index(x)
                        b = nums.index(y)

                        output.append([a,b])

        return output[0]


nums = [3,2,4]
target = 6
print(Solution().twoSum(nums,target))