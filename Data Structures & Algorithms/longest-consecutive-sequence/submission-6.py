class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        mx = 0
        seen = set()

        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            
            if (num + 1) not in mp and (num - 1) not in mp:
                mp[num] = num
            elif (num + 1) in mp and (num - 1) in mp:
                new_start = mp[num - 1]
                mp.pop(new_start, -1)
                mp.pop(num - 1, -1)
                new_end = mp[num + 1]
                mp.pop(new_end, -1)
                mp.pop(num + 1, -1)
                mp[new_end] = new_start
                mp[new_start] = new_end
            elif (num + 1) in mp:
                new_end = mp[num + 1]
                mp.pop(new_end, -1)
                mp.pop(num + 1, -1)
                mp[num] = new_end
                mp[new_end] = num
            elif (num - 1) in mp:
                new_start = mp[num - 1]
                mp.pop(new_start, -1)
                mp.pop(num - 1, -1)
                mp[num] = new_start
                mp[new_start] = num

        
        for start, end in mp.items():
            mx = max(end - start + 1, mx)
        
        return mx

'''

so i think the concept here is to take note of intervals

so i think what we can do is

we keep a hashmap

-1 dict

2: 3
3: 2

4

5 :7
7: 5

can use .pop(key, -1) to pop regardles of if the key is in the hashmap or not

'''