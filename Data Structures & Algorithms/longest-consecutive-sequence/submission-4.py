class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        ln_streak = 0
        for num in my_set:
            if num-1 not in my_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in my_set:
                    curr_num += 1
                    curr_streak += 1
                ln_streak = max(ln_streak,curr_streak)

        return ln_streak

        '''first check duplicate use ho raha hai ki nahi? if no duplicate was in res then we should think to use hashmap(set) method. for this question we have to check that previous element is in present in set or not? if not present make that curr element and check curr element + 1 , curr_element + 2 etc..

        # if it is in my_set then increase curr_sum += 1
                                            curr_streak += 1
                                        ln_streak = max(ln_streak,curr_streak) (this will be outside while loop)

            return ln_streak'''
        

        