### simple Counting Sort template
## This sorting algorithm only really works well with small integer inputs
#

# Note: 'A' stands for array

def countingSort(A):
    min_val = min(A)
    if min_val < 0:
        A = [i-min_val for i in A]
    max_num = max(A)
    count_array = [0 for i in range(max_num+1)]
    for i in A:
        count_array[i] += 1
    A = []
    for i in range(len(count_array)):
        if count_array[i] > 0:
            count = count_array[i]
            A += [i for k in range(count)]
    if min_val < 0:
        A = [i+min_val for i in A]
    return A
