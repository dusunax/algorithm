/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2; 
            
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