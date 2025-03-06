/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return binarySearch(n, 1, n);
    }

    // Java implementation of iterative Binary Search (copy-pasted from GeekforGeeks website: https://www.geeksforgeeks.org/binary-search-in-java/), with
    // some modifications for the Leetcode question
    int binarySearch(int a, int l, int r) {
        while (l <= r) {
            // I initially used 'int m = (l + r) / 2', but thats causing me to fail at 1 of the test cases where n is very large. Apparently, according to the 
            // discussion, doing 'int m = (l + r) / 2' may cause **integer overflow** at very large values, so a safer alternate code is this 'int m = l + (r - l) / 2'
            // which prevents having excessive values being stored in the 'int m' variable to pass the test cases where n is very large

            //  (Note: In Java, the maximum value for an int is 2,147,483,647 ('Integer.MAX_VALUE'), and the minimum value is -2,147,483,648 ('Integer.MIN_VALUE'))
            int m = l + (r - l) / 2;
            

            // If element gives 'isBadVersion(version) == true', then
            // first check if its the first bad version by checking if its immediate 
            // element on the left is 'isBadVersion(version) == false'

            // Else, the first bad version can only be present in left subarray
            // so we decrease our r pointer to mid - 1 
            if (isBadVersion(m) == true) {
                if (isBadVersion(m-1) == false){
                    return m;
                } else{
                    r = m - 1;
                }
            }

            // If element gives 'isBadVersion(version) == false', then
            // first check if the next element on its right is the first bad 
            // version by checking if its immediate element on the right is 
            // 'isBadVersion(version) == true'
            
            // Else the first bad version can only be present in right 
            // subarray so we increase our l pointer to mid + 1
            else {
                if (isBadVersion(m+1) == true){
                    return m+1;
                } else{
                    l = m + 1;
                }
            }  
        }

        // No Element Found
        return -1;
    }
}
