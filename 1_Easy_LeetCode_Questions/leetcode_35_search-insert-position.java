class Solution {
    public int searchInsert(int[] nums, int target) {
        int[] information = binarySearch(nums, 0, nums.length-1, target);

        // Target not found
        if (information[0] == 0){
            return information[2];
        }

        // Target found
        else{
            return information[1];
        }
        
    }

    // Java implementation of iterative Binary Search (copy-pasted from GeekforGeeks website: https://www.geeksforgeeks.org/binary-search-in-java/), with
    // some modifications for the Leetcode question
    public int[] binarySearch(int a[], int l, int r, int x)
    {
        int foundIndex = 0;
        int notFoundIndex = 0;
        int foundBoolean = 0;

        while (l <= r) {
            int m = (l + r) / 2;

            // Index of Element Returned
            if (a[m] == x) {
                foundIndex = m;
                foundBoolean = 1;
                break;

            // If element is smaller than mid, then
            // it can only be present in left subarray
            // so we decrease our r pointer to mid - 1 
            } else if (a[m] > x) {
                r = m - 1;

            // Else the element can only be present
            // in right subarray
            // so we increase our l pointer to mid + 1
            } else {
              l = m + 1;
            }  
            
        }

        notFoundIndex = l;
        int[] intArray = {foundBoolean, foundIndex, notFoundIndex};
        return intArray;
    }
}