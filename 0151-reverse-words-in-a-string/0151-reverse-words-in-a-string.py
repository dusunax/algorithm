class Solution:
    def reverseWords(self, s: str) -> str:
        # o3n_approach = " ".join(list(filter(lambda a: a is not " ", s.split()))[::-1])
        # print(o3n_approach)

        i = len(s) - 1
        word_end = -1
        result = []

        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue

            word_end = i
            word_start = i
            
            while word_start > 0 and s[word_start - 1] != " ":
                word_start -= 1

            print(word_start, word_end)
            result.append(s[word_start:word_end + 1])

            i = word_start -1 # `for` 루프는 `i = word_start`로 바꿔도 index 제어x => while문 써야함
                    
        print(result)
        return " ".join(result)
                
        
# O(3n): 문자열을 " "로 잘라서 filter하고 reverse하고 합친다
# O(1): two pointer

