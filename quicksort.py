### Quick Sort template
##
#

# Note: 'A' stands for array, 'p' stands for pivot

# Edit this compare function for whatever data type being sorted
def compare(object1, object2):
    if object1 < object2: return -1
    if object1 > object2: return 1
    return 0

def quickSort(A):
    if len(A) <= 1:
        return A
    A, p = partition(A)
    array_l = quickSort(A[:p])
    array_r = quickSort(A[p+1:])
    A = array_l + [A[p]] + array_r
    return A

# Partitions the A with the pivot point in between the 2 partitions
# Returns partitioned A along with index of pivot
def partition(A):
#     A, p = choosePivot(A)

#     A, p = lomutoPartition(A)
    A, p = hoarePartition(A)
    return A, p


# Finds the median of the 3 values as pivot and puts it at start of array.
def choosePivot(A):
    chooseFrom = [A[0], A[len(A)//2], A[-1]]
    pivot = sorted(chooseFrom)[1]
    p = A.index(pivot)
    A[0], A[p] = A[p], A[0]
    return A
   
      
def lomutoPartition(A):
    pivot = A[0]
    u = 0
    for i in range(u+1, len(A)):
        if compare(A[i], pivot) < 0:
            u += 1
            A[u], A[i] = A[i], A[u]
    A[0], A[u] = A[u], A[0]
    return A, u
            
    
def hoarePartition(A):
    pivot = A[0]
    i = 1
    u = len(A)-1
    while True:
        while A[i] <= pivot and i < u:
            i += 1
        while A[u] > pivot and i <= u:
            u -= 1
        if i < u:
            A[i], A[u] = A[u], A[i]
        else:
            break
    # Swap pivot into position
    A[0], A[u] = A[u], A[0]
    return A, u



