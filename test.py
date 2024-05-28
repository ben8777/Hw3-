def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        print(f"排序過程: {arr}")  
        quick_sort_helper(arr, low, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print(f"原始數列: {arr}")
quick_sort(arr)
print(f"排序後數列: {arr}")
