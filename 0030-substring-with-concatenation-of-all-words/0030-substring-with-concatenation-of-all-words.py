# Slide window to check Exact length and Exact count.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        substr_len = len(words) * word_len
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            window_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    window_count[word] += 1

                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len] # remove the excess word from prev iteration
                        window_count[left_word] -= 1
                        left += word_len

                    if right - left == substr_len:
                        result.append(left)

                else:
                    window_count.clear()
                    left = right
                    
        return result
        