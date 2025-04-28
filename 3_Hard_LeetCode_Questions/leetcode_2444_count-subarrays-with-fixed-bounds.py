# All approaches taken from this Leetcode solution:
# Source: 
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/6687441/sliding-window-monotonic-queue-with-images-example-walkthrough/?envType=daily-question&envId=2025-04-26 (Leetcode)

class Solution:

    # Approach 1: Brute force (dosent work, exceed time limit)
    def countSubarrays1(self, nums, minK: int, maxK: int) -> int:

        # Generate all possible subarrays
        all_subarrays = []
        all_subarrays_with_fixed_bounds = []

        for i in range(len(nums)+1):
            for j in range(i+1, len(nums)+1):
                all_subarrays.append(nums[i:j])

        # If a subarray meet all the conditions of a fixed-bound subarray, append it to the
        # 'all_subarrays_with_fixed_bounds' list
        for i in all_subarrays:
            if min(i) == minK and max(i) == maxK:
                all_subarrays_with_fixed_bounds.append(i)


        print(all_subarrays_with_fixed_bounds)
        print(all_subarrays)

        return len(all_subarrays_with_fixed_bounds)
    

    # //////////////////////////////////////////////////////////////////////////////    


    # Approach 2: Using Sliding Window, use the important formula of counting subarrays with specific 
    # bounds (works)
    # IMPORTANT FORMULA:
    #       valid = max(0, min(mini, maxi) - start)
    #                     AND
    #               count += valid


    # How this important formula works?
    # Definition of each variable:
    # Variable | Meaning
    #   start  | Index of last invalid element (where the window was broken)
    #   mini   | Latest index where minK value was found
    #   maxi   | Latest index where maxK value was found
    #   count  | How many valid subarrays we have found so far

    # 🛤️ Intuition:
    # For a subarray to be valid, it must include both:
    # - At least one minK (minimum value you care about)
    # - At least one maxK (maximum value you care about)
    # So we care about where is the earliest occurrence among mini and maxi.

    # ✅ The formula:
    #           min(mini, maxi)
    # gives the earliest between the latest minK and latest maxK.

    # ✅ Then subtracting start:
    #           min(mini,maxi)−start
    # tells you how many new valid subarrays you can form ending at current i.

    # ✅ Wrapping it with max(0, ...) ensures that if no valid subarray exists, valid will 
    # be 0 (we don't allow negative subarrays).

    # Then:
    #           count+=valid
    # means you add the number of valid subarrays ending at this position into your total count!

    # 🏗️ Step-by-Step Meaning:
    # 1. Find earliest of mini and maxi.
    # 2. Check how many elements are after start (but before/at mini or maxi).
    # 3. These elements can form valid subarrays ending here.
    # 4. Add them into the running total.
    
    # 🎯 Example: [5, 2, 7, 3, 8] with minK = 3, maxK = 7
    # i | nums[i] | start      | mini | maxi | valid            | count
    # 0 | 5       | -1         | -1   | -1   | 0                | 0
    # 1 | 2       | 1 (invalid)| -1   | -1   | 0                | 0
    # 2 | 7       | 1          | -1   | 2    | 0                | 0
    # 3 | 3       | 1          | 3    | 2    | 1 (min(2,3) - 1) | 1
    # 4 | 8       | 1          | 3    | 2    | 1 (min(2,3) - 1) | 2
    
    # ✅ Here:
    # - At i = 3, we found both minK=3 and maxK=7 inside [7, 3], and start=1, so valid = 1.
    # - Similarly at i = 4, no new minK or maxK, but previous mini/maxi still valid.

    # 🧠 Final 10-Second Summary:
    # Line                                    | Meaning
    # valid = max(0, min(mini, maxi) - start) | How many valid subarrays ending at current i.
    # count += valid                          | Add to total number of valid subarrays.
    def countSubarrays2(self, nums, minK: int, maxK: int) -> int:

        start = -1
        mini = -1
        maxi = -1

        count = 0

        for i in range(len(nums)):
            
            # The element is not in the range minK to maxK
            if nums[i] < minK or nums[i] > maxK:
                start = i

            # The element is equal to minK
            if nums[i] == minK:
                mini = i

            # The element is equal to maxK
            if nums[i] == maxK:
                maxi = i

            # The element is in the range minK to maxK, but is not equal to minK and maxK
            if nums[i] != minK and nums[i] != maxK:
                pass


            # Important formula of counting subarrays with specific bounds.
            #       valid = max(0, min(mini, maxi) - start)
            #                     AND
            #               count += valid
            print(f"Start {start}")
            print(f"mini {mini}")
            print(f"maxi {maxi}")
            valid = max(0, min(mini, maxi) - start)
            count += valid

        return count



solution = Solution()
print(solution.countSubarrays1([1,3,5,2,7,5], 1, 5))        # 2
print(solution.countSubarrays1([1,1,1,1], 1, 1))            # 10

print(solution.countSubarrays2([1,3,5,2,7,5], 1, 5))        # 2
print(solution.countSubarrays2([1,1,1,1], 1, 1))            # 10
