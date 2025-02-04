def insertion_sort(arr):
    
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


arr = [-3, -8,-5,3,6,4,0,3, -1]
insertion_sort(arr)
print(arr)