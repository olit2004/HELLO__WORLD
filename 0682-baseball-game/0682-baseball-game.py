class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record=[]
        for i in operations:
            if  i.lstrip('-').isdigit():
                record.append(int(i))
            elif i=="C"   :
                record.pop()
            elif i=="D"    :
                record.append(record[-1]*2)
            else:
                record.append(record[-1]+record[-2])
        return  sum(record)      