class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_fq = {}
        for ch in s:
            ch_fq[ch] = ch_fq.get(ch,0) + 1
        for ch in t:
            if ch not in ch_fq:
                return False
            else:
                if ch_fq[ch] == 0:
                    return False
                else:
                    ch_fq[ch] -= 1
        return True
        