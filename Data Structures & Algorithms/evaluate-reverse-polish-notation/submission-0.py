class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                b = st.pop()
                a = st.pop()
                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(a-b)
                elif t == '*':
                    st.append(a*b)
                else:
                    res = a//b
                    if res < 0 and a % b != 0:
                        res += 1
                    st.append(res)
            else:
                st.append(int(t))
        return st[-1]


        '''we can use
val = a//b # positive case will be handed correctly
if val<0 and a%b != 0:# negative and not perfectly divisible
val+=1 # for negative case e.g. -13/12 → val =(a//b)= -2, but we have to truncate towards zero so val+=1 → val = -1
stack.append(val)'''