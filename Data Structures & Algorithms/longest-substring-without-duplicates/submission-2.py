class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)

        seen = set()
        max_length = 0
        left, right = 0, 1
        seen.add(s[left])
        while right<len(s):
            if s[right] in seen:
                # found a duplicate, move the left pointer until you reach the duplicate
                max_length = max(max_length, right - left)
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                
                left += 1

            seen.add(s[right])
            right += 1                   
        
        return max(max_length, len(seen))

            