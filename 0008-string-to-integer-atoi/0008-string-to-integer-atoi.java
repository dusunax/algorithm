class Solution {
    public int myAtoi(String s) {
        int result = 0;
        int sign = 1;
        int index = 0;
        int max = Integer.MAX_VALUE; // JAVA!
        int min = Integer.MIN_VALUE;

        s = s.trim();

        if (index < s.length() && s.charAt(index) == '-') {
            sign = -1;
            index++;
        } else if (index < s.length() && s.charAt(index) == '+') {
            index++;
        }

         while (index < s.length() && Character.isDigit(s.charAt(index))) {
            int digit = s.charAt(index) - '0';

            if (result > (max - digit) / 10) {
                return sign == 1 ? max : min;
            }

            result = result * 10 + digit;
            index++;
        }

        return result * sign;
    }
}

// JAVA

// ; is required

// JAVA의 Stirng은 array가 아니다.
// string.charAt()

// Wrapper Class의 메소드 직접 호출
// Character.isDigit()

// char 타입(primitive type) 
// char: 단일 문자 하나를 표현하는 기본 데이터 타입, '', 16비트 Unicode, 

// String 타입(reference type)
// String: 문자열(문자들의 시퀀스)을 표현하는 객체, "", 