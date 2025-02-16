class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_of_seen_values = {}
        for idx, value in enumerate(nums):
            required_number = target - value
            if required_number in dict_of_seen_values:
                return [idx, dict_of_seen_values[required_number]]
            else:
                dict_of_seen_values[value] = idx
