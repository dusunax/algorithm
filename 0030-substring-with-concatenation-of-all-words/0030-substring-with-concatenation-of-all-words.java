class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        int wordLen = words[0].length(); // 각 단어의 길이
        int concatLen = words.length * wordLen; // 모든 단어를 연결한 문자열의 길이
        Map<String, Integer> wordCount = new HashMap<>();
        
        // 단어의 빈도를 계산
        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        // 각 offset을 기준으로 슬라이딩 윈도우 검사
        for (int i = 0; i < wordLen; i++) {
            int left = i, right = i;
            Map<String, Integer> windowCount = new HashMap<>();
            
            while (right + wordLen <= s.length()) {
                String word = s.substring(right, right + wordLen);
                right += wordLen;

                if (wordCount.containsKey(word)) {
                    windowCount.put(word, windowCount.getOrDefault(word, 0) + 1);

                    // 단어의 빈도가 초과된 경우, 왼쪽 포인터 이동
                    while (windowCount.get(word) > wordCount.get(word)) {
                        String leftWord = s.substring(left, left + wordLen);
                        windowCount.put(leftWord, windowCount.get(leftWord) - 1);
                        left += wordLen;
                    }

                    // 길이가 맞으면 결과에 추가
                    if (right - left == concatLen) {
                        result.add(left);
                    }
                } else {
                    // 포함되지 않는 단어가 나온 경우, 윈도우 초기화
                    windowCount.clear();
                    left = right;
                }
            }
        }

        return result;
    }
}