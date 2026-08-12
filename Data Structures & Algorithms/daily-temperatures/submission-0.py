class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n-1,-1,-1):
            curr_temp = temperatures[i]
            while st and temperatures[st[-1]] <= curr_temp:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)        
        return ans

        

        
