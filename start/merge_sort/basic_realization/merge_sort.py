# def merge_sort(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid + 1, right)
#         merge(arr, left, mid, right)
        
# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid
    
#     L = [0] * n1
#     R = [0] * n2
    
#     for i in range(n1):
#         L[i] = arr[left + i]
    
#     for j in range(n2):
#         R[j] = arr[mid + j + 1]
    
#     i = 0
#     j = 0
#     k = left
    
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i+=1
#         else:
#             arr[k] = R[j]
#             j+=1
#         k+=1
    
#     while i < n1:
#         arr[k] = L[i]
#         i+=1
#         k+=1
    
#     while j < n2:
#         arr[k] = R[j]
#         j+=1
#         k+=1
        
        

def merge_sort(arr):
    if len(arr) <= 1:  # Базовый случай: массив из 1 элемента уже отсортирован
        return arr
    
    # Делим массив на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Сливаем отсортированные половины
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Слияние двух массивов
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array    

arr = [9,5,6,3,7,2,8,4,0,1]
# merge_sort(arr, 0, len(arr) - 1)
arr2 = merge_sort(arr)
print(arr2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]