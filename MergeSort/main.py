'''
Created on 24 mar. 2020

@author: daniel
'''

def merge(array, L, R):
    i = j = k = 0
    nL = len(L)
    nR = len(R)
    
    while i < nL and j < nR:
        if L[i] <= R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1
    
    while i<nL:
        array[k] = L[i]
        i+=1
        k+=1
    while j<nR:
        array[k] = R[j]
        j+=1
        k+=1
        
def mergeSort(array):
    if len(array) < 2:
        return
        
    mid = len(array)//2
    L = array[:mid]
    R = array[mid:]        
    mergeSort(L)
    mergeSort(R)
    merge(array, L, R)

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    array = [1,5,3,4,2]
    print("Given array is: ", end="\n")
    printArray(array)
    mergeSort(array)
    print("Sorted array is: ", end="\n")
    printArray(array)