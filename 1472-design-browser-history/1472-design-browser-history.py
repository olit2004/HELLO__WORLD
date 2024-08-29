class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.homepage=homepage
        self.stk1=[self.homepage]
        self.stk2=[]
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.stk1.append(url)
        self.stk2=[]
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and len(self.stk1)>1:
        
                val=self.stk1.pop()
                self.stk2.append(val)
                steps-=1
        return self.stk1[-1]
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and len(self.stk2)>0:

                val2=self.stk2.pop()
                self.stk1.append(val2)
                steps-=1
        return self.stk1[-1]
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)