# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    if len(arr) == 0:
        return arr
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        print('cur', cur_index)
        print('sml', smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        arr_len = len(arr)
        while arr_len > 0:
            if arr[smallest_index] >= arr[cur_index]:
                smallest_index = cur_index
                cur_index += 1
            else:
                arr[0] = arr[smallest_index] 




        # TO-DO: swap

    return arr

test_array = [5, 4, 1, 3, 6, 2]

selection_sort(test_array)

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
              