class Solution {
    public boolean isPalindrome(String s) {
        if (s == " ") return true;
        s = s.toLowerCase();
        String result = s.replaceAll("[^a-z0-9]", "");
        String reverse = new StringBuilder(result).reverse().toString(); 
 
        System.out.printf("값 출력: result = %s, reverse = %s%n", result, reverse);
        return result.equals(reverse);
    }
}