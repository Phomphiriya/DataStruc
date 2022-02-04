def bubble_sort(lst):
    result = lst.copy()
    for i in range(len(result)-1):
        swapped = False
        for k in range(len(result)-1-i):
            if result[k] > result[k+1]:
                result[k], result[k+1] = result[k+1], result[k]
                swapped = True
        if not swapped:
            break
    return result

def subset_sum(target, lst, left=0, res=[], carry=[]):  # knapsack style
    if left >= len(lst):
        return res
    carry.append(lst[left])
    if sum(carry) == target:
        res.append(carry.copy())
    res = subset_sum(target, lst, left+1, res, carry)
    carry.pop()
    res = subset_sum(target, lst, left+1, res, carry)
    return res

def list_sorting(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

inp = input("Enter Input : ").split('/')
target = int(inp[0])
lst = bubble_sort(list(map(int, inp[1].split())))
viable_lst = subset_sum(target, lst)
if len(viable_lst) == 0: print("No Subset")
else:
    viable_lst = list_sorting(viable_lst)
    for item in viable_lst: print(item)