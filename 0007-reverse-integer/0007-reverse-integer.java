class Solution {
    public int reverse(int x) {
        int num = Math.abs(x);
        int res = 0;

        while (num > 0) {
            int digit = num % 10;
            num /= 10;

            if (res > (Integer.MAX_VALUE / 10) || (res == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            }

            res = res * 10 + digit;
        }

        return x > 0 ? res : -res;
    }
}