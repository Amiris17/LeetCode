class Solution(object):
    def isPalindrome(self, x):
        string=str(x)
        #easier to do this for a string
       #beg=string[0]
        end=len(string)-1
        for i in range(len(string)):
            if string[i]==string[end]: #if beginning is equal to the end decrement i else return false and if the else is not reached we return True
                end-=1
            else:
                return False
        return True