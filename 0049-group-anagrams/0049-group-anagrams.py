class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for str in strs:
            sorted_key = ''.join(sorted(str))
            # if sorted_key not in result:
            #     result[sorted_key] = []
            result[sorted_key].append(str)
        
        return list(result.values())
            
