# TO-DO: Complete the selection_sort() function below 
test_array = [5, 4, 1, 3, 6, 2]
print('pre sort', test_array)
def selection_sort( arr ):
    # loop through n-1 elements
    if len(arr) == 0:
        return arr
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j


        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

    return arr


selection_sort(test_array)
print('post sort', test_array)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# Legacy code 

    # Problem 1

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # if arr[smallest_index] >= arr[cur_index+1]:
        #     cur_index = i+1
        #     print(arr[smallest_index])
        # elif arr[smallest_index] <= arr[cur_index+1]:
        #     smallest_index = i+1
        #     print(arr[smallest_index])
        # else:
        #     arr[0] = smallest_index
              