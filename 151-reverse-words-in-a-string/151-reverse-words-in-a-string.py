class Solution(object):
    def reverseWords(self, string):
        result=string.split()
        fin_string=" ".join(result)
        #result= " ".join(string.split())
        #So at this moment all bad white spaces should be filtered out so all we need to do is every single time we encounter a white space swap orders like reversing a linked list.
        new_list = []
        fin_string=fin_string.split()
        place_holder=len(fin_string)
        for i in range(place_holder):

            new_list.append(fin_string[place_holder-1])
            place_holder-=1
            reversed_=" ".join(new_list)
        return reversed_
