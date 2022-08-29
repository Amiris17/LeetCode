class Solution(object):
    def myAtoi(self, s
               ):
        s = s.lstrip()  # Step 1Read in and ignore any leading whitespace.


        
        sign = 1
        i = 0

        if s == "":
            return 0
        if s[i] == "+":
            i += 1

        elif s[i] == "-":
            sign = -1
            i += 1
        parsed = 0
        while i<len(s):
            if s[i].isdigit() == False:

                break
            else:
                parsed = parsed * 10 + int(s[i])
            i+=1
                # print(i)

        parsed *= sign

        if parsed> 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif parsed < -2 ** 31:
            return -2 ** 31
        else:
            return parsed