from itertools import permutations

def cross(xs, ys):
    results = set()
    for x in xs:
        for y in ys:
            results.update({x+y,x-y,x*y})
            if y != 0:
                results.add(x/y)
    return results
         
def all_possible_permute(nums):
    result = set()
    for p in [[{x} for x in list(xs)] for xs in permutations(nums)]:
        result.update(all_possible(p))
    return result
         
def all_possible(nums):
    if len(nums) == 1:
        return nums[0]
    result = set()
    for i in range(len(nums)-1):
        new_nums = nums[:i] + [cross(nums[i], nums[i+1])] + nums[i+2:]
        result.update(all_possible(new_nums))
    return result
         
def count_consecutive_pos(nums):
    for i in range(1, 10000000):
        if round(i,10) not in nums:
            return i-1

maximum = (0, None)
for a in range(1,10):  # no way 0 is included
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                count = count_consecutive_pos(all_possible_permute([a,b,c,d]))
                if count > maximum[0]:
                    maximum = (count, (a,b,c,d))
                    
# print(sorted([x for x in all_possible_permute([1,2,5,8]) if round(x % 1, 3) == 0 and x > 0]))
print(maximum)

