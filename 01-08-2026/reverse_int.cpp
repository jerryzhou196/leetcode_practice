class Solution {
    public:
        int reverse(int x) {
            int rev = 0;
            // cout << INT_MAX << endl;
            while (x != 0){
                int pop = x % 10;
                x /= 10;
                // cout << rev << endl;
                if ((rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) ||
                    (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7))) {
                    return 0;
                }
                rev = rev * 10 + pop;
            }
            return rev;
        }
    };
    // 964632435
    // 2147483647
