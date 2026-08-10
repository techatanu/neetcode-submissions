class MinStack(object):

    def __init__(self):
        self.st = []
        self.minEle= None
        
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.st) == 0:
            self.st.append(value)
            self.minEle = value
        else:
            if value >= self.minEle:
                self.st.append(value)
            elif value < self.minEle:
                encoded_val = (2 * value - self.minEle)
                self.st.append(encoded_val)
                self.minEle = value
       

        

    def pop(self):
        """
        :rtype: None
        """
        if not self.st:
            return

        top_val = self.st.pop()
        if top_val < self.minEle:
            self.minEle = 2 * self.minEle - top_val
    

        

    def top(self):
        """
        :rtype: int
        """
        if not self.st:
            return
        top_val = self.st[-1]
        if top_val < self.minEle:
            return self.minEle
        return top_val


    def getMin(self):
        """
        :rtype: int
        """
        if not self.st:
            return -1
        return self.minEle

        


