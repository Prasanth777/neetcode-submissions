
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        inverse_count_nums = defaultdict(list)
        for num, freq in count_nums.items():
            inverse_count_nums[freq].append(num)
        top_k_max_counters=[]
        for i in sorted(count_nums.values(), reverse=True)[:k]:
            top_k_max_counters.append(inverse_count_nums[i].pop())
            if len(top_k_max_counters) == k:
                break
        return top_k_max_counters

