import time
import random

def linear_search(arr, target):
    comparisons=0
    for i in range(len(arr)):
        comparisons+=1
        if arr[i]==target:
            return i,comparisons
    return -1,comparisons
arr = [2,5,10,15,23,35,48,60,75,90]
target=35
index,comparisons=linear_search(arr, target)
print("Array:",arr)
print("Target:",target)
print("Index Found:",index)
print("Comparisons:",comparisons)