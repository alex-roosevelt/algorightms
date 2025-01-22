import random


def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    elem = random.choice(arr)
    left = list(filter(lambda x: x < elem, arr))
    center = [i for i in arr if i == elem]
    right = list(filter(lambda x: x > elem, arr))
    return quick_sort(left) + center + quick_sort(right)


arr = [9,5,6,3,7,2,8,4,0,1]
# merge_sort(arr, 0, len(arr) - 1)
arr2 = quick_sort(arr)
print(arr2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]