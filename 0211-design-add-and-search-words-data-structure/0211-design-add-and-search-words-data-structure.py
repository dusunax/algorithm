class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i) -> bool:
            if not isinstance(node, dict):
                return False

            if i == len(word):
                 return "$" in node if isinstance(node, dict) else False 

            char = word[i]
            print(char)

            if char == ".":
                for child in node.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                return dfs(node.get(char, {}), i + 1)
        
        return dfs(self.trie, 0)


            


        

# Overview
# search func has "." for wildcard for the rowercase characters.
# most "." count is 2



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)