class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            st = set()
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    if val in st:
                        return False
                    st.add(val)

            for col in range(9):
                st = set()
                for row in range(9):
                    val = board[row][col]
                    if val != ".":
                        if val in st:
                            return False
                    st.add(val)

                for sr in range(0,9,3):
                    for sc in range(0,9,3):
                        st = set()

                        er = sr + 2
                        ec = sc + 2

                        for row in range(sr,er+1):
                            for col in range(sc,ec+1):
                                val = board[row][col]
                                if val != ".":
                                    if val in st:
                                        return False
                                    st.add(val)
        return True


        