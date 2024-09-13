class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrfix = strs[0]

        for str in strs[1:]:
            while str.find(commonPrfix) != 0:
                commonPrfix = commonPrfix[:-1]
                if not commonPrfix:
                    return ""
        
        return commonPrfix
