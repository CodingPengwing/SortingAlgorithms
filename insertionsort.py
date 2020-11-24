### Insertion Sort template
##
#

# Note: 'A' stands for array

# Edit this compare function for whatever data type being sorted
def compare(object1, object2):
    if object1 < object2: return -1
    if object1 > object2: return 1
    return 0

def insertionSort(A):
    for i in range(1, len(A)):
        j = i - 1
        while j >= 0 and compare(A[j+1], A[j]) < 0:
            A[j+1], A[j] = A[j], A[j+1]
            j = j - 1
    return A