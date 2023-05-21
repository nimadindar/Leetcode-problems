"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        # returns a default dic with default value of list
        result = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('a')] += 1

            result[tuple(count)].append(s)
        return result.values()
