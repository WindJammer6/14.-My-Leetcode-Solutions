class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter_for_each_element = {}

        for i in nums:
            if i not in counter_for_each_element:
                counter_for_each_element.update({i : 1})
            else:
                counter_for_each_element[i] += 1

        rounded_up_number_of_half_of_elements_in_list = int(len(nums)/2) + (len(nums) % 2)

        for key, value in counter_for_each_element.items():
            if value > rounded_up_number_of_half_of_elements_in_list or value == rounded_up_number_of_half_of_elements_in_list:
                return key
        return "There is no majority element!"
        
number_list = [6,5,5]

solution = Solution()

print(solution.majorityElement(number_list))