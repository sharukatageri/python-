
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
output:
Input
nums =
[1,1,2]
Output
[1,2]
Expected
[1,2]
