def mergersort(arr):
    if len(arr)<= 1:
        return arr
    

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    sortedleft = mergersort(left)
    sortedright = mergersort(right)

    return merge(sortedleft,sortedright)

def merge(left,right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res




mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysort = mergersort(mylist)
print("sorted list " , mysort)