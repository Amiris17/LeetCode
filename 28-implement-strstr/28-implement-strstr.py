class Solution(object):
    def strStr(self,haystack,needle):
        if len(needle)==0:
            return 0
        if haystack is None or needle is None:
            return -1
        if haystack==needle:
            return 0
        needle_length=len(needle)

        for i in range(len(haystack)):
            if haystack[i:i+needle_length]==needle:
                return i
        return -1
