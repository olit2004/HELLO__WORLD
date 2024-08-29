class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        stk=[]
        
        for i in range(len(temperatures)) :
            while  len(stk)!=0 and temperatures[i]>temperatures[stk[-1]]:
                pi=stk.pop()
                answer[pi]=i-pi
            stk.append(i)   
        return answer   
            