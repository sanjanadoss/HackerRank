//https://leetcode.com/problems/palindrome-number/

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x>0 && x%10==0)){
            return false;
        }
        int rev = 0;
        while (x>rev){
            rev = rev*10 + x%10;
            x = x/10;
        }
        if (x==rev || x==rev/10){
            return true;
        }
        else{
            return false;
        }
    }
};

//Runtime: 12 ms, faster than 76.52% of C++ online submissions for Palindrome Number
//Memory Usage: 5.9 MB, less than 32.40% of C++ online submissions for Palindrome Number.
