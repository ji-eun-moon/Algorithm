class Solution:
    def groupAnagrams(self, strs):

        anagram_dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            anagram_dic.setdefault(key, [])
            anagram_dic[key].append(s)

        return list(anagram_dic.values())

solve = Solution()
print(solve.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(solve.groupAnagrams(strs = [""]))
print(solve.groupAnagrams(strs = ["a"]))