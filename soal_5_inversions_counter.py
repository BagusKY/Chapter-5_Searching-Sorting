import time
import random

def countInversionsNaive(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def countInversionsSmart(arr):
    def mergeAndCount(arr, temp_arr, left, mid, right):
        i = left       # Pointer sub-array kiri
        j = mid + 1    # Pointer sub-array kanan
        k = left       # Pointer array gabungan
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                # Jika arr[i] > arr[j], maka semua elemen sisa di sub-array kiri
                # (dari indeks i hingga mid) pasti lebih besar dari arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1; k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1; k += 1

        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]

        return inv_count

    def mergeSortAndCount(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += mergeSortAndCount(arr, temp_arr, left, mid)
            inv_count += mergeSortAndCount(arr, temp_arr, mid + 1, right)
            inv_count += mergeAndCount(arr, temp_arr, left, mid, right)
        return inv_count

    n = len(arr)
    temp_arr = [0] * n
    return mergeSortAndCount(list(arr), temp_arr, 0, n - 1)

# --- Pengujian Waktu Eksekusi ---
print("\nSoal 5 (Uji Waktu Inversion Counter):")
sizes = [1000, 5000, 10000]

for s in sizes:
    test_array = [random.randint(1, 100000) for _ in range(s)]
    
    start_time = time.time()
    res_naive = countInversionsNaive(test_array)
    time_naive = time.time() - start_time
    
    start_time = time.time()
    res_smart = countInversionsSmart(test_array)
    time_smart = time.time() - start_time
    
    print(f"Size: {s:<6} | Naive: {time_naive:.4f}s | Smart: {time_smart:.4f}s | Valid: {res_naive == res_smart}")