### Merge Sort template
##
#

# Note: 'A' stands for array

# Edit this compare function for whatever data type being sorted
def compare(object1, object2):
    if object1 < object2: return -1
    if object1 > object2: return 1
    return 0

def mergeSort(A):
    if len(A) <= 1:
        return A
    A_l = A[:len(A)//2]
    A_r = A[len(A)//2:]
    A_l = mergeSort(A_l)
    A_r = mergeSort(A_r)
    A = merge(A_l, A_r)
    return A

def merge(A1, A2):
    i = 0
    u = 0
    output = []
    while i < len(A1) and u < len(A2):
        if compare(A1[i], A2[u]) <= 0:
            output.append(A1[i])
            i += 1
        else:
            output.append(A2[u])
            u += 1
    if i == len(A1):
        output += A2[u:] 
    if u == len(A2):
        output += A1[i:]
    return output

