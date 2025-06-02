def  quick(arr):
    if len(arr) <= 1:
        return arr
    piviot = arr[0]
    left = [x  for x in arr[1:] if x < piviot]
    right = [x for x in arr[1:] if x >= piviot]

    return quick(left) + [piviot] + quick(right)




mylist = [5, 3, 8, 4, 2]
print(quick(mylist))
