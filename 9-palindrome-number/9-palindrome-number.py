class Solution(object):
    def isPalindrome(self, x):
        string=str(x)
        #easier to do this for a string
       #beg=string[0]
        end=len(string)-1
        for i in range(len(string)):
            if string[i]==string[end]:
                end-=1
            else:
                return False
        return True