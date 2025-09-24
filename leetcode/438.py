from typing import List



class Solution:
    @staticmethod
    def count_symbols(s: str):
        p_chars = {}
        for c in s:
            if not c in p_chars:
                p_chars[c] = 0

            p_chars[c] += 1
        
        return p_chars

    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []

        p_chars = self.count_symbols(p)
        slide_hash = self.count_symbols(s[:len(p)])

        if p_chars == slide_hash:
            answer.append(0)

        left = 0
        for right in range(len(p), len(s)):
            slide_hash[s[left]] -= 1
            if slide_hash[s[left]] == 0:
                del slide_hash[s[left]]
            left += 1
            if s[right] not in slide_hash:
                slide_hash[s[right]] = 0
            slide_hash[s[right]] += 1

            if slide_hash == p_chars:
                answer.append(left)

        return answer

Solution().findAnagrams("cbaebabacd", "abc")