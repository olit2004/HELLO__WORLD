class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r=[]
        for i in range (n):
            if (i+1)%3==0 and (i+1)%5==0:
                r.append("FizzBuzz")
            elif (i+1)%3==0:
                r.append("Fizz")
            elif (i+1)%5==0: 
                 r.append("Buzz")
            else :
                r.append(str(i+1))
        return r       