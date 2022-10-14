class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        resulting_str=""
        
        for i in range(len(command)):
            if command[i]=="G":
                resulting_str+="G"
            if command[i]=="(" and command[i+1]==")": #lets assume that all inputs are valid
                resulting_str+="o"
            if command[i]=="a":
                resulting_str+="al"
        
        return resulting_str
            
            