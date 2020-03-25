'''
Created on 24 mar. 2020

@author: daniel
'''

def search(array, x, n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            high = mid-1
        elif array[mid] < x:
            low = mid+1
    return -1


if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10]
    x = 11
    index = search(array, x, len(array))
    if index >= 0:
        print("Number %d" % array[index] + " is at index: %d" % index)
    else:
        print("Number %d" % x + " is not in the array")
    
    