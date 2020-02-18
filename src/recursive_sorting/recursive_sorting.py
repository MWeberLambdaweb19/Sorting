# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a = 0
    b = 0
    for i in range(elements):
       if a >= len(arrA):
           merged_arr[i] = arrB[b]
           b += 1
       elif b >= len(arrB):
           merged_arr[i] = arrA[a]
           a += 1
       elif arrA[a] < arrB[b]:
           merged_arr[i] = arrA[a]
           a += 1
       elif arrB[b] < arrA[a]:
           merged_arr[i] = arrB[b]
           b += 1    
    # TO-DO
    # for i in elements:
        # if all elements of arrA are in elements, put the next element
        # of arrB in merge

        # if all elements of len B are in elements, put in elements
        # of len arrA

        # if next element in arrA is smaller, add to merged array

        # if next element in arrB is smaller, add to merged array
    # for i in elements:
    #     if arrA[i] in elements:
    #         elements.append(arrB[i+1])
    #     elif arrB[i] in elements:
    #         elements.append(arrA[i+1])
    #     elif arrA[i] > arrA[i+1]:
    #         merged_arr.append(arrA[i])
    #     elif arrB[i] > arrB[i+i]:
    #         merged_arr.append(arrB[i])
    # if arrA[0] < arrB[0]:
    #     merged_arr.append(arrA[0])
    # else: 
    #     merged_arr.append(arrB[0])
    # if arrA[0] < arrA[1]:
    #     merged_arr.append(arrA[0])
    # elif arrA[0] < arrB[0]:
    #     merged_arr.append(arrA[0])
    # elif arrA[1] > arrA[0]:
    #     merged_arr.append(arrA[1])
        
    # if arrB[0] < arrB[1]:
    #     merged_arr.append(arrB[0])
    # elif arrB[0] < arrA[0]:
    #     merged_arr.append(arrB[0])
    # elif arrB[1] > arrB[0]:
    #     merged_arr.append(arrB[1])
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # need to split this element in half
    # need to split those elements in half down to one using recursion
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[ : len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    arr = merge(left, right)
    print('left', left)
    print('right', right)

    return arr
    # return merge(left, right)

test_arr = [5, 3, 2, 1, 6, 4, 7, 8, 9, 10]
print(merge_sort(test_arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
