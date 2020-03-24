'''
Created on 24 mar. 2020

@author: daniel
'''

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]        
        j = i-1        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    
if __name__ == '__main__':
    array = [1, 5 ,3, 4, 2]
    insertionSort(array)
    for i in range(len(array)):
        print(array[i])
