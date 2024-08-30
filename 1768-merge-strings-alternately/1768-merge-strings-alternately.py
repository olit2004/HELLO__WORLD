class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=''
        c=0
        x=0
        y=0
        
        while x<len(word1)and y<len(word2):
             if c%2==0:
                    merged+=word1[x]
                    x+=1
                    
             else:       
                    merged+=word2[y]
                    y+=1   
             c+=1       
        if x<len(word1):
            for i in range(x,len(word1)):
                merged+=word1[i]
        elif y<len(word2):
            for i in range(y,len(word2)):
                merged+=word2[i]            
        return merged        