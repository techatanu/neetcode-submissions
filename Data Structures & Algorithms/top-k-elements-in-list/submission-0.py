class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}
        for num in nums:
            if num in frq:
                frq[num] += 1
            else:
                frq[num] = 1
        heap = []
        for key, val in frq.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap,[val,key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
