nums = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

nums = list(map(int, nums.splitlines()))
nums_list = [[int(c) for c in str(n)] for n in nums]

adj_map = {}
for nums in nums_list:
    for n in nums:
        if n not in adj_map:
            adj_map[n] = set()
    [k, v1, v2] = nums
    adj_map[k].update((v1,v2))
    adj_map[v1].add(v2)

def topological_sort(adj_map, v):
    stack = []
    visited = set()
    def topol_sort(k):
        if k in visited:
            return
        visited.add(k)
        for v in adj_map[k]:
            topol_sort(v)
        stack.append(k)

    topol_sort(v)
    return stack[::-1]

sort = []
for k in adj_map:
    if k not in sort:
        sort = topological_sort(adj_map, k)
print(sort)
