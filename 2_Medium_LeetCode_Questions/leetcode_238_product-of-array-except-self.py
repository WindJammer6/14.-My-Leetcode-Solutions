class Solution:
    def productExceptSelf(self, nums):
        # Save intermediate products from first index/prefix to end index - 1 
        prefix_products = [1]
        for num in nums[:len(nums)-1]:
            if len(prefix_products) != 0:
                # print(prefix_products)
                prefix_products.append(num * prefix_products[-1])
            else:
                prefix_products.append(num)

        # print(prefix_products)


        # Save intermediate products from last index/suffix to first index + 1
        suffix_products = [1]
        for num in reversed(nums[1:]):
            if len(suffix_products) != 0:
                # print(suffix_products)
                suffix_products.append(num * suffix_products[-1])
            else:
                suffix_products.append(num)

        # print(suffix_products)

        # Create the answer array
        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(suffix_products[-1])
            elif i == len(nums) - 1:
                answer.append(prefix_products[i])
            else:
                answer.append(suffix_products[len(nums)-i-1] * prefix_products[i])

        # print(answer)
        return answer
    

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))        # [24,12,8,6]
print(solution.productExceptSelf([-1,1,0,-3,3]))    # [0,0,9,0,0]