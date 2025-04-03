class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.println(solution.maximum69Number(9669));  // 9969
        System.out.println(solution.maximum69Number(9996));  // 9999
        System.out.println(solution.maximum69Number(9999));  // 9999

    }
}

class Solution {
    public int maximum69Number (int num) {
        String s = String.valueOf(num);
        int i = s.indexOf("6");

        if (i == -1){
            return num;
        } else{
            s = s.substring(0, i) + "9" + s.substring(i + 1);
            int newNum = Integer.parseInt(s);
            return newNum;
        }
    }
}