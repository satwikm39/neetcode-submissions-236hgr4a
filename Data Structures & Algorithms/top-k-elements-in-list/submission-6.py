class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for n, count in freq.items():
            bucket[count].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        