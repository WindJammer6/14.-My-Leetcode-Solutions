// Trying many cases of the Nim Game:
// n = 1: Since you go first, just simply take the 1 stone, you will win
// n = 2: Since you go first, just simply take the 2 stones, you will win
// n = 3: Since you go first, just simply take the 3 stones, you will win

// n = 4: Since you go first, regardless of how many stones you take, 1, 2, or 3, you will definitely lose

// n = 5: Since you go first, just simply take 1 stone, such as the remaining stones for the friend such
//        as the remaining stones for the friend forces him to make the '4-stones-choice'
// n = 6: Since you go first, just simply take 2 stone, such as the remaining stones for the friend such
//        as the remaining stones for the friend forces him to make the '4-stones-choice'
// n = 7: Since you go first, just simply take 3 stone, such as the remaining stones for the friend such
//        as the remaining stones for the friend forces him to make the '4-stones-choice'

// n = 8: Since you go first, regardless of how many stones you take, 1, 2, or 3, you will definitely lose,
//        as the opponent's next move will force you to make the '4-stones-choice'

// n = 9: Since you go first, just simply take 1 stone, such as the remaining stones for the friend such
//        as the remaining stones for the friend forces him to make the '8-stones-choice'
// n = 10: Since you go first, just simply take 2 stone, such as the remaining stones for the friend such
//         as the remaining stones for the friend forces him to make the '8-stones-choice'
// n = 11: Since you go first, just simply take 3 stone, such as the remaining stones for the friend such
//         as the remaining stones for the friend forces him to make the '8-stones-choice'

// n = 12: Since you go first, regardless of how many stones you take, 1, 2, or 3, you will definitely lose,
//         as the opponent's next move will force you to make the '8-stones-choice'


// Conclusion, if you start at a 'n' that is a multiple of 4, you will definitely lose, but if you start
// at a 'n' that is a multiple of 4, you will win

class Solution {
    public boolean canWinNim(int n) {
        if (n % 4 == 0){
            return false;
        } else {
            return true;
        }
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.println(solution.canWinNim(4)); // false
        System.out.println(solution.canWinNim(1)); // true
        System.out.println(solution.canWinNim(2)); // true
    }
}