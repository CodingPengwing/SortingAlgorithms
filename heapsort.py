### Heap Sort template
##
#

# Note: 'A' stands for array

# Edit this compare function for whatever data type being sorted
def compare(object1, object2):
    if object1 < object2: return -1
    if object1 > object2: return 1
    return 0

def heapSort(A):
    # Add sentinel to top of list
    A = [None] + A
    A = heapify(A)
    for i in reversed(range(1, len(A))):
        A = eject(A, i)
    return A[1:]

def heapify(A):
    return bottomUpHeapify(A)
    
def bottomUpHeapify(A):
    n = len(A)
    for i in reversed(range(1, n//2 + 1)):
        I = A[i]
        heap = False
        while not heap and 2*i < n:
            u = 2*i
            if u < n-1:
                if compare(A[u], A[u+1]) < 0:
                    u += 1
            if compare(I, A[u]) >= 0:
                heap = True
            else:
                A[i] = A[u]
                i = u
        A[i] = I
    return A

# Eject the first element of the array (after the sentinel) down to position p.
# Bring element p up to first position and sift down to re-heapify.
def eject(A, p):
    A[1], A[p] = A[p], A[1]
    i = 1
    I = A[i]
    heap = False
    while not heap and 2*i < p:
        u = 2*i
        if u < p-1:
            if compare(A[u], A[u+1]) < 0:
                u += 1
        if compare(I, A[u]) >= 0:
            heap = True
        else:
            A[i] = A[u]
            i = u
    A[i] = I
    return A