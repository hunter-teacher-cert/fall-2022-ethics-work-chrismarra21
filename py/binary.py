# https://py3.codeskulptor.org/#user307_VR9Kig4dOZ_1.py
# Christine Marra
# CSCI 77800 Fall 2022
# collaborators: Maxwell Yearwood
# consulted: 


"""Binary Search Iterative Function. Returns index of target if present, else returns -1"""


def binarySearchIterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test list #1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binarySearchIterative(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


  #Test list #2

arr2 = [2,4,6,8,42]
x = 9
# Function call
#result = binary_search(arr, 0, len(arr)-1, x)
result = binarySearchIterative(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array" + "---> "+ str(-1)) 



  
"""Recursive Binary Search Function. Returns index of target if present, else returns -1"""


def binarySearch(arr, target):
    return binarySearchRec(arr,0, len(arr)-1, target)

  
# Returns index of x in arr if present, else -1
def binarySearchRec(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearchRec(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearchRec(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


def isSorted(arr):
    retBoo = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
           return False
    return retBoo
  


# Test list #1 
arr = [ 2, 3, 4, 10, 40 ]
x = 40
#print("Is the list sorted?" + " " + isSorted(arr))
# Function call
#result = binary_search(arr, 0, len(arr)-1, x)
result = binarySearch(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array" + "---> "+ str(-1))

#Test list #2

arr2 = [2,4,6,8,42]
x = 9
# Function call
#result = binary_search(arr, 0, len(arr)-1, x)
result = binarySearch(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array" + "---> "+ str(-1))
