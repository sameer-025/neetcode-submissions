class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        b = {}

        for i in nums:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1

        max_element = max(b, key=b.get)

        return max_element