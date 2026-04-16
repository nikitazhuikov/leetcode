class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        if len(s) != len(t):
            return False
        for chr in s:
            if chr in s_dict:
                s_dict[chr] += 1
            else:
                s_dict[chr] = 1
        for chr in t:
            if chr in s_dict:
                s_dict[chr] -= 1
        return all(value == 0 for value in s_dict.values())

if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))