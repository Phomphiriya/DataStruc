def insertionIdx(lst, curr_index, value): 
    if curr_index > 0 and lst[curr_index - 1] > value:
        lst[curr_index] = lst[curr_index - 1]
        return insertionIdx(lst, curr_index - 1, value)
    else: return curr_index

def insertionSort(lst, start=0, length=None, progress=0):
    if length is None: length = len(lst)
    val = lst[start]
    idx = insertionIdx(lst, start, val)
    lst[idx] = val
    progress += 1
    if progress > 1:
        if len(lst[progress:]) != 0:
            print(f"insert {val} at index {idx} : {lst[:progress]} {lst[progress:]}")
        else: print(f"insert {val} at index {idx} : {lst[:progress]}")

    if start+1 < length:insertionSort(lst, start+1, length, progress)

if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ").split()))
    insertionSort(in_lst)
    print("sorted")
    print(in_lst)