'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

# I don't exactly know why this solution doesn't work.

def topKFrequent(nums, key):

    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i],0) + 1

    sorted_dict = {k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1], reverse=True)}

    result = list(sorted_dict.keys())

    return result[:key]
  
  # Answer
  
  def topkfrequent(nums,k):

    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums: 
        count[n] = 1 + count.get(n,0)

    for n,c in count.items():
        freq[c].append(n)

    res = []
    
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
