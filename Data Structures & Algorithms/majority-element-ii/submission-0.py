class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count:
            if count[num] > n / 3:
                result.append(num)

        return result