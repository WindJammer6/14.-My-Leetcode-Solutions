// Approach 1 (Dosent work, exceeds memory limit, but does bottom-up dynamic programming more closely)

// The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
// lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
// and base cases for this question and modified the top-down dynamic programming (with tabulation)
// code to this context to answer this question

// Using an example:
// prices = [7,1,5,3,6,4]

// Let:
// - i be the day to buy the goods
// - j be the day to sell the goods
// - Each cell contains the profit of the buy and sell

//             j →      0     1     2     3     4     5     6
//                           [7]   [1]   [5]   [3]   [6]   [4]
//             i ↓      0     0     0     0     0     0     0
//        1 (xi=7)      0     0     6     2     4     1     3
//        2 (xi=1)      0     0     0    -4    -2    -5    -3
//        3 (xi=5)      0     0     0     0     2    -1     1
//        4 (xi=3)      0     0     0     0     0    -3    -1
//        5 (xi=6)      0     0     0     0     0     0     2
//        6 (xi=4)      0     0     0     0     0     0     0


// Recurrence:
// DP[i][j] = xi - yj   if i > j

// Subproblems:
// for n in i from 0 to length of array,
//      for k in j from i to length of array
//          if DP[n, k]  >  max_profit
//              max_profit = DP[n,k]

// Base cases:
// - if i > j, DP[i, j] = 0
// - Else, DP[i, j] = xi - yj

// Using bottom-up approach:
// Pseudocode:
// Initialize 2-dim array 𝐷𝑃 (with entries 𝐷𝑃[𝑖,𝑗] for 0 ≤ 𝑖 ≤ 𝑚, 0 ≤ 𝑗 ≤ 𝑛)
// Initialize max_profit ← 0
// for 𝑖 from 0 to 𝑚:
//    𝐷𝑃[𝑖,0] ← 0
// for 𝑗 from 0 to 𝑛:
//    𝐷𝑃[0,𝑗] ← 0

// // Create the DP 2-dim array
// for 𝑖 from 1 to 𝑚:
//    for 𝑗 from 1 to 𝑛:
//        if j > i:
//              𝐷𝑃[𝑖,𝑗] ← 𝑥𝑖 -yj
//        else:
//              𝐷𝑃[𝑖,𝑗] ← 0

//  Then once the 2-dim array DP is created, scan the full 2-dim array DP to
//  find the highest max profit cell
//  ...
//  return 𝐷𝑃[𝑚, 𝑛]

// About creating the 2-dim array DP:
// Always start by initializing a table of suitable size. Start by storing
// the base values in the table. Tabulate all values that are computed. Don’t
// forget to actually solve the problem!


// import java.util.Arrays;

//class Solution {
//    public int maxProfit(int[] prices) {
//        int[][] DP = new int[prices.length][prices.length];
//
//        // Start by storing the base values in
//        // the table
//        for (int i = 0; i < prices.length; i++){
//            DP[i][0] = 0;
//        }
//        for (int j = 0; j < prices.length; j++){
//            DP[0][j] = 0;
//        }
//
//        // Create the DP 2-dim array
//        for (int k = 0; k < prices.length; k++){
//            for (int l = 0; l < prices.length; l++) {
//                if (l > k) {
//                    DP[l][k] = prices[l] - prices[k];
//                } else {
//                    DP[l][k] = 0;
//                }
//            }
//        }
//
//        //  Then once the 2-dim array DP is created, scan the full 2-dim array DP to
//        //  find the highest max profit cell
//        int maxProfit = 0;
//        for (int i = 0; i < prices.length; i++) {
//            for (int j = 0; j < prices.length; j++) {
//                if (DP[i][j] > maxProfit) {
//                    maxProfit = DP[i][j];
//                }
//            }
//        }
//
//        // Print the 2-dim array DP
//        // Loop through all rows
//        for (int[] row : DP)
//
//            // converting each row as string
//            // and then printing in a separate line
//            System.out.println(Arrays.toString(row));
//
//        return maxProfit;
//    }
//}


// Approach 2 (Dosent work, exceeds time limit, uses a more intuitive method by iterating through each item
// in the list and finding the max element from the remaining items in the list)
//class Solution {
//    public int maxProfit(int[] prices) {
//        int maxProfit = 0;
//
//        for (int i = 0; i < prices.length; i++) {
//
//            int maxOfSubArray = 0;
//            for (int j = i+1; j < prices.length; j++) {
//                if (prices[j] > maxOfSubArray) {
//                    maxOfSubArray = prices[j];
//                }
//            }
//
//            if (maxProfit < maxOfSubArray - prices[i]){
//                maxProfit = maxOfSubArray - prices[i];
//            }
//        }
//
//        return maxProfit;
//    }
//}



// Approach 3 (Works, uses a more intuitive method by iterating through the list and finding
// the largest element and smallest element from the list)
// Pseudocode:
// 1. Set min_price to a high value (or maximum integer value).
// 2. Initialize max_profit to 0.
// 3. Loop through each price in prices:
// 4. Update min_price if the current price is lower than min_price.
// 5. Calculate the profit as price - min_price.
// 6. Update max_profit if the calculated profit is greater than max_profit.
// 7. After the loop, max_profit contains the maximum possible profit. Return max_profit.
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = 1000000000;
        int maxProfit = 0;

        for (int price : prices){
            if (price < minPrice){
                minPrice = price;
            }

            if (maxProfit < price - minPrice){
                maxProfit = price - minPrice;
            }
        }

        return maxProfit;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        int [] prices1 = {7,1,5,3,6,4};
        System.out.println(solution.maxProfit(prices1));    // 5

        int [] prices2 = {7,6,4,3,1};
        System.out.println(solution.maxProfit(prices2));    // 0
    }
}