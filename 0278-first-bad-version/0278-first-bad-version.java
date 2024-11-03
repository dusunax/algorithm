/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = (int) Math.floor(left + (right - left) / 2); 
            
            if(isBadVersion(mid)){
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}

/**
* ❗️ error: incompatible types: possible lossy conversion from double to int int mid = Math.floor((left + right) / 2);
 */ 
// In Java, you need to explicitly cast the result to int,
// or you can avoid Math.floor altogether since integer division will naturally yield an integer.
// but since we need integer for the pointer~ let's use floor with return value of int\U0001f914

// how can we cast?
// do: int mid = (int) Math.floor((left + right) / 2);

/**
* ❗️Time Limit Exceeded (when n is 2126753390)
 */
 // use `left + (right - left) / 2` than `(left + right) / 2`
 // avoids overflow, because (right - left) will be smaller than right and left when added back to left, 
 // preventing the sum from exceeding int limits.


/**
* \U0001f449 `left + (right - left) / 2` and `(left + right) / 2`
 */
// how to prevent overflow & calculate the same result
// when if, left = 1,000, right = 2,000
// - (left + right) / 2 is 1500, (1000 + 2000) / 2 = 1500
// - left + (right - left) / 2 is also 1500, 1000 + (2000 - 1000) / 2 = 1000 + 500 = 1500
