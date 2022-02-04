ls = []
def sortnum(number):
    global ls
    if number == []:
        return
    else:
        t = number.index(max(number))
        j = number.pop(t)
        ls.append(j)
        return sortnum(number)

inp = list(map(int,input("Enter innput : ").split(',')))
sortnum(inp)
print(f'List after Sorted : {ls}')